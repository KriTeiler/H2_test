#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import asyncio

from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv
import os

load_dotenv()
bot = AsyncTeleBot (os.getenv('TOKEN'))


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Привет, мы оба знаем зачем ты здесь.'
    await bot.reply_to(message, text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)

if __name__ == '__main__':
    asyncio.run(bot.polling())