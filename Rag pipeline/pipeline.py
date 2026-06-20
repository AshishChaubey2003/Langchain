from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

# Load PDF
loader = PyPDFLoader("attention.pdf")
docs = loader.load()

# Split
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

documents = splitter.split_documents(docs)

# Embeddings
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Vector DB
vectorstore = Chroma.from_documents(
    documents,
    embedding=embedding
)

# Retriever
retriever = vectorstore.as_retriever(search_kwargs={"k":3})

# LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="gemma2-9b-it"
)

# Query
query = "What is attention mechanism?"

# Retrieve docs
docs = retriever.invoke(query)

context = "\n\n".join([doc.page_content for doc in docs])

prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{query}
"""

response = llm.invoke(prompt)

print(response.content)