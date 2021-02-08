import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def mainCommandHandler(incoming_message, telebot_instance):
    """Echo the user message."""
    chat_id = incoming_message.chat.id
    msg_id = incoming_message.message_id
    user = incoming_message.from_user 
    try:
        print(incoming_message.text)
        text = incoming_message.text.encode('utf-8').decode()
    except:
        print("no text in the message")
    try:
        info = "got text message: " + text + " from " + user.username
        print(info)
    except:
        print("no message is received")

    try:
        telebot_instance.sendMessage(chat_id=chat_id, text="Hello I am goose", reply_to_message_id=msg_id)
    except:
        print("message is lost, bot has no target to reply")

    return 

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('your mother fat!')

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)