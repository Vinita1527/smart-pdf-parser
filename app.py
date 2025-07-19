from flask import Flask, render_template, request, redirect
import os
import json
from extract_headings import extract_headings
from extract_relevant_sections import extract_relevant_sections
from generate_terms import extract_terms

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    if (
        os.path.exists('headings.json') and
        os.path.exists('relevant_sections.json') and
        os.path.exists('term_to_heading_map.json')
    ):
        with open('headings.json', 'r', encoding='utf-8') as f:
            headings = json.load(f) or []

        with open('relevant_sections.json', 'r', encoding='utf-8') as f:
            relevant = json.load(f) or {}

        with open('term_to_heading_map.json', 'r', encoding='utf-8') as f:
            term_definitions = json.load(f) or {}

        filename = relevant.get('__filename__') if isinstance(relevant, dict) else None

        if isinstance(relevant, dict) and '__filename__' in relevant:
            relevant.pop('__filename__')

        return render_template('index.html',
                               headings=headings,
                               relevant=relevant,
                               term_definitions=term_definitions,
                               filename=filename)
    return render_template('index.html', headings=[], relevant={}, term_definitions={}, filename=None)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    file = request.files['pdf_file']
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Step 1: Extract headings
        headings = extract_headings(filepath)
        with open('headings.json', 'w', encoding='utf-8') as f:
            json.dump(headings, f, indent=2)

        # Step 2: Extract sections & term mapping
        relevant, term_map = extract_relevant_sections(filepath, headings)
        relevant['__filename__'] = file.filename
        with open('relevant_sections.json', 'w', encoding='utf-8') as f:
            json.dump(relevant, f, indent=2)

        with open('term_to_heading_map.json', 'w', encoding='utf-8') as f:
            json.dump(term_map, f, indent=2)

        print("✅ Extraction complete. JSON files updated.")

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
