from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}!')


async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def help_comm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi\n/time\n/help')


async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')


async def sub(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}!')


async def prod(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}!')


async def div(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}!')
