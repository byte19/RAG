from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

# Add the src directory to the system path
sys.path.append(os.path.abspath("../src"))


from backend.python_test.ingestion import process_File

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400

    # Save the file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    print(f"File saved to {file_path}")

    processed = process_File(file_path)
    return jsonify({"message": f"File '{file.filename}' uploaded and saved and {processed}.", "path": file_path}), 200


@app.route('/chat', methods=['POST'])
def chat():
    pass

if __name__ == '__main__':
    app.run(debug=True)
