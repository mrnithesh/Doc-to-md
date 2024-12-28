import streamlit as st
from markitdown import MarkItDown
import os
md=MarkItDown()
def convert(file):
    result=md.convert(file)
    print(result.text_content)
    return result.text_content

st.title("MarkItDown")
uploaded_file = st.file_uploader("upload file",type=["docx","pdf","xlsx"])
if uploaded_file is not None:
    
    result=convert(uploaded_file)
    if result:
        st.write(result.text_content)

# result=md.convert("resume.pdf")
# print(result.text_content)