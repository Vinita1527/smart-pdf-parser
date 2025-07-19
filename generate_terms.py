import fitz
import json
import sys
from collections import Counter
import re

def extract_terms(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:
        full_text += page.get_text()

    words = re.findall(r'\b[a-zA-Z]{4,}\b', full_text.lower())
    stopwords = {
        "this", "that", "with", "from", "these", "those", "have", "been", "which",
        "will", "would", "there", "their", "about", "into", "some", "many", "more",
        "most", "such", "also", "using", "other", "than", "very", "only", "what", "when"
    }

    filtered_words = [w for w in words if w not in stopwords]
    common = Counter(filtered_words).most_common(10)
    return {term: [] for term, _ in common}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_terms.py <pdf_path>")
        sys.exit(1)

    path = sys.argv[1]
    terms = extract_terms(path)

    with open("term_definitions.json", "w", encoding="utf-8") as f:
        json.dump(terms, f, indent=2)
