from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN = "7659447937:AAH8gmXQey4UjmpLv4lQEuFabXHnB2SKLDw"
OWNER_ID = 8378435704  # paste your user id here

async def forward_to_owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.forward(chat_id=OWNER_ID)
    await update.message.reply_text("Your message has been sent ✅")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, forward_to_owner))
    app.run_polling()

if __name__ == "__main__":
    main()
  
