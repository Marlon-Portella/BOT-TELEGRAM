from telegram.ext import *
import constants,responses

def start_command(updtade,context):
  updtade.massage.replay_text(f"Olá {update.massage.frem_user['first_name']}Sejá bem  vindo")

def help_command(update,context):
  update.massage.replay_text("oi ou olá")

def handle_massage(update,context):
  txt = str(update.massge.text).lower()
  response = responses.sample_responses(txt)

  update.massage.replay_text(response)

def error(update, context):
  print(f"Update: {update}cased error: {context.error}")

def main():
  updater = updater(constants.API_KEY, use_context=True)
  dp = updater.dispatcher

  dp.add_handler(CommandHandler("star", start_command))

