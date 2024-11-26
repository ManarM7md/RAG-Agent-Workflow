# Reliable RAG Agents with LangGraph, Groq-Llama-3, and Chroma

This project demonstrates the development of reliable **Retrieval-Augmented Generation (RAG) agents** using **LangGraph**, **Groq-Llama-3**, and **Chroma**. By integrating state-of-the-art concepts from research papers, the agent achieves robust, accurate, and efficient handling of complex natural language queries.

---

## Workflow of the RAG Agent

### 1. Routing
Directs queries to either:
- **Vectorstore**: For LLM-related questions.
- **Web Search**: For other general queries.

### 2. Retrieval
Retrieves relevant context documents and grades them for relevance.

### 3. Hallucination Detection
Validates answers to ensure factual accuracy.

### 4. Synthesis
Combines the validated context to generate concise, accurate responses.

---

## Technology Stack

- **Embedding Model**: `BAAI/bge-base-en-v1.5`
- **LLM**: `Groq-Llama3-8B`
- **Vectorstore**: `Chroma`
- **Agent Framework**: `LangGraph`
- **Search API**: `Tavily Search API`

---

## Conclusion
This project demonstrates the integration of state-of-the-art RAG techniques into a reliable, efficient agent framework. By leveraging LangGraph and Groq-Llama-3, we achieve improved reliability, accuracy, and compatibility for advanced natural language understanding tasks.
