import streamlit as st
import io
import os
from markitdown import MarkItDown

# Initialize MarkItDown
md = MarkItDown()

def convert_to_markdown(uploaded_file):
    try:
        # Read the uploaded file as bytes
        bytes_data = uploaded_file.getvalue()
        
        # Create a temporary file
        temp_file_path = f"temp_{uploaded_file.name}"
        with open(temp_file_path, "wb") as f:
            f.write(bytes_data)
        
        # Use the file path approach for conversion
        result = md.convert(temp_file_path)
        
        # Clean up the temporary file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
            
        if result is None or not hasattr(result, 'text_content'):
            raise Exception("Conversion failed or result doesn't have text_content attribute.")
            
        return result.text_content
    except Exception as e:
        st.error(f"Error during conversion: {str(e)}")
        return None

# UI
st.title("MarkItDown Document Converter")
st.write("Convert your documents to Markdown format using the MarkItDown library")

# Supported file types
supported_files = ["pdf", "docx", "pptx", "xlsx", "xls", "html", "csv", "json", "xml", "epub"]

uploaded_file = st.file_uploader("Upload a document to convert", type=supported_files)

if uploaded_file is not None:
    st.write(f"Processing: **{uploaded_file.name}**")
    
    with st.spinner("Converting to Markdown..."):
        markdown_text = convert_to_markdown(uploaded_file)
    
    if markdown_text:
        # Download button for the markdown file
        st.download_button(
            label="Download Markdown",
            data=markdown_text,
            file_name=f"{os.path.splitext(uploaded_file.name)[0]}.md",
            mime="text/markdown"
        )
        
        # Display the markdown
        st.subheader("Converted Markdown:")
        st.markdown(markdown_text)
        
        