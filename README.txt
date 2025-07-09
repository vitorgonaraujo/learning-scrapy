
🕷️ Web Crawler com Scrapy

Este é um projeto simples de crawler feito em Python usando o Scrapy.
Criei para me desafiar a entender na prática como o Scrapy funciona.

📌 Tecnologias usadas
- Python
- Scrapy
- Pipenv (para gerenciar o ambiente virtual e as dependências)

🚀 Como rodar
1. Clone o repositório:
   git clone https://github.com/vitorgonaraujo/learning-scrapy.git
   cd seu-repo

2. Instale o Pipenv (se ainda não tiver):
   pip install pipenv

3. Instale as dependências:
   pipenv install

4. Ative o ambiente virtual:
   pipenv shell

5. Execute o crawler:
   scrapy crawl bookspider

⚙️ O que faz
- Acessa o site "https://books.toscrape.com"
- Coleta imagem, título, preço e etc.
- Salva os dados em um arquivo chamado booksdata.json

📚 Objetivo
Projeto feito para aprender os fundamentos do Scrapy e praticar Python.
