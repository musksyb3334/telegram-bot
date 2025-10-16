

# bot_store.py
# بوت بيع منتجات (حسابات + بروكسيات)
# أضف فقط التوكن تبعك في السطر رقم 8

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# 🔹 ضع التوكن تبعك هون (من BotFather)
TOKEN = "8387675825:AAEGrt-aCy7ZGf4yd1tM3Cqo95GUuLPoQ4k"

# 🔹 معرف الدعم (تم تعيينه حسب طلبك)
SUPPORT_USERNAME = "Anasweb22"

# 🔹 تعريف المنتجات
PRODUCTS = {
    "nice_12k": ("حساب Nice survey", "12,000 SYB"),
    "heypiggy_12k": ("حساب Hey piggy", "12,000 SYB"),
    "nice_repeat_25k": ("حساب Nice survey مريدم مرتين على الاقل", "25,000 SYB"),
    "surveyworld_10k": ("حساب Survey world", "10,000 SYB"),
    "us_number_3k3": ("رقم امريكي SYB", "3,300 SYB"),
}

PROXIES = {
    "proxy_2days_20": ("بروكسي يومين عائلي", "20 SYB"),
    "proxy_week_60k": ("بروكسي اسبوعي عائلي", "60,000 SYB"),
    "proxy_month_200k": ("بروكسي شهري عائلي", "200,000 SYB"),
}

# 🔹 القائمة الرئيسية
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🛒 شراء حسابات", callback_data="menu_accounts")],
        [InlineKeyboardButton("📋 الأسعار", callback_data="menu_prices")],
        [InlineKeyboardButton("🌐 شراء بروكسيات", callback_data="menu_proxies")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "أهلاً وسهلاً 👋\nاختار يلي بدك تشتريه أو شوف الأسعار 👇",
        reply_markup=reply_markup
    )

# 🔹 عرض قائمة الحسابات
def menu_accounts(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = []
    for key, (title, price) in PRODUCTS.items():
        keyboard.append([InlineKeyboardButton(f"{title} — {price}", callback_data=f"show:{key}")])
    keyboard.append([InlineKeyboardButton("🔙 رجوع", callback_data="back_to_main")])
    query.edit_message_text("اختر الحساب يلي بدك تشتريه:", reply_markup=InlineKeyboardMarkup(keyboard))

# 🔹 عرض قائمة البروكسيات
def menu_proxies(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = []
    for key, (title, price) in PROXIES.items():
        keyboard.append([InlineKeyboardButton(f"{title} — {price}", callback_data=f"showproxy:{key}")])
    keyboard.append([InlineKeyboardButton("🔙 رجوع", callback_data="back_to_main")])
    query.edit_message_text("اختر نوع البروكسي:", reply_markup=InlineKeyboardMarkup(keyboard))

# 🔹 عرض صفحة الأسعار العامة
def menu_prices(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    text = "📋 *قائمة الأسعار*:\n\n"
    for _, (title, price) in PRODUCTS.items():
        text += f"- {title} : {price}\n"
    text += "\n🌐 *بروكسيات*:\n"
    for _, (title, price) in PROXIES.items():
        text += f"- {title} : {price}\n"
    keyboard = [[InlineKeyboardButton("🔙 رجوع", callback_data="back_to_main")]]
    query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

# 🔹 عرض تفاصيل منتج (الحسابات)
def show_product(update: Update, context: CallbackContext, key: str):
    query = update.callback_query
    query.answer()
    title, price = PRODUCTS[key]
    text = f"🛍️ *{title}*\nالسعر: *{price}*\n\nلطلب هذا المنتج تواصل مع الدعم 👇"
    keyboard = [
        [InlineKeyboardButton("📞 تواصل مع الدعم", url=f"https://t.me/{SUPPORT_USERNAME}")],
        [InlineKeyboardButton("🔙 رجوع للمنتجات", callback_data="menu_accounts")]
    ]
    query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

# 🔹 عرض تفاصيل بروكسي
def show_proxy(update: Update, context: CallbackContext, key: str):
    query = update.callback_query
    query.answer()
    title, price = PROXIES[key]
    text = f"🛍️ *{title}*\nالسعر: *{price}*\n\nلطلب هذا المنتج تواصل مع الدعم 👇"
    keyboard = [
        [InlineKeyboardButton("📞 تواصل مع الدعم", url=f"https://t.me/{SUPPORT_USERNAME}")],
        [InlineKeyboardButton("🔙 رجوع للبروكسيات", callback_data="menu_proxies")]
    ]
    query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

# 🔹 التعامل مع الأزرار
def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data

    if data == "menu_accounts":
        menu_accounts(update, context)
    elif data == "menu_proxies":
        menu_proxies(update, context)
    elif data == "menu_prices":
        menu_prices(update, context)
    elif data == "back_to_main":
        query.answer()
        keyboard = [
            [InlineKeyboardButton("🛒 شراء حسابات", callback_data="menu_accounts")],
            [InlineKeyboardButton("📋 الأسعار", callback_data="menu_prices")],
            [InlineKeyboardButton("🌐 شراء بروكسيات", callback_data="menu_proxies")],
        ]
        query.edit_message_text("رجعت للقائمة الرئيسية 👇", reply_markup=InlineKeyboardMarkup(keyboard))
    elif data.startswith("show:"):
        key = data.split("show:")[1]
        show_product(update, context, key)
    elif data.startswith("showproxy:"):
        key = data.split("showproxy:")[1]
        show_proxy(update, context, key)
    else:
        query.answer("زر غير معروف 😅")

# 🔹 تشغيل البوت
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button_handler))

    print("✅ Bot started... جاهز ريس!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
