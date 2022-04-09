import telebot
from telebot import types
TOKEN = "5212514116:AAE6MoOvow9sLfsanaON8gdtWuES3VOr0zs"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('🖥 Личный Кабинет')
    item2 = types.KeyboardButton('📊 Инвестировать')
    item3 = types.KeyboardButton('📚 О боте')
    item4 = types.KeyboardButton('👥 Партнерка')

    markup.add(item2, item1)
    markup.add(item4, item3)
    bot.send_message(message.chat.id, '*🙋‍♂‍Привет*, *{0.first_name}*!'.format(message.from_user), reply_markup=markup, parse_mode='Markdown')


inline_about = types.InlineKeyboardMarkup()
admin_link = types.InlineKeyboardButton(text="👤 Администратор", url="https://t.me/olsed")
code_link = types.InlineKeyboardButton(text="👨‍💻 Заказать бота", url="https://t.me/olsed")
tg_link = types.InlineKeyboardButton(text="💶 Канал с выплатами", url="https://t.me/+UtnUU3cMd8djNTNi")
tgchat_link = types.InlineKeyboardButton(text="✉ Наш чат", url="https://t.me/+yF4n1h-Jec5mYzZi")
inline_about.row(admin_link, code_link)
inline_about.row(tg_link, tgchat_link)


inlineinvest = types.InlineKeyboardMarkup()
fast = types.InlineKeyboardButton(text="⚡ Покупка Комплектов", callback_data="fast")
inlineinvest.row(fast)

time_invest = types.InlineKeyboardMarkup()
two = types.InlineKeyboardButton(text="⌛ Комплект на  -  7 дней", callback_data="two")
four = types.InlineKeyboardButton(text="⌛ Комплект на  -  21 день", callback_data="four")
five = types.InlineKeyboardButton(text="⌛ Комплект на  -  30 дней", callback_data="five")
time_invest.row(two)
time_invest.row(four)
time_invest.row(five)

profile = types.InlineKeyboardMarkup()
dep = types.InlineKeyboardButton(text="💳 Пополнить баланс", callback_data="dep")
withd = types.InlineKeyboardButton(text="💸 Вывести средства", callback_data="withd")
profile.row(dep, withd)

platejka = types.InlineKeyboardMarkup()
qiwi = types.InlineKeyboardButton(text="🥝 QIWI", callback_data="qiwi")
payeer = types.InlineKeyboardButton(text="🅿 PAYEER", callback_data="payeer")
platejka.row(qiwi, payeer)

platejkaw = types.InlineKeyboardMarkup()
qiwiw = types.InlineKeyboardButton(text="🥝 QIWI", callback_data="qiwiw")
payeerw = types.InlineKeyboardButton(text="🅿 PAYEER", callback_data="payeerw")
platejkaw.row(qiwiw, payeerw)

yes_oplata = types.InlineKeyboardMarkup()
yesoplata = types.InlineKeyboardButton(text="✅ Я оплатил!", callback_data="yesoplat")
yes_oplata.row(yesoplata)

buy = types.InlineKeyboardMarkup()
buyk = types.InlineKeyboardButton(text="🛒 Купить комплект за 50₽", callback_data="buyk")
buy.row(buyk)
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'fast':
              bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='☝ *Выберите действие:*', reply_markup=time_invest, parse_mode="Markdown")
        elif call.data == 'dep':
              bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='💸 *Выберите способ для пополнения:*', reply_markup=platejka, parse_mode="Markdown")
        elif call.data == 'buyk':
              bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='🚫 *На вашем счету недостаточно средств, пополните баланс*', reply_markup=profile, parse_mode="Markdown")
        elif call.data == 'two':
              bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='⌛️ *Доход в день: 14.28\n\n⌛️ Доход всего: 100.32₽  / 200%\n\n🛒 Куплено: 0 шт*', reply_markup=buy, parse_mode="Markdown")
        elif call.data == 'four':
              bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='⌛️ *Доход в день: 19.05\n\n⌛️ Доход всего: 300.05₽  / 300%\n\n🛒 Куплено: 0 шт*', reply_markup=buy, parse_mode="Markdown")
        elif call.data == 'five':
              bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='*⌛️ Доход в день: 21.66\n\n⌛️ Доход всего: 609.17₽  / 400%\n\n🛒 Куплено: 0 шт*', reply_markup=buy, parse_mode="Markdown")
        elif call.data == 'withd':
              bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='💸 *Выберите способ для вывода средств:*', reply_markup=platejkaw, parse_mode="Markdown")
        elif call.data == 'yesoplat':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='*🔍 Оплата не найдена, попробуйте еще раз!*', parse_mode="Markdown")
        elif call.data == 'payeer':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='*💰 Пополнение баланса:\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n🔹 Переведите деньги на указанный Payeer кошелёк.\n➖➖➖➖➖➖➖➖➖➖➖➖\n🅿️ Payeer: P1068235794\n\n✏️ Комментарий к платежу: ML6221\n➖➖➖➖➖➖➖➖➖➖➖\n🔎 Деньги автоматически пополнятся вам в течении 1 минуты.*', reply_markup=yes_oplata, parse_mode="Markdown")
        elif call.data == 'qiwi':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='*💰 Пополнение баланса:\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n🔹 Переведите деньги на указанный Qiwi кошелёк.\n➖➖➖➖➖➖➖➖➖➖➖➖\n 🥝 Qiwi: +79382042773\n\n✏️ Комментарий к платежу: ML6221\n➖➖➖➖➖➖➖➖➖➖➖\n🔎 Деньги автоматически пополнятся вам в течении 1 минуты.*', reply_markup=yes_oplata, parse_mode="Markdown")
        elif call.data == 'payeerw':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='*🚫 Минимальная сумма для вывода средств: 10₽*', parse_mode="Markdown")
        elif call.data == 'qiwiw':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='*🚫 Минимальная сумма для вывода средств: 10₽*', parse_mode="Markdown")
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '🖥 Личный Кабинет':
            bot.send_message(message.chat.id, '*👤 Имя: '+str(message.chat.username)+'\n🆔 ID: '+str(message.chat.id)+'\n➖➖➖➖➖➖➖➖➖➖➖➖\n👤 Партнеров приглашено: 0\n➖➖➖➖➖➖➖➖➖➖➖➖\n💰 Ваш баланс: 0.00₽\n➖➖➖➖➖➖➖➖➖➖➖➖\n📥 Пополнения: 0.00₽ \n📤 Выплаты: 0.00₽*', reply_markup=profile, parse_mode="Markdown")
        elif message.text == '📊 Инвестировать':
              bot.send_message(message.chat.id, '☝ *Выберите действие:*', reply_markup=inlineinvest, parse_mode="Markdown")
        elif message.text == '👥 Партнерка':
              bot.send_message(message.chat.id, '*🤝 Партнёрская программа:\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n🔑 Вы получаете:\n▫️ 15% на баланс с пополнений ваших рефералов\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n🔗 Ваша реферальная ссылка: https://t.me/MoneyXRobot?start='+str(message.chat.id)+'\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n🎊 Вы уже пригласили: 0*', parse_mode="Markdown")
        elif message.text == '📚 О боте':
              bot.send_message(message.chat.id, '*📊 Статистика:\n\n👨‍💻 Пользователей: 687\n👨‍💻 Пользователей сегодня: 18\n📥 Инвестировано: 4317₽\n📤 Выплачено: 3925₽*', reply_markup=inline_about, parse_mode="Markdown")
bot.polling(none_stop = True)