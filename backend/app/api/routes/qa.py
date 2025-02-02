from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.document import Document
from app.core.database import get_db
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import ChatPromptTemplate
from app.utils.pdf_utils import extract_text_from_pdf
from langchain.vectorstores import FAISS

router = APIRouter()


@router.post("/ask")
async def ask_question(
    document_id: int, question: str, db: AsyncSession = Depends(get_db)
):
    # Verify document exists
    result = await db.execute(select(Document).where(Document.id == document_id))

    document = result.scalar_one_or_none()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    text_content = extract_text_from_pdf(document.path)
    embeddings = OpenAIEmbeddings()

    # Store embeddings in FAISS
    vector_store = FAISS.from_texts([text_content], embeddings)
    vector_store.save_local("vector_db/")

    # Load FAISS database
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.load_local(
        "vector_db/", embeddings, allow_dangerous_deserialization=True
    )
    retriever = vector_store.as_retriever()

    # Define RAG pipeline
    system_prompt = (
        "Use the given context to answer the question. "
        "If you don't know the answer, say you don't know. "
        "Use three sentences maximum and keep the answer concise. "
        "Context: {context}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [("system", system_prompt), ("human", "{question}")]
    )

    # Use RetrievalQA instead of create_retrieval_chain
    qa_chain = RetrievalQA.from_llm(
        ChatOpenAI(temperature=0.7, model="gpt-4-turbo"), retriever=retriever
    )

    # Get answer
    response = qa_chain.run(question)
    return {"answer": response}
