# Assistente RAG - Notas Fiscais

---

## Descrição

O **Assistente RAG** é uma aplicação web desenvolvida com Flask que funciona como um assistente inteligente para responder perguntas relacionadas a notas fiscais, mas poderia ser qualquer outra coisa no db vetorizado. Utiliza técnicas de Recuperação Baseada em Conhecimento (RAG - Retrieval-Augmented Generation) para fornecer respostas precisas e contextualizadas a partir de um repositório de informações.
<img width="1874" height="888" alt="image" src="https://github.com/user-attachments/assets/7ff47365-ad9f-4579-9032-ca53ff74ed7c" />
---

## Funcionalidades

- Interface web simples e intuitiva para interação via texto.
- Processamento dinâmico de perguntas enviadas pelo usuário.
- Respostas geradas com destaque de elementos importantes (ex: negrito).
- Tratamento de erros para garantir experiência estável.
- Visualização das perguntas e respostas em formato amigável.

---

## Tecnologias

- **Backend:** Python, Flask  
- **Frontend:** HTML5, CSS3 (estilização customizada)  
- **Lógica de Resposta:** Implementada no módulo `main.py` (função `responder`)  
- **Formatação:** Regex para conversão simples de marcação Markdown para HTML

---

## Estrutura do Projeto

├── app.py # Aplicação Flask
├── main.py # Lógica de processamento e respostas
├── templates/
│ └── index.html # Template HTML com Jinja2
├── static/
│ └── public/
│ └── header.png # Imagem do cabeçalho
└── README.md # Documentação do projeto
