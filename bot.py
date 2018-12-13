from telegram.ext import CommandHandler, Updater, ConversationHandler, MessageHandler, Filters
import sqlite3

class Bot:
    def __init__(self, token, chat_id, db=None):
        self.updater = Updater(token) # creating updater with class patameter (because I don't want to display Bojnurd-lug-Bot token in my GitHub!)
        dispatcher = self.updater.dispatcher
        self.chat_id = chat_id

        dispatcher.add_handler(CommandHandler('start', self.start_handler))
        dispatcher.add_handler(MessageHandler(Filters.all, self.message_handling))

    def start_handler(self, bot, update):
        pass

    def message_handling(self, bot, update):
        if update.message.new_chat_members:
            if update.message.new_chat_members[0].is_bot: # delete the bots which joined(added) to group
                bot.kickChatMember(self.chat_id, update.message.new_chat_members[0].id)
                bot.deleteMessage(self.chat_id, update.message.message_id) # delete join message
                bot.deleteMessage(self.chat_id, update.message.message_id+1) # delete (bot deleted ...) message

    def run(self):
        self.updater.start_polling()
        self.updater.idle()