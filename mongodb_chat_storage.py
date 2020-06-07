from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot(
    "Chatbot Backed by MongoDB",
    storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
    database_uri="mongodb://127.0.0.1:27017/wow_data",
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ]
    )

#chatbot.set_trainer(ListTrainer)

print('Chatbot Started:')

while True:
    try:
 #       print(" -> You:")
        user_input = input()
        bot_response = chatbot.get_response( user_input )
        print( bot_response )

    except (KeyboardInterrupt, EOFError, SystemExit):
        break

