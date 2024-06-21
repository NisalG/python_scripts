from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('MyChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus data
trainer.train('chatterbot.corpus.english')

while True:
    try:
        user_input = input("You: ")
        bot_response = chatbot.get_response(user_input)
        print(f"Bot: {bot_response}")

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
