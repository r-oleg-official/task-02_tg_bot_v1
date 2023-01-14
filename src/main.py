from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


app = ApplicationBuilder().token("API Token").build()

app.add_handler(CommandHandler("hi", hi))
app.add_handler(CommandHandler("help", help_comm))
app.add_handler(CommandHandler("sum", sum))
# app.add_handler(CommandHandler("-", hi))
# app.add_handler(CommandHandler("*", hi))
# app.add_handler(CommandHandler("/", hi))


print("Server start.")
app.run_polling()
