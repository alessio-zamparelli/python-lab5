from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler)
from telegram import (ChatAction, ReplyKeyboardMarkup, ReplyKeyboardRemove)
from os import _exit
import os
import configparser
import db_operator as myDB
from flask import Flask

import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.ERROR)

app = Flask(__name__)




@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
