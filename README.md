# 🌌 NASA B-APOD - Bot do Discord usando API do APOD em Python

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![NASA API](https://img.shields.io/badge/NASA%20API-APOD-red?style=for-the-badge&logo=nasa&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Projeto desenvolvido como parte da preparação dos alunos para o **NASA Space Apps Challenge**. O objetivo desta aplicação é consumir a API oficial da NASA **APOD (Astronomy Picture of the Day)** para buscar a Foto Astronômica do Dia e exibi-la via linha de comando (terminal) ou em um Bot do Discord.

---

## 📌 Sobre o Projetos

A NASA disponibiliza diariamente uma imagem ou vídeo astronômico acompanhado de uma explicação técnica escrita por astrônomos profissionais. Esta aplicação conecta-se aos servidores da NASA, processa a resposta em **JSON** e apresenta os dados de forma estruturada.

### 🚀 Funcionalidades
- [x] Requisição HTTP autenticada à API da NASA (`api.nasa.gov`)
- [x] Extração de título, data, descrição e link de mídia (imagem/vídeo)
- [x] Execução simples via terminal (CLI)
- [ ] *[Desafio do Aluno]* Integração completa com Bot do Discord (`discord.py`)
- [ ] *[Desafio do Aluno]* Busca de fotos em datas históricas personalizadas

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Módulos Principais:**
  - `requests` (para chamadas à API REST)
  - `python-dotenv` (gerenciamento de chaves de API seguras)
  - `discord-py` *(opcional para versão Bot)*

---

## 💻 Como criar a sua versão:

### 1. Faça o Fork e Clone do Repositório
Clique no botão **Fork** no canto superior direito deste repositório e, em seguida, clone o seu repositório 'forkado'.

### 2. Configure o Ambiente Virtual (Escolha um dos métodos abaixo)

🎨 Método 1: Direto pelo Visual Studio Code (Recomendado para a Aula)

  * Abra a pasta do projeto no VS Code (File > Open Folder...).
  * Abra a Paleta de Comandos usando o atalho:
    * Windows/Linux: Ctrl + Shift + P
    * macOS: Cmd + Shift + P
  * Digite e selecione: Python: Create Environment... (ou Python: Criar ambiente...).
  * Selecione a opção Venv.
  * Escolha o nome do ambiente: .venv ou venv são os mais utilizados.
  * Escolha o interpretador Python instalado no seu computador.
  * Pesquisar pacotes PyPi:
    * discord-py
    * requests
    * python-dotenv
  * Abra um novo terminal integrado no VS Code (Ctrl + ' ou Terminal > New Terminal) ou execute um arquivo .py qualquer através do icone ▶. O ambiente virtual (.venv) já estará ativado automaticamente!

🐧 Método 2: Terminal Manual no Linux

  ##### 1. Criar o ambiente virtual
  `python3 -m venv venv`
  
  ##### 2. Ativar o ambiente virtual
  `source venv/bin/activate`
  
  ##### 3. Instalar as dependências
  `pip install discord-py requests python-dotenv`

🪟 Método 3: Terminal Manual no Windows
  ##### 1. Criar o ambiente virtual
  `python -m venv venv`

  ##### 2. Ativar o ambiente virtual (Prompt de Comando - CMD)
  `venv\Scripts\activate`

  Ou ativar via PowerShell:
  `.\venv\Scripts\Activate.ps1`

  ##### 3. Instalar as dependências
  `pip install discord-py requests python-dotenv`

### 3. Configure as Variáveis de Ambiente

Utilize o arquivo chamado .env na raiz do projeto (no mesmo nível do main.py) e adicione as suas chaves nos templates:

NASA_API_KEY=SUA_CHAVE_NASA_AQUI
DISCORD_TOKEN=SEU_TOKEN_DO_BOT_DISCORD

*💡 Nota: Obtenha sua chave gratuita em api.nasa.gov. Para testes rápidos, você pode usar DEMO_KEY.*

## 4. PRONTO!

Caso tenham qualquer dúvida, estou sempre a disposição!

