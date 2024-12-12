# LLM Advance Rag

## Overview
This repository demonstrates the integration of large language models (LLMs) using the LangChain framework and OpenAI's GPT-based APIs. It provides tools for building question-answering (QA) bots that can retrieve, process, and analyze textual data, such as PDF documents, using advanced AI models.

---

## Features
- **Document Chunking and Indexing**: Process PDF documents into smaller chunks and index them for retrieval.
- **Query Expansion**: Expand user queries using advanced techniques for better information retrieval.
- **Reranking**: Use a cross-encoder to rank retrieved documents based on relevance to the query.
- **Streamlit Interface**: A user-friendly UI for uploading files and querying the indexed documents.

---

## Requirements

### Python Libraries
- `langchain`
- `chromadb`
- `streamlit`
- `sentence-transformers`
- `python-dotenv`
- `pydantic`
- `concurrent.futures`

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/akarshan-kumar/Adv-rag.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Adv-rag
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your OpenAI API key to the `config.ini` file.

5. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## Usage

### 1. Upload a PDF
- Navigate to the Streamlit app and enter a collection name.
- Upload a PDF document to process.
- The document is automatically chunked and indexed.

### 2. Ask Questions
- Enter a question related to the uploaded document.
- The app retrieves relevant chunks, processes them through the LLM, and provides an answer.

---

## Project Structure
- **Agents**: Contains custom LLM prompt templates.
- **RagTool**: Retrieval-augmented generation utilities, including query expansion and document indexing.
- **config.ini**: Configuration file for API keys and settings.
- **app.py**: Streamlit interface for the QA bot.
- **README.md**: This documentation.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
