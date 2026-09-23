# ================================================================= #
# -- Código Completo --
# ---------------------
# Só abra este arquivo caso já tenha implementado seu próprio Bot.
#
# Utilize o arquivo example.py como base.
# 
# Se abrir, terá spoiler de como resolver e não valerá o exercício.
# ================================================================= #

import os
import time
import discord
import requests
from dotenv import load_dotenv
from discord.ext import commands

# 1. Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém as chaves salvas no .env
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
NASA_API_KEY = os.getenv("NASA_API_KEY")

APOD_BASE_URL = "https://api.nasa.gov/planetary/apod"

# 2. Configura os privilégios (Intents) do Bot
intents = discord.Intents.default()
intents.message_content = True  # Necessário para ler o conteúdo das mensagens e comandos

# 3. Inicializa o cliente do Bot com o prefixo de comandos desejado
bot = commands.Bot(command_prefix="!", intents=intents)


# =========================================================================== #
def request_apod(date="today",
             start_date=None,
             end_date="today",
             count=None):

    params = {
        "api_key": NASA_API_KEY,
    }

    if date:
        params['date'] = date

    elif count:
        params['count'] = count

    else:
        params['start_date'] = start_date
        params['end_date'] = end_date

    r = requests.get(APOD_BASE_URL, params=params)

    return r


def extract_infos(json: dict):

    if isinstance(json, dict):
        date = json.get("date", "Sem data")
        title = json.get("title", "Sem titulo")
        explanation = json.get("explanation", "Sem descrição")
        image = json.get("hdurl") or json.get("url")

        return (date, title, explanation, image)


def get_apod(date="today",
             start_date=None,
             end_date="today",
             count=None):
    r = request_apod(date, start_date, end_date, count)

    info = extract_infos(r.json())

    return info


# =========================================================================== #


# Evento: Executado quando o bot se conecta com sucesso ao Discord
@bot.event
async def on_ready():
    print(f"🤖 Bot conectado com sucesso como: {bot.user.name} (ID: {bot.user.id})")
    print(f"🔑 Chave da NASA carregada: {'Sim' if NASA_API_KEY else 'Não (verifique seu .env)'}")
    print("--------------------------------------------------")


# Comando de teste básico
@bot.command(name="ping")
async def ping(ctx):
    """Responde com pong para testar a conexão do bot."""
    await ctx.send("🏓 Pong! O bot da NASA está online.")

# =========================================================================== #

@bot.command()
async def apod_hoje(ctx):

    today = time.strftime("%Y-%m-%d")

    date, title, explanation, img = get_apod(date=today)

    await ctx.send(f"{title}\n{explanation}{img}")

# 4. Inicia a execução do bot usando o Token do Discord
if __name__ == "__main__":
    if not DISCORD_TOKEN:
        print("❌ ERRO: DISCORD_TOKEN não foi encontrado no arquivo .env!")
    else:
        bot.run(DISCORD_TOKEN)
