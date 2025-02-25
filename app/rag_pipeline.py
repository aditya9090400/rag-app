# from langchain.llms import Ollama
from langchain_community.llms import Ollama
from app.retrieval import retrieve_documents

llm = Ollama(model="llama3")

async def generate_answer(query: str, docs):
    relevant_docs = retrieve_documents(query, docs)
    
    context = "\n".join([doc["content"] for doc, _ in relevant_docs])
    prompt = f"Based on the following documents, answer the question: {query}\n\n{context}"
    
    response = llm(prompt)
    return response
