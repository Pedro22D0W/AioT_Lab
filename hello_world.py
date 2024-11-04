import os
from flask import *
from PIL import Image, ImageFilter


app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(),'uploads')

@app.route('/')
def home():
    image_url = request.args.get('image_url')
    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
    file = request.files['imagem']
    original_file_path = os.path.join(UPLOAD_FOLDER, 'imagem_original.jpg')
    filtered_file_path = os.path.join(UPLOAD_FOLDER, 'imagem_com_filtro.jpg')
    file.save(original_file_path)

    apply_filter(original_file_path, filtered_file_path)

    return redirect(url_for('home'))

def apply_filter(original_path, filtered_path):
    # Abrir a imagem
    with Image.open(original_path) as img:
        # Aplicar um filtro de borrão
        filtered_img = img.filter(ImageFilter.CONTOUR)
        # Salvar a imagem filtrada com um nome diferente
        filtered_img.save(filtered_path) 
    
    
    return redirect(url_for('home'))





    


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)