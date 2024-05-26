import os
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='../../frontend/build', static_url_path='/')

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '../static/uploads')
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'pptx', 'ipynb'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_categories():
    categories = [name for name in os.listdir(app.config['UPLOAD_FOLDER']) if os.path.isdir(os.path.join(app.config['UPLOAD_FOLDER'], name))]
    return {'categories': categories}

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    category = request.form.get('category')  # Get selected category from form data
    if not category:
        return jsonify({'error': 'No category selected'})
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], category, filename)  # Save file to selected category folder
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create category folder if it doesn't exist
        file.save(file_path)
        return jsonify({'success': 'File uploaded successfully'})
    return jsonify({'error': 'File type not allowed'})

@app.route('/search', methods=['POST'])
def search():
    # Implement search functionality here
    pass

@app.route('/categories')
def categories():
    return jsonify(get_categories())

if __name__ == '__main__':
    app.run(debug=True)
