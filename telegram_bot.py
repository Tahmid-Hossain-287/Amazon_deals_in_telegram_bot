import telegram

bot = telegram.Bot(token="")
group_1_id = 

updates = bot.get_updates()
print(len(updates))
print((updates[-1]))

# bot.send_message(text= "It is working!", chat_id=group_1_id)

