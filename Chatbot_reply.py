from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def get_response(usrText):
    chatbot1 = ChatBot('B08',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.'
        },
         ],

                  #database='./database.sqlite3',
    trainer='chatterbot.trainers.ListTrainer', read_only=True)
    chatbot1.set_trainer(ListTrainer)


    while True:
        if usrText.strip()!= 'Bye':
            result = chatbot1.get_response(usrText)
            reply = str(result)
            return(reply)
        if usrText.strip() == 'Bye':
            return('Bye')
            break