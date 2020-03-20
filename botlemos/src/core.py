from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from stonks import cotar, frasear, coronar
TELEGRAM_TOKEN = "935141102:AAE5ssMgzHoQ95yV7WvO304EKKcBSRtzMdQ"
url = 'https://economia.awesomeapi.com.br/all/USD-BRL'


def hello(update, context):
    update.message.reply_text(
        'IAE {} SEU CORNO DA DESGRAÇA'.format(update.message.from_user.first_name))


def dolar(update, context):
    chat_id = update.message.chat_id
    corno = update.message.from_user.first_name
    cotar(corno)
    frase = frasear()
    update.message.reply_text(
        '{} - Rafael Lemos'.format(frase))
    context.bot.send_photo(chat_id=chat_id, photo=open('cotacao.png', 'rb'))


def corona(update, context):
    chat_id = update.message.chat_id
    corno = update.message.from_user.first_name
    coronar(corno)
    frase = frasear()
    update.message.reply_text(
        '{} - Rafael Lemos'.format(frase))
    context.bot.send_photo(chat_id=chat_id, photo=open('coronafofoelfinal.png', 'rb'))
    


def main():

    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('dolar', dolar))
    updater.dispatcher.add_handler(CommandHandler('corona', corona))

    updater.start_polling()


    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()
