from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080', 
			'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}
			}

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, handlers=[logging.FileHandler('bot.log', 'w', 'utf-8')])


def greet_user(bot, update): # принимает 2 параметра. bot- экземпляр бота
	text = 'Вызван /start' # которому отдаем команды. update - сообщение Телеграмм
	print(text)
	update.message.reply_text(text) # ответ пользователю


def talk_to_me(bot, update):
	user_text = "Привет {}! Ты написал {}".format(update.message.chat.first_name, update.message.text) #то что написал пользователь
	print(update.message) # печатаю в консоль
	logging.info("User: %s, Chat id: %s, Message %s", update.message.chat.first_name, 
					update.message.chat.id, update.message.text)
	update.message.reply_text(user_text) # отправляет пользователю то, что он нам прислал

def main(): # объявление функции
	mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
	
	logging.info('Бот запускается')

	dp = mybot.dispatcher
	mybot.dispatcher.add_handler(CommandHandler('start', greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me)) # применяем фильтры(реакция на текстовые сообщения, и название функции)


	mybot.start_polling() # начни проверять наличие сообщение
	mybot.idle() # будет работать пока мы его принудительно не остановим


main() # вызов функции