

# Rotas principais do app Flask
from flask import Blueprint, render_template, request, redirect, url_for, flash
import io
try:
    import PyPDF2  # Biblioteca para leitura de PDFs
except ImportError:
    PyPDF2 = None
from werkzeug.utils import secure_filename
import os

# Importa funções utilitárias de NLP e classificação
from .utils import preprocess_text, classificar_email_hibrido, sugerir_resposta

# Blueprint para organização das rotas
main = Blueprint('main', __name__)

# Extensões permitidas para upload
ALLOWED_EXTENSIONS = {'txt', 'pdf'}
# Pasta de upload configurável via variável de ambiente
UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'uploads')

def allowed_file(filename):
    """
    Verifica se o arquivo possui extensão permitida.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/', methods=['GET', 'POST'])
def home():
    """
    Rota principal: exibe formulário e processa upload/texto de email.
    Segue boas práticas de validação, feedback ao usuário e separação de responsabilidades.
    """
    conteudo_email = None
    conteudo_processado = None
    categoria = None
    resposta = None
    if request.method == 'POST':
        input_type = request.form.get('input_type')
        # Processa texto manual
        if input_type == 'text':
            conteudo_email = request.form.get('email_text')
        # Processa upload de arquivo
        elif input_type == 'file':
            file = request.files.get('file')
            if file and file.filename.endswith('.txt'):
                conteudo_email = file.read().decode('utf-8')
            elif file and file.filename.endswith('.pdf') and PyPDF2:
                # Leitura segura de PDF
                pdf = PyPDF2.PdfReader(file)
                conteudo_email = ''
                for page in pdf.pages:
                    conteudo_email += page.extract_text() or ''
            else:
                # Feedback para arquivo inválido
                flash('Envie um arquivo .txt ou .pdf válido.')
                return redirect(request.url)

        # Pré-processamento e classificação
        if conteudo_email:
            conteudo_processado = preprocess_text(conteudo_email)
            categoria = classificar_email_hibrido(conteudo_email)
            resposta = sugerir_resposta(categoria)
            # Feedback positivo ao usuário
            flash('Conteúdo do email extraído, pré-processado e classificado com sucesso!')
        else:
            # Feedback negativo ao usuário
            flash('Não foi possível extrair o conteúdo do email.')
        # Renderiza template com resultados
        return render_template('index.html', conteudo_email=conteudo_email, conteudo_processado=conteudo_processado, categoria=categoria, resposta=resposta)

    # GET: renderiza página inicial sem dados
    return render_template('index.html', conteudo_email=conteudo_email, conteudo_processado=None, categoria=None, resposta=None)