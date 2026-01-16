import telebot
from telebot import types
token = "8047220972:AAHyKszlmpuxwUq1bBkvH27RhW4FHyEd4bo"
mybot = telebot.TeleBot(token)
@mybot.message_handler(["start"])
def start(message):
    text1 = """Добро пожаловать, это бот для заказа пиццы.
        Чтобы посмотреть меню используйте команду /menu,
        чтобы увидеть свою историю заказов используйте /profile."""
    mybot.send_message( text = text1, chat_id = message.chat.id)

@mybot.message_handler(["menu"])
def menu(message):
    text2 = "Меню:"
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text = "Пепперони", callback_data= "pizza1")
    button2 = types.InlineKeyboardButton(text = "Сырная", callback_data= "pizza2")
    button3 = types.InlineKeyboardButton(text = "Гавайская", callback_data= "pizza3")
    keyboard.add(button1, button2, button3)
    mybot.send_message(text = text2, chat_id = message.chat.id, reply_markup= keyboard)

@mybot.callback_query_handler(func = lambda call: call.data == "pizza1")
def pepperoni(call):
    text3 = "Классическая пепперони, ничего лишнего: сыр, томаты и пепперони"
    keyboard = types.InlineKeyboardMarkup()
    button_order = types.InlineKeyboardButton(text = "Заказать", callback_data= "order_pizza1")
    button_back_menu = types.InlineKeyboardButton(text = "Назад в меню", callback_data= "backmenu")
    keyboard.add(button_order, button_back_menu)
    mybot.edit_message_text(text = text3, chat_id = call.message.chat.id, reply_markup = keyboard,message_id= call.message.message_id)

@mybot.callback_query_handler(func = lambda call: call.data == "pizza2")
def cheesy(call):
    text6 = "Сууупер сырная пицца, ну вот прям очень"
    keyboard = types.InlineKeyboardMarkup()
    button_order = types.InlineKeyboardButton(text = "Заказать", callback_data= "order_pizza2")
    button_back_menu = types.InlineKeyboardButton(text = "Назад в меню", callback_data= "backmenu")
    keyboard.add(button_order, button_back_menu)
    mybot.edit_message_text(text = text6, chat_id = call.message.chat.id, reply_markup = keyboard,message_id= call.message.message_id)

@mybot.callback_query_handler(func = lambda call: call.data == "pizza3")
def hawaian(call):
    text7 = "Сыр, ветчина и ананасы, да простят нас итальянцы"
    keyboard = types.InlineKeyboardMarkup()
    button_order = types.InlineKeyboardButton(text = "Заказать", callback_data= "order_pizza3")
    button_back_menu = types.InlineKeyboardButton(text = "Назад в меню", callback_data= "backmenu")
    keyboard.add(button_order, button_back_menu)
    mybot.edit_message_text(text = text7, chat_id = call.message.chat.id, reply_markup = keyboard,message_id= call.message.message_id)

@mybot.callback_query_handler(func = lambda call: call.data.startswith("order_"))
def ordering(call):
    pizza_type = call.data[6:]
    if pizza_type == "pizza1":
        pt = "Пепперони"
    elif pizza_type == "pizza2":
        pt = "Сырную"
    else:
        pt = "Гавайскую"
    text8 = f"""Вы выбрали {pt}.
      Теперь выберете размер:"""
    keyboard = types.InlineKeyboardMarkup()
    button_s1 = types.InlineKeyboardButton(text = "Маленькая", callback_data= "small_pizza")
    button_s2 = types.InlineKeyboardButton(text = "Cредняя", callback_data= "mid_pizza")
    button_s3 = types.InlineKeyboardButton(text = "Большая", callback_data= "large_pizza")
    keyboard.add(button_s1, button_s2, button_s3)
    mybot.edit_message_text(text=text8, chat_id = call.message.chat.id, reply_markup = keyboard,message_id= call.message.message_id)

@mybot.callback_query_handler(func = lambda call:call.data == "small_pizza")
def small_pizza_ord(call):
    text_ordering = "Введите ваш адрес доставки"
    mybot.send_message(text = text_ordering, chat = call.message.chat.id)
    
    

@mybot.callback_query_handler(func = lambda call: call.data == "backmenu")
def backmenu(call):
    menu(call.message)
    mybot.delete_message(call.message.chat.id, call.message.message_id)

    
mybot.infinity_polling()

