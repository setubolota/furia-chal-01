##################################################
##                                              ##
##   BOT CONVERSACIONAL - MENTORIA FURIA TECH   ##
##                                              ##
##                                              ##
##    by Gabriel Setubal - Gabriel Moraes       ##
##         @setubola          @                 ##
##                                              ##
##################################################

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os
from liquidpediaRequest import LiquipediaClient

load_dotenv()

TOKEN = os.getenv("PASSKEY")

#   FUNÇÕES DOS COMANDOS INTERATIVOS
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Mensagem inicial do BOT
    await update.message.reply_text(
        "Falaaa Furiosx! Esperamos que esteja tudo bem! Para se comunicar digite ou clique nos comandos para interagir\n"
        "/proximosjogos - Próximos jogos da FURIA\n"
        "/estatisticas - Estatísticas do time\n"
        "/redes - Informe-se em nossas redes sociais!"
    )

async def proximos_jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Os próximos jogos da nossa line serão:\n"
    )
    #REQ - API Gateway

async def estatisticas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #fazer o request do S3 e retornar com as infos colhidas
    await update.message.reply_text(
        "Essas são as últimas estatísticas do nosso time de CS2\n"
    )
    #REQ - API Gateway

async def resultados(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Partidas passadas:\n"
    )
    #REQ - API Gateway

async def redes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Nós estamos em todas as redes sociais\n"
        "Instagram: @furiagg\n"
        "TikTok: @furiagg\n"
        "Twitter: @FURIA\n"
        "Caso deseje adquirir algum manto oficial, acesse o link abaixo: https://www.furia.gg"
    )

def main():
    try:
        # Inicializando o bot
        application = Application.builder().token(TOKEN).build()

        # Adiciona os comandos interativos do BOT
        application.add_handler(CommandHandler("start" , start))
        application.add_handler(CommandHandler("proximosjogos" , proximos_jogos))
        application.add_handler(CommandHandler("estatisticas" , estatisticas))
        application.add_handler(CommandHandler("resultados" , resultados))
        application.add_handler(CommandHandler("redes" , redes))
        
        # Inicia o polling
        print("Bot iniciado com sucesso!")
        application.run_polling()

    except Exception as e:
        print(f"Erro ao iniciar o bot: {e}")

#Execução do código
if __name__ == "__main__":
    main()
