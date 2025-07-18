### 🔍 About
smart-pdf-parser is a Python tool to extract structured outlines (title, H1, H2, H3 with page numbers) from PDFs. It helps in analyzing and navigating PDF documents by providing a clear hierarchy of headings.

---

### 📦 Features
- Processes PDF files from a specified input folder
- Extracts document title and headings (H1, H2, H3)
- Outputs structured JSON files with page numbers and heading levels

---

### 🚀 How to Run

1. Place your PDF files in the `input/` folder.  
2. Run the Python script:
   ```bash
   python extract_outline.py
3. The output JSON files will be generated in the output/ folder.

### 📚 Dependencies
Python 3.10+

PyMuPDF (fitz)

## Install dependencies via:

pip install -r requirements.txt

### 🗂 Folder Structure
smart-pdf-parser
├── app.py                         # Main Flask app
├── extract_headings.py           # Extracts headings from documents
├── extract_relevant_sections.py  # Filters relevant sections
├── generate_terms.py             # Generates key terms
├── headings.json                 # Output: extracted headings
├── relevant_sections.json        # Output: key content sections
├── term_definitions.json         # Output: term definitions
├── term_to_heading_map.json      # Output: terms mapped to headings
├── requirements.txt              # Python dependencies
├── sample.pdf                    # Sample input document
├── templates/
│   └── index.html                # HTML template for web UI
├── uploads/                      # Folder for user-uploaded files
├── __pycache__/                  # Auto-generated cache

