from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random

TOKEN = "PASTE_YOUR_TOKEN_HERE"

episodes = [
    "🟣 Episode 1: The Bazaar Awakens...",
    "💳 Episode 2: Value Streams...",
    "🚗 Episode 3: Speed Layer..."
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bazaar Bargain YEG is live.")

async def episode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(episodes))

async def ad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = " ".join(context.args)
    await update.message.reply_text(f"🎬 AD: {topic}")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("episode", episode))
app.add_handler(CommandHandler("ad", ad))

app.run_polling()
