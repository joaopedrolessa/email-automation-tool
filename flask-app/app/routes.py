from flask import Blueprint, render_template, request, redirect, url_for, flash
import io
try:
    import PyPDF2
except ImportError:
    PyPDF2 = None
from werkzeug.utils import secure_filename
import os

# Importa as funções de IA
## Removido integração IA

# Create a Blueprint for the app
main = Blueprint('main', __name__)

ALLOWED_EXTENSIONS = {'txt', 'pdf'}
UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'uploads')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/', methods=['GET', 'POST'])
def home():
    conteudo_email = None
    categoria = None
    resposta = None
    if request.method == 'POST':
        input_type = request.form.get('input_type')
        if input_type == 'text':
            conteudo_email = request.form.get('email_text')
        elif input_type == 'file':
            file = request.files.get('file')
            if file and file.filename.endswith('.txt'):
                conteudo_email = file.read().decode('utf-8')
            elif file and file.filename.endswith('.pdf') and PyPDF2:
                pdf = PyPDF2.PdfReader(file)
                conteudo_email = ''
                for page in pdf.pages:
                    conteudo_email += page.extract_text() or ''
            else:
                flash('Envie um arquivo .txt ou .pdf válido.')
                return redirect(request.url)

        # Apenas exibe o conteúdo extraído
        if conteudo_email:
            flash('Conteúdo do email extraído com sucesso!')
        else:
            flash('Não foi possível extrair o conteúdo do email.')
        return render_template('index.html', conteudo_email=conteudo_email)