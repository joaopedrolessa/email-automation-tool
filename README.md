# 🤖 AutoU | AI Email Automation & Classification

<div align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS_EC2-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" />
  <img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" />
</div>

### 📖 Project Overview
**AutoU** is an intelligent automation tool designed to optimize corporate workflows. It uses **Natural Language Processing (NLP)** to read, classify, and draft responses for incoming emails automatically.

Unlike simple rule-based automations, this project leverages **Zero-Shot Classification (Transformers)** to understand context without extensive model training, classifying emails as **Productive** or **Unproductive** with high accuracy.

---

### ⚙️ Architecture & Tech Stack

The application follows a modular architecture deployed on **Linux environments**:

* **Backend:** Python 3.10+ & Flask (Web Interface & API).
* **AI Engine:** Hugging Face Transformers (`facebook/bart-large-mnli`) for local Zero-Shot Classification.
* **Data Processing:** `PyPDF2` for PDF extraction and `NLTK` for text preprocessing.
* **Infrastructure:** Designed for deployment on **AWS EC2** (Ubuntu Server).

---

### ☁️ Cloud & Deployment
This project was engineered to run in a cloud environment, demonstrating **DevOps** and **Infrastructure** skills:

* **AWS EC2:** Hosted on a Linux instance to simulate a real-world production server.
* **Linux Automation:** Configured using SSH and Bash scripts for environment setup.
* **Offline Capability:** The AI model runs locally on the server, removing dependencies on expensive external APIs (like OpenAI), ensuring data privacy and cost reduction.

---

### 🔄 How It Works (Pipeline)

1.  **Input:** User uploads `.txt` or `.pdf` files via the Web UI.
2.  **Extraction & Cleaning:** The system extracts raw text and removes noise (stopwords/formatting).
3.  **AI Classification:**
    * The content is fed into the **BART Transformer Model**.
    * The model assigns a probability score to labels: `Produtivo` (Business Value) vs `Improdutivo` (Spam/Noise).
4.  **Action:** Based on the highest confidence score, the system generates a standardized response template ready to be sent.

---

### 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/joaopedrolessa/AutoU.git](https://github.com/joaopedrolessa/AutoU.git)
   cd AutoU
````

2.  **Set up the Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    # .\venv\Scripts\activate # Windows
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    # Note: This will download the Transformer model (approx. 1.5GB)
    ```

4.  **Run the Flask App:**

    ```bash
    python run.py
    ```

    Access at: `http://localhost:5000`

-----

### 🚧 Future Improvements

  * Implement **Docker** containerization for easier deployment.
  * Fine-tune the model specifically for Portuguese business vocabulary.
  * Integrate directly with Gmail/Outlook APIs for real-time fetching.

-----

### 👨‍💻 Author

**João Pedro (Jaypi)**

  * *Backend Developer | Python Automation | AWS Enthusiast*
  * [LinkedIn Profile](https://www.linkedin.com/in/joaopedrolessa/)

<!-- end list -->

```

---

### 🏁 CHECKLIST FINAL DO GITHUB (Faça isso agora):

1.  **Atualize esse README** do projeto `AutoU`.
2.  **Vá no seu Perfil Principal** (Overview).
3.  Clique em "Customize your pins".
4.  **A Ordem Perfeita dos Pins (Top 4):**
    1.  `AutoU` (O projeto de IA + AWS - Mostra modernidade).
    2.  `CalculadoraMedia` (O projeto Java - Mostra base acadêmica e MVC).
    3.  `stg-catalog-challenge` (Seu Fullstack mais complexo).
    4.  `node-ts-webapi...` (Backend puro).

**Assim que você terminar esses 4 passos, seu GitHub virou uma máquina de vendas.**

Me avise com um "OK" quando terminar. Aí, pegaremos aquele texto que criei para o seu **LinkedIn** (na mensagem anterior) e vamos garantir que ele esteja lá certinho. O GitHub já vencemos! 🚀
```
