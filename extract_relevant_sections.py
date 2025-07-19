import fitz
import json
from collections import defaultdict
import re

def clean_word(word):
    return re.sub(r'[^\w\s]', '', word).lower()

def extract_relevant_sections(pdf_path, headings):
    doc = fitz.open(pdf_path)
    relevant_sections = {}
    term_to_heading_map = defaultdict(set)

    if not headings:
        full_text = [line.strip() for page in doc for line in page.get_text().split('\n') if line.strip()]
        relevant_sections["Full Document"] = full_text
    else:
        for heading in headings:
            page_num = heading["page"]
            heading_text = heading["text"]
            lines = []

            for j in range(page_num, min(page_num + 2, len(doc))):
                page = doc[j]
                page_lines = page.get_text().split('\n')
                for line in page_lines:
                    clean = line.strip()
                    if clean and heading_text not in clean:
                        lines.append(clean)
                        for word in clean.split():
                            term_to_heading_map[clean_word(word)].add(heading_text)

            relevant_sections[heading_text] = lines[:5]

    term_to_heading_map = {term: list(sections) for term, sections in term_to_heading_map.items()}

    return relevant_sections, term_to_heading_map

if __name__ == "__main__":
    from extract_headings import extract_headings
    extract_relevant_sections("uploads/sample.pdf", extract_headings("uploads/sample.pdf"))
