#импортируем телебот
import telebot
#импортируем библиотеку "типы" из модуля телебота
from telebot import types

#указываем наш токен
API_TOKEN="6415054160:AAFB7m9Nnd_oqM7TcFiST9levxg16ay0E9E"
bot = telebot.TeleBot(API_TOKEN)

#Обработка команды старт
@bot.message_handler(commands=['start'])
def  send_welcome(message):
 #Задаем переменную для стихотворения
 fairytale = (f"For nine night long,\n"
                                       f"pierced by a spear\n"
                                       f"I hung upong the Yggdrasil\n "
                                       f"None brought me bread\n"
                                       f"None gave me mead\n"
                                       f"Down to the depths I searched\n"
                                       f"Until i spied the Runes\n"
                                       f"I seized them up\n"
                                       f"And, screaming, i fell")
 #Прикрепляем наше стихотворение и изображение дерева к команде старт
 with open('venv\Yggdrasil.jpg','rb') as file:
    new_photo = file.read()
 bot.send_photo(message.from_user.id, new_photo, caption=fairytale, reply_markup=KBRD)
 #Это кнопки клавиатуры и их (текст?)
KBRD = types.InlineKeyboardMarkup(row_width=3)
btn1 = types.InlineKeyboardButton(text='Runes', callback_data = "btn1_cd")
btn2 = types.InlineKeyboardButton(text='Roll', callback_data = "btn2_cd")
KBRD.add(btn1)
KBRD.add(btn2)
#Обработка команд клавиатуры(непонятно)
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'btn1_cd':
        with open('venv\Runes.jpg', 'rb') as file:
            new_photo2 = file.read()
        bot.send_photo(call.message.chat.id, new_photo2)

        # file = open('Runes.jpg')
        # bot.send_photo(call.message.chat.id, file, 'text', reply_markup=btn1)
        # bot.send_message(call.message.chat.id, 'Выберите что вам надо', reply_markup=btn1)

    # elif call.data == 'btn_types1':
    #     file = open('photo2.jpg', 'rb')
    #     bot.send_photo(call.message.chat.id, file, 'text',
            #                reply_markup=kb2)  # Переход дальше не настроен, вы можете ссылаться на свои дальнейшие блоки или же вернуться к главному меню.
        bot.send_message(call.message.chat.id, 'Впишите номер РУНЫ из картинки выше.')



#Обработка вводимого текста
@bot.message_handler(content_types = 'text')


def message_reply(message):
    if message.text == "1":
        bot.send_message(message.chat.id, 'Феху - Скот, имущество. Руна богатства и благополучия, во всех проявлениях, руна пламени, огня созидания, и огня разрушения.')
    elif message.text == '2':
        bot.send_message(message.chat.id, 'Уруз - зубр. Неукротимая сила, неизбежные пермены. Пламя, сжигающее всё на отжившее и неестественное. Исцеление от болезни и невероятная сила слова.')
    elif message.text == '3':
        bot.send_message(message.chat.id, "Туриз - шип, молот Тора.")
    elif message.text == '4':
        bot.send_message(message.chat.id, "Ансуз - Язык Бога, Один, 'Голос Вселенной'.")
    elif message.text == '5':
        bot.send_message(message.chat.id, "Райдо - Колесо, Путешествие")
    elif message.text == '6':
        bot.send_message(message.chat.id, "Кеназ - факел")
    elif message.text == '7':
        bot.send_message(message.chat.id, "Гебо - дар, подарок.")
    elif message.text == '8':
        bot.send_message(message.chat.id, "Вунйо - радость, победа.")
    elif message.text == '9':
        bot.send_message(message.chat.id, "")
if __name__ == '__main__':
    # schedule.every().day.at('22:11').do(send_message)
    # Thread(target=schedule_checker).start()
    bot.polling(none_stop=True)

