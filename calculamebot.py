import telebot

bot = telebot.TeleBot("599557504:AAE4DprZ0HUQJoBV7p7_VRvpS6Hu4WecIoY")

@bot.message_handler(commands=["start"])
def send_welcome(message):
	print(message)
	chatid = message.chat.id
	nombreUsuario = message.chat.first_name
	saludo = "Hola {nombre}, Bienvenidos al Bot de Calculos "
	bot.send_message(chatid, saludo.format(nombre=nombreUsuario))
	
@bot.message_handler(commands=["help"])
def send_welcome(message):
	print(message)
	chatid = message.chat.id
	nombreUsuario = message.chat.first_name
	saludo = "Hola {nombre}, Para hacer algun tipo de operacion escribeme un mensaje con tu operación Ejemplo 2+2"
	bot.send_message(chatid, saludo.format(nombre=nombreUsuario))
	
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	chatid = message.chat.id
	calculo = message.text
	try: 
		resultado = eval(calculo)
		respeusta = "El resultado es {calc}"
		bot.send_message(chatid, respeusta.format(calc=resultado))
		#bot.send_message(chatid, eval(calculo))
	except ZeroDivisionError:
		bot.send_message(chatid, "No se puede realizar la operación por error de division entre 0")
	except NameError:
		bot.send_message(chatid, "Se ingresaron Datos no numericos, No Se puede Relizar ningun tipo de operación")
	
print("el bot corre")
bot.polling()