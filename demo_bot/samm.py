from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import web

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


db = web.database(
    dbn = 'mysql', 
    host = 'localhost', 
    db = 'samm_db', 
    user = 'samm', 
    pw = 'samm.2019',
    port= 3306)

#Samm17_bot 
token = '842675543:AAHwX8-0n7rH6-n4p8-WDUBarXExajUBtsI'

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    try:
        username = update.message.from_user.username
        update.message.reply_text('Hola {} usa estos comandos:\n/producto sku'.format(username))
    except Exception as e:
        print "Error start():",e.args

def help(bot, update):
    try:
        username = update.message.from_user.username
        update.message.reply_text('Hola {}\n/producto sku'.format(username))
    except Exception as e:
        print "Error help():",e.args

def producto(bot, update):
    try:
        text = update.message.text.split()
        username = update.message.from_user.username
    
        sku = text[1]
        print "Send info to {}".format(username)
        print "sku {}".format(sku)
        result = db.select('productos', where='sku=$sku', vars=locals())[0]

        producto = str(result.producto)
        precio = str(result.precio)
        existencias = str(result.existencias)

        print "Sending Producto " + producto
        print "Sending Precio " + precio
        print "Sending Existencias " + existencias

        update.message.reply_text('Hola {}\nEste es el producto que buscas:\n{}, {}, {}'.format(username, producto, precio, existencias))
    except Exception as e:
        update.message.reply_text('Ejemplo\n/info 001')
        update.message.reply_text('El sku {} es incorreto'.format(sku))
        print "Error en info: ", e.args

def echo(bot, update):
    try:
        texto = update.message.text # almacena el texto que envio el usuario
        if texto == "hola":
            update.message.reply_text("Como estas?") # envia la respuesta
        else:
            update.message.reply_text(update.message.text) # envia el texto que recibe
        print update.message.text
        print update.message.date
        print update.message.from_user
        print update.message.from_user.username
    except Exception as e:
        print "Error echo():", e.args
    
def error(bot, update, error):
    try:
        logger.warn('Update "%s" caused error "%s"' % (update, error))
    except Exception as e:
        print "Error error():", e.args

def main():
    try:
        print 'S.A.M.M. init token'
        updater = Updater(token)

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        print 'S.A.M.M. init dispatcher'

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("producto", producto))
        

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))

        # log all errors
        dp.add_error_handler(error)

        # Start the Bot
        updater.start_polling()

        # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        print 'S.A.M.M. start'
        updater.idle()
    except Exception as e:
        print "Error en main():", e.args

if __name__ == '__main__':
    main()
