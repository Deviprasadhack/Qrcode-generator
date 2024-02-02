import requests
import telebot

bot = telebot.TeleBot('6121118235:AAGdNmeJapt2o0iRJTvsRz56zx6uNIdKXOQ')

@bot.message_handler(commands=['start']) 
def send_welcome(message):
  bot.reply_to(message, "Welcome!")

# Set webhook
url = f"https://api.telegram.org/bot{bot.token}/setWebhook"
data = {'url': 'https://github.com/Deviprasadhack/Qrcode-generator'}
requests.post(url, data=data)

@bot.message_handler(commands=['generate_qr'])  
def generate_qr(message):

  text = message.text.split(' ', 1)[1]
  
  api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={text}"  

  response = requests.get(api_url)
  qr_image = response.content
  
  bot.send_photo(message.chat.id, qr_image)


  #Call API to read QR code
  #Send result to user  

  bot.polling()
