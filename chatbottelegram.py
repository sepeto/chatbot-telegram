import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Bienvenido CriptoInversor! Te gustaría invertir, aprender sobre criptos, o aprender sobre plataformas avanzadas.')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Navega a traves del Menu 1: Como comprar/vebder Bitcoins- 2: Recomendacinoes básicas de seguridad-  '
    '3: Plataformas de inversion- 4:Crear SmartContracts- 5:Recibir soporte en conferencia por Zoom')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def invertir(update: Update, context : CallbackContext) -> None:
    if(update.message.text.upper().find("INVERTIR")>0):
        update.message.reply_text("Permiteme enseñarte a invertir. Navega a traves del Menu 1: Como comprar/vebder Bitcoins- 2: Recomendacinoes básicas de seguridad- " 
        "3: Plataformas de inversion- 4:Crear SmartContracts- 5:Recibir soporte en conferencia por Zoom")
    elif(update.message.text.upper().find("PRECIO")>0):
        update.message.reply_text("El precio del Bitcoin es de 15.884€")
    elif(update.message.text.upper().find("PRECIO")>0):
        update.message.reply_text("El precio del Bitcoin es de 15.884€")
    elif(update.message.text.upper().find("1")>0):
        update.message.reply_text('Si quieres aprender a comprar y vender bitcoins hay diferentes maneras: '
        '-La mas rapida:registrarte en 2Gether y comprar con tarjeta desde el movil, '
        '-La manera más económica y segura: comprar a traves de Kraken o Binance desde el ordenador por transferencia'    
        '-La otra manera es contactar con nosotros y te asesoremos para comprar en efectivo, tarjeta y o transferencia'
        'Para cualquier de las formas tenemos tutoriales que te ayudarán')

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1253765688:AAGYAKPS7nu9ChQO4KmlGwbE__hTjcjktnk", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text, invertir))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()




if __name__ == '__main__':
    main()
