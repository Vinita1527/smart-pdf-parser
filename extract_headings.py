import fitz  # PyMuPDF
import json

def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)
    headings = []

    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                font_sizes = [span["size"] for line in block["lines"] for span in line["spans"]]
                if font_sizes and max(font_sizes) >= 14:
                    text = " ".join(span["text"].strip() for line in block["lines"] for span in line["spans"]).strip()
                    if len(text.split()) < 15 and text not in [h["text"] for h in headings]:
                        headings.append({"text": text, "page": page_num})

    if not headings:
        headings = [{"text": "Full Document", "page": 0}]

    return headings

if __name__ == "__main__":
    extract_headings("uploads/sample.pdf")
