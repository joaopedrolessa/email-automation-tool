import openai
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def classificar_email_simples(texto):
    produtivo_keywords = [
        "suporte", "problema", "erro", "dúvida", "atualização", "caso", "solicitação", "ajuda", "urgente", "pendente",
        "preciso de ajuda", "favor verificar", "poderia analisar", "necessito de resposta", "solicito informação",
        "reunião", "agendar", "documentação", "relatório", "atualizar cadastro", "acompanhamento",
        "responder", "retorno", "pendência", "ação necessária", "solicito providências", "encaminhar para setor"
    ]
    improdutivo_keywords = [
        "agradeço", "agradecemos", "obrigado", "obrigada",
        "parabéns", "felicidades", "feliz aniversário", "bom trabalho",
        "tenha um ótimo dia", "desejo sucesso", "boa sorte",
        "apenas para informar", "sem necessidade de resposta", "mensagem automática",
        "cumprimentos", "saudações", "atenciosamente"
    ]
    texto_lower = texto.lower()
    for palavra in produtivo_keywords:
        if palavra in texto_lower:
            return "Produtivo"
    for palavra in improdutivo_keywords:
        if palavra in texto_lower:
            return "Improdutivo"
    return None  # Não classificado

def classificar_email_ia(texto):
    prompt = f"Classifique o seguinte email como Produtivo ou Improdutivo:\n\n{texto}\n\nCategoria:"
    try:
        resposta = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=10
        )
        categoria = resposta.choices[0].text.strip()
        if "produtivo" in categoria.lower():
            return "Produtivo"
        elif "improdutivo" in categoria.lower():
            return "Improdutivo"
        else:
            return "Indefinido"
    except Exception as e:
        return f"Erro IA: {e}"

def classificar_email_hibrido(texto):
    # Primeiro tenta classificar pelas regras
    categoria = classificar_email_simples(texto)
    if categoria:
        return categoria
    # Se não classificar, usa IA
    return classificar_email_ia(texto)

def sugerir_resposta(categoria):
    if categoria == "Produtivo":
        return "Obrigado pelo contato! Sua solicitação será analisada e retornaremos em breve."
    elif categoria == "Improdutivo":
        return "Agradecemos sua mensagem!"
    else:
        return "Não foi possível sugerir uma resposta automática."
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

# Certifique-se de baixar os recursos necessários do NLTK
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def preprocess_text(text, lang='portuguese'):
    """
    Remove stop words, pontuação e aplica lemmatização ao texto.
    """
    # Tokenização simples por espaço
    tokens = text.lower().split()
    # Remove pontuação
    tokens = [t.strip(string.punctuation) for t in tokens if t.strip(string.punctuation)]
    # Remove stop words
    stop_words = set(stopwords.words(lang))
    tokens = [t for t in tokens if t not in stop_words]
    # Lemmatização
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return ' '.join(tokens)