import streamlit as st
from langchain_google_vertexai import ChatVertexAI
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser

# Google Vertex AI Initialization
import vertexai
from google.colab import userdata

# Streamlit Sidebar Configuration
st.sidebar.title("Configuration")
project_id = st.sidebar.text_input("Google Cloud Project ID", "your_project_id")
api_key = st.sidebar.text_input("Google API Key", type="password")

# Initialize VertexAI
vertexai.init(project=project_id)
llm = ChatVertexAI(model="gemini-1.5-flash", api_key=api_key)

# Document Loading
urls = st.text_area(
    "Enter URLs (one per line):",
    "\n".join([
        "https://lilianweng.github.io/posts/2023-06-23-agent/",
        "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
        "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
    ]),
).splitlines()

st.write(f"Processing {len(urls)} URLs...")
docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

# Split Documents
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=512, chunk_overlap=0)
doc_splits = text_splitter.split_documents(docs_list)

# Create Embeddings and VectorStore
embed_model = FastEmbedEmbeddings(model_name="intfloat/multilingual-e5-large")
vectorstore = Chroma.from_documents(doc_splits, embed_model, collection_name="local-rag")
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# Define Prompt for RAG
rag_prompt = PromptTemplate(
    template="""Use retrieved context to answer the question:
    Question: {question}
    Context: {context}
    Answer:""",
    input_variables=["question", "context"]
)

# Interaction Section
st.title("Question Answering System")
question = st.text_input("Ask a question:", "What is prompt engineering?")
if question:
    # Retrieve documents
    docs = retriever.invoke(question)
    context = "\n\n".join(doc.page_content for doc in docs)

    # Generate answer
    answer_prompt = rag_prompt.format(question=question, context=context)
    answer = llm(answer_prompt)

    st.subheader("Answer")
    st.write(answer)
