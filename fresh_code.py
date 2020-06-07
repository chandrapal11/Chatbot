from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

bot = ChatBot('B01')
bot.set_trainer(ListTrainer)

for file in os.listdir('C:/Users/Chandrapal Panwar/Desktop/IBM watson/chatterbot-corpus-master/chatterbot_corpus/data/english/' ):
    data = open(r'C:/Users/Chandrapal Panwar/Desktop/IBM watson/chatterbot-corpus-master/chatterbot_corpus/data/english/' + file,encoding='latin-1' ).readlines()
    bot.train(data)

while True:
    message = input("you :")
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print('Chatbot :',reply)
    if message.strip() == 'Bye':
        print('Chatbot : Bye')
        break



