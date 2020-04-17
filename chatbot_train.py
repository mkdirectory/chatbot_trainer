from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot=Chatbot('Bot')
bot.set_trainer(ListTrainer)

for file in os.listdir('C:\Users\f2017114011\Downloads\Disease-Prediction')
      data= open('')
      bot.train(data)

while true:

           message= input('You:')
           if message.strip()!='Bye':
                reply= bot.get_response(messeage)
                print('ChatBot :', reply)
           if message.strip() == 'Bye':
                print('ChatBot: Bye')
                break

