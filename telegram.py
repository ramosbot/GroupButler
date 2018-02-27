import telepot
from Chatbot import Chatbot

telegram = telepot.Bot("471702748:AAFd0dXOp5dPLrzJkCENNfh-ejvuNI4XC48")
bot = Chatbot("luz")
def recebendoMsg(msg):
    frase = bot.escuta(frase=msg["text"])
    resp = bot.pensa(frase)
    bot.fala(resp)
    #chatID = msg["chat"]["id"]
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID,resp)

telegram.message_loop(recebendoMsg)

while True:
    pass