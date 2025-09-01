````markdown
# 📧 AutoU - Classificação e Resposta Automática de Emails  

AutoU é uma aplicação **Flask** que automatiza a leitura, classificação e resposta de e-mails corporativos em **português**.  

O sistema classifica mensagens em **Produtivo** ou **Improdutivo** e sugere automaticamente uma resposta padrão para cada categoria.  
Toda a classificação é feita **localmente** com modelos *Transformers* (*zero-shot classification*), sem depender de APIs pagas ou serviços externos.  

---

## 🚀 Funcionalidades principais
- Upload de e-mails em **.txt** ou **.pdf** diretamente na interface web.
- Classificação automática em **Produtivo** (útil para o negócio) ou **Improdutivo** (spam/irrelevante).
- Sugestão imediata de resposta padronizada por categoria.
- Processamento **local e offline** (não requer API paga).
- Código simples e modular para fácil personalização.  

---

## 🛠️ Stack Tecnológica
- **Python 3.10+**
- **Flask** – backend e interface web
- **Hugging Face Transformers** – modelo `facebook/bart-large-mnli` para zero-shot classification
- **PyPDF2** – leitura e extração de texto de PDFs
- **NLTK** – pré-processamento opcional (stopwords, lematização)

> As dependências estão listadas em `requirements.txt`.

---

## 🔄 Como funciona
1. **Entrada:** usuário envia o texto do e-mail ou faz upload de um arquivo `.txt` ou `.pdf` via interface (`templates/index.html`).
2. **Extração:** PDFs são lidos com `PyPDF2`; textos passam por limpeza opcional em `preprocess_text`.
3. **Classificação:**  
   - A função `classificar_email_hibrido` chama o pipeline *zero-shot classification* do modelo `facebook/bart-large-mnli`.  
   - São usados **labels em português**: `Produtivo` e `Improdutivo`.  
   - O modelo retorna a categoria com **maior score de confiança**.
4. **Resposta:** `sugerir_resposta(categoria, email)` devolve uma mensagem **fixa e padrão** para cada categoria.  
   - Exemplo: Produtivo → “Sua solicitação foi recebida e será analisada.”  
5. **Resultado:** o usuário visualiza no navegador a classificação e a resposta sugerida.

---

## 💻 Como rodar localmente
1. Clone o repositório e entre na pasta:  
   ```bash
   git clone <url-do-repositorio>
   cd email-automation-tool/flask-app
````

2. Crie e ative o ambiente virtual:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate   # Windows
   source venv/bin/activate # Linux/Mac
   ```
3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   pip install transformers torch  # caso não estejam no requirements
   ```
4. Execute a aplicação:

   ```bash
   python run.py
   ```
5. Acesse no navegador:
   👉 `http://localhost:5000`

---

## 🏗️ Estrutura do projeto

* **`app/routes.py`** → recebe uploads/inputs, extrai conteúdo e chama a classificação.
* **`app/utils.py`** → funções centrais:

  * `preprocess_text`: limpeza opcional do texto.
  * `classificar_email_transformers`: pipeline de classificação.
  * `sugerir_resposta`: gera resposta fixa por categoria.

---

## ⚖️ Decisões de Design

* **Zero-shot Transformers**: elimina necessidade de dataset próprio e treinos pesados.
* **Respostas fixas**: solução simples para o escopo inicial (um template por categoria).
* **Execução local**: evita custos com APIs externas e garante maior controle do fluxo.

---

## 🐞 Limitações conhecidas

* Recursos gratuitos limitados (ex.: servidores AWS free-tier).
* O modelo em inglês (`bart-large-mnli`) pode perder precisão em português.
* Respostas são **muito genéricas** (uma só por categoria).

---

## 🎯 Como melhorar a precisão

* Refinar **labels** em português (ex.: “solicitação de suporte”, “mensagem irrelevante”).
* Definir **threshold de confiança** antes de classificar.
* Combinar regras simples (regex, palavras-chave) junto com o modelo.
* Fine-tuning de um modelo em **português** com dataset pequeno e específico.

---

## 🔮 Próximos passos

* Substituir respostas fixas por **templates dinâmicos** ou **modelos generativos**.
* Criar **dataset em português** e treinar um classificador dedicado.
* Adicionar suporte a múltiplas categorias além de Produtivo/Improdutivo.
* Deploy em **Docker** para facilitar distribuição.

---

## 📜 Licença

MIT — veja o arquivo `LICENSE`.
