from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os



bot = ChatBot('trialBot')

bot.set_trainer(ListTrainer)

#directory containing training text files
mainDir = 'C:\\chatterbot\\wow_data\\'

for _file in os .listdir(mainDir):
    chats = open(mainDir + _file, 'r').readlines()
    bot.train(chats)


while True:
    request = raw_input('You: ')
    response = bot.get_response(request)

    print('Bot: ' + str(response))
