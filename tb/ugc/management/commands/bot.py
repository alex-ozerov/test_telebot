from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.utils.request import Request
from ugc.models import Profile
from ugc.models import Message
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
import requests
from bs4 import BeautifulSoup


def do_eth():
    DOLLAR_ETH = 'https://myfin.by/crypto-rates/ethereum-usd'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}
    full_page = requests.get(DOLLAR_ETH, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "birzha_info_head_rates"})
    print(convert[0].text)



BUTTON_BTC = 'BTC'
BUTTON_ETH = 'ETH'
BUTTON_DOGE = 'DOGE'


def get_base_reply_keyboard():
    keyboard = [
        [
            KeyboardButton(BUTTON_BTC),
            KeyboardButton(BUTTON_ETH),
            KeyboardButton(BUTTON_DOGE),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Произошла ошибка: {e}'
            print(error_message)
            raise e
    return inner


@log_errors
def do_echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text
    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.name,
            'firstname': update.message.from_user.first_name,
            'lastname': update.message.from_user.last_name,
        }
    )
    Message(
        profile=p,
        text=text,
    ).save()
    if text == BUTTON_ETH:
        return bot.message(do_eth)
    elif text == BUTTON_BTC:
        return do_btc(update=update)
    elif text == BUTTON_DOGE:
        return do_doge(update=update)
    else:
        reply_text = "Ваш запрос = {}".format(text)
    update.message.reply_text(
        text=reply_text,
        reply_markup=get_base_reply_keyboard(),
    )


class Command(BaseCommand):
    help = 'Телеграмм-бот'

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
        )
        print(bot.get_me())

        updater = Updater(
            bot=bot,
            use_context=True,
        )

        message_handler = MessageHandler(Filters.text, do_echo)
        updater.dispatcher.add_handler(message_handler)

        updater.start_polling()
        updater.idle()
