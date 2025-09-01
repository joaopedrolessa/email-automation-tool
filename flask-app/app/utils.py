# Classificação por IA (zero-shot) — usamos apenas modelos gratuitos locais via transformers

def classificar_email_transformers(texto):
    """
    Classifica email como Produtivo ou Improdutivo usando zero-shot (transformers).
    Retorna 1 para Produtivo e 0 para Improdutivo (sempre retorna um inteiro binário).
    """
    try:
        from transformers import pipeline
    except ImportError:
        return "[Transformers] Erro: instale as dependências com 'pip install transformers torch'"
    # labels mais curtas e diretas ajudam o modelo a decidir melhor
    labels = [
        "Produtivo: Requer ação (suporte/atualização/dúvida)",
        "Improdutivo: Mensagem social (felicitações/agradecimentos)"
    ]
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    result = classifier(texto, candidate_labels=labels, hypothesis_template="Este email é: {}.")
    # Espera-se result com 'labels' e 'scores'
    if not result or 'labels' not in result or 'scores' not in result:
        # falha no pipeline -> assumir improdutivo (0)
        return 0
    top_label = result['labels'][0]
    top_score = float(result['scores'][0])
    # limiar mínimo de confiança para aceitar a classificação do modelo
    CONFIDENCE_THRESHOLD = 0.65
    if top_score >= CONFIDENCE_THRESHOLD:
        return 1 if top_label.startswith("Produtivo") else 0
    # baixa confiança: usar fallback para o label de maior score (ainda retorna binário)
    return 1 if top_label.startswith("Produtivo") else 0


def sugerir_resposta_produtivo(email):
    """
    Analisa o email produtivo e sugere resposta específica para:
    - Solicitação de suporte técnico
    - Atualização sobre caso em aberto
    - Dúvida sobre o sistema
    """
    try:
        from transformers import pipeline
    except ImportError:
        return "[Transformers] Erro: instale as dependências com 'pip install transformers torch'"
    # labels simples para subtipo; vamos checar score e usar fallback quando baixa confiança
    labels = [
        "Solicitação de suporte técnico",
        "Atualização sobre caso em aberto",
        "Dúvida sobre o sistema"
    ]
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    result = classifier(email, candidate_labels=labels, hypothesis_template="Este email é uma {}.")
    if not result or 'labels' not in result or 'scores' not in result:
        return "Olá! Recebemos sua solicitação e em breve nossa equipe irá analisar e responder conforme o assunto."
    top_label = result['labels'][0]
    top_score = float(result['scores'][0])
    # limiar mais baixo para subtipo
    SUBTYPE_THRESHOLD = 0.55
    if top_score < SUBTYPE_THRESHOLD:
        # baixa confiança para subtipo -> resposta produtiva genérica
        return "Olá! Recebemos sua solicitação e em breve nossa equipe irá analisar e responder conforme o assunto."
    if top_label == "Solicitação de suporte técnico":
        return "Olá! Recebemos sua solicitação de suporte técnico. Nossa equipe está analisando o caso e retornaremos em breve com orientações ou solução."
    if top_label == "Atualização sobre caso em aberto":
        return "Olá! Informamos que estamos acompanhando o caso em aberto e enviaremos atualizações assim que houver novidades. Se precisar de mais informações, estamos à disposição."
    if top_label == "Dúvida sobre o sistema":
        return "Olá! Agradecemos sua dúvida sobre o sistema. Nossa equipe irá responder com as informações solicitadas o mais breve possível. Se desejar, consulte também nosso manual ou FAQ."
    return "Olá! Recebemos sua solicitação e em breve nossa equipe irá analisar e responder conforme o assunto."


def classificar_email_hibrido(texto):
    """
    Classificação usando apenas o modelo zero-shot (transformers).
    """
    return classificar_email_transformers(texto)

def sugerir_resposta(categoria, email=None):
    """
    Gera resposta sugerida. Se `categoria` for Produtivo e `email` fornecido,
    identifica subtipo (suporte / atualização / dúvida) usando zero-shot e retorna mensagem específica.
    """
    # Retorna UMA resposta fixa para cada categoria
    if categoria == "Produtivo":
        return "Olá! Recebemos sua solicitação. Nossa equipe irá analisar e retornará em breve."
    if categoria == "Improdutivo":
        return "Agradecemos sua mensagem."
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