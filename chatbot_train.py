from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


def setup():
    chatbot1 = ChatBot('B08',storage_adapter='chatterbot.storage.SQLStorageAdapter',trainer='chatterbot.trainers.ListTrainer')
    for file in os.listdir( 'C:/Users/Chandrapal Panwar/Desktop/IBM watson/chatterbot-corpus-master/chatterbot_corpus/data/english/' ):
        convData = open( r'C:/Users/Chandrapal Panwar/Desktop/IBM watson/chatterbot-corpus-master/chatterbot_corpus/data/english/' + file, encoding='latin-1' ).readlines()
        chatbot1.set_trainer( ListTrainer )
        chatbot1.train( convData )
        print("Training completed")

setup()