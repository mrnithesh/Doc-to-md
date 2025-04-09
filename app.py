import streamlit as st
import io
import os
from markitdown import MarkItDown

# Page configuration
st.set_page_config(
    page_title="MarkItDown",
    page_icon="📝",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .title-container {
        text-align: center;
        margin-bottom: 2rem;
    }
    .title {
        font-weight: 800;
        color: #262730;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #4F4F4F;
        margin-bottom: 2rem;
    }
    .stButton button {
        width: 100%;
        border-radius: 5px;
        height: 3rem;
        font-weight: 600;
        background-color: #4169e1;
        color: white;
    }
    .upload-container {
        border: 2px dashed #dedede;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    .footer {
        text-align: center;
        color: #888888;
        font-size: 0.8rem;
        margin-top: 3rem;
    }
    .social-links {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: 1rem;
    }
    .social-links a {
        color: #4169e1;
        text-decoration: none;
        font-weight: 600;
    }
    .sidebar-info {
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize MarkItDown
md = MarkItDown()

# Sidebar
with st.sidebar:
    st.title("About MarkItDown")
    
    st.markdown("### What is MarkItDown?")
    st.markdown("MarkItDown is a tool that transforms various document formats into clean, readable Markdown format.")
    
    st.markdown("### Supported File Types")
    st.markdown("""
    - PDF (.pdf)
    - Word Documents (.docx)
    - PowerPoint (.pptx)
    - Excel (.xlsx, .xls)
    - HTML (.html)
    - CSV (.csv)
    - JSON (.json)
    - XML (.xml)
    - EPUB (.epub)
    """)
    
    st.markdown("### How to Use")
    st.markdown("""
    1. Upload a supported document
    2. Wait for conversion to complete
    3. Preview the markdown output
    4. Download your markdown file
    """)
    
    st.markdown("### Connect with Me")
    

    
    st.markdown("[GitHub](https://github.com/mrnithesh)", unsafe_allow_html=True)
    st.markdown("[LinkedIn](https://linkedin.com/in/mrnithesh)", unsafe_allow_html=True)
    

    
    st.markdown("### Developed by")
    st.markdown("**Mr. Nithesh 💖**")
    st.markdown("A passionate developer and tech enthusiast.")

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

# UI Components
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Title section
    st.markdown('<div class="title-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">MarkItDown 📝</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Transform your documents into clean Markdown format</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Supported file types
    supported_files = ["pdf", "docx", "pptx", "xlsx", "xls", "html", "csv", "json", "xml", "epub"]
    
    # Upload section
    st.markdown('<div class="upload-container">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=supported_files)
    st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_file is not None:
        # Processing section
        st.markdown(f"**{uploaded_file.name}**")
        
        with st.spinner("Converting to Markdown..."):
            markdown_text = convert_to_markdown(uploaded_file)
        
        if markdown_text:
            # Result section
            st.success("Conversion successful!")
            
            # Download button for the markdown file
            st.download_button(
                label="Download Markdown",
                data=markdown_text,
                file_name=f"{os.path.splitext(uploaded_file.name)[0]}.md",
                mime="text/markdown"
            )
            
            # Display the markdown in a clean container
            with st.expander("Preview Markdown", expanded=True):
                st.markdown(markdown_text)
    
    # Footer
    st.markdown('<div class="footer">Created by Mr. Nithesh 💖</div>', unsafe_allow_html=True)

