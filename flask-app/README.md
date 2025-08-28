# AutoU - Classificação e Resposta Automática de Emails

## Descrição do Projeto

Aplicação web para automatizar a leitura, classificação e resposta de emails recebidos por uma empresa do setor financeiro, utilizando inteligência artificial.

## Funcionalidades

- Upload de emails em formato `.txt`, `.pdf` ou inserção direta de texto.
- Classificação automática dos emails em:
  - **Produtivo:** Requer ação ou resposta específica.
  - **Improdutivo:** Não requer ação imediata.
- Sugestão de resposta automática baseada na classificação.
- Interface web intuitiva para upload e exibição dos resultados.

## Requisitos Técnicos

### Interface Web

- Formulário para upload de arquivos ou inserção de texto.
- Botão para envio do email para processamento.
- Exibição da categoria atribuída e resposta sugerida.

### Backend Python

- Leitura e pré-processamento do conteúdo dos emails (NLP: remoção de stop words, stemming/lemmatização).
- Classificação do email usando API de IA (ex: OpenAI, Hugging Face, etc.).
- Geração de resposta automática adequada à categoria.
- Integração entre backend e interface web.

### Hospedagem

- Deploy da aplicação em nuvem (Heroku, Vercel, AWS, GCP, etc.).
- Disponibilização de link público funcional.

## Entregáveis

- Código fonte no GitHub (scripts Python, HTML, requirements.txt, dados de exemplo, README).
- Vídeo demonstrativo (3-5 minutos) apresentando a solução, interface, funcionamento e explicação técnica.
- Link da aplicação hospedada na nuvem.

## Critérios de Avaliação

- Funcionalidade e experiência do usuário.
- Qualidade técnica e organização do código.
- Uso eficaz de IA para classificação e resposta.
- Hospedagem funcional e acessível.
- Interface web intuitiva e visualmente agradável.
- Autonomia e resolução de problemas.
- Clareza na demonstração e comunicação.

## Instruções de Entrega

- Enviar links do repositório, vídeo e aplicação publicada via formulário oficial.
- Certificar-se de que todos os links estão públicos e acessíveis.

---

## Como Executar Localmente

1. Clone o repositório:
   ```
   git clone <url-do-repositorio>
   cd email-automation-tool/flask-app
   ```
2. Crie e ative o ambiente virtual:
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
4. Execute a aplicação:
   ```
   python run.py
   ```
5. Acesse `http://localhost:5000` no navegador.

## Observações

- Para rodar o processamento de IA, configure as chaves de API necessárias no arquivo `.env` ou nas variáveis de ambiente.
- Para deploy, siga as instruções da plataforma escolhida (Heroku, Vercel, etc.).
- Inclua exemplos de emails para teste na pasta `data/` se necessário.

---

## Checklist de Implementação

- [x] Formulário web permite upload de `.txt`, `.pdf` ou inserção de texto
- [ ] Backend lê e processa o conteúdo do email
- [ ] Pré-processamento de texto (remoção de stop words, stemming/lemmatização)
- [ ] Classificação automática (Produtivo/Improdutivo) usando IA
- [ ] Geração de resposta automática baseada na classificação
- [ ] Exibição dos resultados na interface web
- [ ] Deploy da aplicação em nuvem (Heroku, Vercel, AWS, etc.)
- [ ] Link público funcional da aplicação
- [ ] Vídeo demonstrativo gravado e publicado
- [x] Repositório organizado e documentado
- [x] README com instruções claras de execução local e deploy

---

**Capriche na interface e na experiência do usuário!**

Dúvidas? Consulte o escopo acima ou entre em contato pelo canal oficial do processo seletivo.