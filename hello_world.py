import os
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from PIL import Image, ImageFilter

app = Flask(__name__)

# Define a pasta de uploads para armazenar as imagens
UPLOAD_FOLDER = os.path.join(app.root_path, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Cria a pasta 'uploads' caso ela não exista
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    # Lista as imagens na pasta de uploads
    image_files = [f for f in os.listdir(UPLOAD_FOLDER) if os.path.isfile(os.path.join(UPLOAD_FOLDER, f))]
    return render_template('index.html', image_files=image_files)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['imagem']
    original_file_path = os.path.join(UPLOAD_FOLDER, 'imagem_original.jpg')
    filtered_file_path = os.path.join(UPLOAD_FOLDER, 'imagem_com_filtro.jpg')
    file.save(original_file_path)

    apply_filter(original_file_path, filtered_file_path)

    return redirect(url_for('home'))

def apply_filter(original_path, filtered_path):
    with Image.open(original_path) as img:
        filtered_img = img.filter(ImageFilter.CONTOUR)
        filtered_img.save(filtered_path)

# Rota para servir as imagens na pasta 'uploads'
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)