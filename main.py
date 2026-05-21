import logging
import random
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8929311013:AAHMsBZ_qC4EHvsYAd_WN0hUps95Moh5IJI"

OSK_TEMPLATES = [
    "{} кончил в аппарат жизнеобеспечения твоей матери, она сдохла, сын передозированной шлюхи",
    "{} жиробас ебаный, твоя сестра сосёт санитару в морге, уёбок венозный",
    "{} выебал трахеостому твоего отца, вся твоя семья гнойная куча в реанимации",
    "{} свиноблядский сын бляди, я кончил на могилу твоей бабки, мразь родовая",
    "{} твоя мать сдохла от передоза пока ты нюхал клей, сын нарковыбляди"
]

LONG_TEMPLATES = [
    "{} гнойный выкидыш из утробы героиновой шлюхи, я кончил в аппарат жизнеобеспечения всей твоей семьи, они сдохли, а ты их позор",
    "{} ты жиробас ебаный вегетативный сынок залупенской впадины размером с черную дыру, кончившей в мать твою передозированную, сын шлюхи",
    "{} еблище твоей матери, я отключил твою сестру от капельницы пока она сосала у реаниматолога, свиноблядский выродок"
]

def check_length(text, min_len, max_len, target_name):
    words = text.split()
    if len(words) < min_len:
        filler = f" бля {target_name} сука гнойный"
        text += filler
        return check_length(text, min_len, max_len, target_name)
    if len(words) > max_len:
        words = words[:max_len]
        text = " ".join(words)
    return text

async def osk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Напиши цель: /osk Антон")
        return
    target = " ".join(context.args)
    template = random.choice(OSK_TEMPLATES)
    result = template.format(target)
    result = check_length(result, 12, 18, target)
    await update.message.reply_text(result)

async def long(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Напиши цель: /long Антон")
        return
    target = " ".join(context.args)
    template = random.choice(LONG_TEMPLATES)
    result = template.format(target)
    result = check_length(result, 19, 25, target)
    await update.message.reply_text(result)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот готов. Команды: /osk имя, /long имя")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("osk", osk))
    app.add_handler(CommandHandler("long", long))
    print("Бот запущен")
    app.run_polling()

if __name__ == "__main__":
    main()    if not context.args:
        await update.message.reply_text("Напиши цель: /osk Антон")
        return
    target = " ".join(context.args)
    template = random.choice(OSK_TEMPLATES)
    result = template.format(target)
    result = check_length(result, 12, 18, target)
    await update.message.reply_text(result)

async def long(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Напиши цель: /long Антон")
        return
    target = " ".join(context.args)
    template = random.choice(LONG_TEMPLATES)
    result = template.format(target)
    result = check_length(result, 19, 25, target)
    await update.message.reply_text(result)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот готов. Команды: /osk имя, /long имя")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("osk", osk))
    app.add_handler(CommandHandler("long", long))
    print("Бот запущен")
    app.run_polling()

if __name__ == "__main__":
    main()    template = random.choice(OSK_TEMPLATES)
    result = template.format(target)
    result = check_length(result, 12, 18, target)
    await update.message.reply_text(result)

async def long(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Напиши цель: /long Антон")
        return
    target = " ".join(context.args)
    template = random.choice(LONG_TEMPLATES)
    result = template.format(target)
    result = check_length(result, 19, 25, target)
    await update.message.reply_text(result)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот готов. Команды: /osk имя, /long имя")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("osk", osk))
    app.add_handler(CommandHandler("long", long))
    print("Бот запущен")
    app.run_polling()

if __name__ == "__main__":
    main()
