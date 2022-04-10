import telebot
import loadImage as loadImage
import constants as constants

bot = telebot.TeleBot(constants.TOKEN)
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Greetings! I can delete watermark from your photo.\n' +  
        'Just send me photo and you will sea the results\n' )


@bot.message_handler(content_types=['photo'])
def getPhoto(message):
    try:
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'mnt/img/' + 'photo.jpeg'
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, "Clean process starts")
        try:
            loadImage.delWatermark()
            bot.send_photo(chat_id=message.chat.id, photo=open('mnt/img/photo.jpeg', 'rb'))
        except:
            bot.reply_to(message, "This photo is too high resolution for me")
        
    except Exception as e:
        bot.reply_to(message, e)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, "I am working with photo. I don't analyzing your text)")
    
bot.polling(none_stop=True, interval=0)