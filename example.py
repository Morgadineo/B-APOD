import os
import discord
import requests
from dotenv import load_dotenv
from discord.ext import commands

# 1. Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém as chaves salvas no .env
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
NASA_API_KEY = os.getenv("NASA_API_KEY")

# 2. Configura os privilégios (Intents) do Bot
intents = discord.Intents.default()
intents.message_content = True  # Necessário para ler o conteúdo das mensagens e comandos

# 3. Inicializa o cliente do Bot com o prefixo de comandos desejado
bot = commands.Bot(command_prefix="!", intents=intents)


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


# 4. Inicia a execução do bot usando o Token do Discord
if __name__ == "__main__":
    if not DISCORD_TOKEN:
        print("❌ ERRO: DISCORD_TOKEN não foi encontrado no arquivo .env!")
    else:
        bot.run(DISCORD_TOKEN)
