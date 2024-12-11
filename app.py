from Agents.LLMcall import get_answere
from RagTool.rag import retrival
import time
import streamlit as st
import os

# Set a directory to save uploaded files
UPLOAD_DIRECTORY = "PDF"

# Create the directory if it doesn't exist
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

# Title of the app
st.title("QA Bot For Zania.ai")

# String input for collection name
colleciton_name = st.text_input("Enter a Collection name!")

# File upload
uploaded_file = st.file_uploader("Upload a PDF file")

rg = None  # Initialize retrival object to None

if uploaded_file is not None:
    # Save the file to the upload directory
    file_path = os.path.join(UPLOAD_DIRECTORY, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Create retrieval object
    rg = retrival(colleciton_name, file_path)
    st.success(f"File saved and index created!")

# Timer start
st1 = time.perf_counter()

# Question input and processing
if rg:  # Ensure rg is initialized before processing questions
    userinput = st.text_input("Enter a question:")
    if userinput:
        # Process the user question
        context = rg.mul_query_collection(userinput)
        # context = rg.query_collection(userinput, query_expansion=False)
        ans = get_answere(context, userinput)

        # Display the answer
        st.write(f"{ans}")

        # Log execution time
        en = time.perf_counter()
        print(f"Execution time: {en - st1} seconds")
else:
    st.warning("Please upload a file to enable the QA bot.")
