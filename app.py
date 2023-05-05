from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter


def main():
    load_dotenv()
    # print(os.getenv("OPENAI_API_KEY"))
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF")

    # upload pdf
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    # extract text
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # split into chunks
        text_splitter = CharacterTextSplitter(
            separators="/n",
            chunk_size=1000,
            chunk_overlap=500,
            length_function=len
        )

        st.write(text)


if __name__ == "__main__":
    main()
