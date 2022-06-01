from mal import AnimeSearch, MangaSearch, Anime, Manga

from telegram.ext import Updater, MessageHandler, CommandHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from echo.config import TOKEN
import random

MAL = None
STATE = None
TYPE = None
TEXT = None
ANI_SEARCH = 1
MANGA_SEARCH = 2

print('bot working')

creditors = f"AnimeSearchBot (@An1meSearchBot) - v0.1\n\n" \
            f"@bioneis\n" \


def do_keyboard(update, context, textile):
    keyboard = [
        [
            InlineKeyboardButton("Anime Search", callback_data='1'),
            InlineKeyboardButton("Manga Search", callback_data='2'),
        ],
        [
            InlineKeyboardButton("Random Anime", callback_data='6'),
            InlineKeyboardButton("Random Manga", callback_data='7'),
        ],
        [
            InlineKeyboardButton("Best Anime | Fall 2021", callback_data='8')
        ],
        [
            InlineKeyboardButton("Credits", callback_data='3')
        ],

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(textile, reply_markup=reply_markup)


def do_start(update, context):
    textile = f"Konnichiwa! Anime Search Bot welcomes you! \nAll available functions are located below\n"
    return do_keyboard(update, context, textile)


def button(update, context):
    global MAL
    query = update.callback_query

    query.answer()

    if query.data == '1':
        query.edit_message_text(text=f"Write the name of anime")
        return do_asearch(update, context)
    if query.data == '2':
        query.edit_message_text(text=f"Write the name of manga")
        return do_msearch(update, context)
    if query.data == '3':
        query.edit_message_text(text=creditors)
    if query.data == '4':
        detailed(update, context, type_=1)
    if query.data == '5':
        detailed(update, context, type_=2)
    if query.data == '6':
        return do_arand(update, context, type=1)
    if query.data == '7':
        return do_mrand(update, context, type=1)
    if query.data == '8':
        return do_release(update, context)
    if query.data == '10':
        searcher(update, context, type_=1, ID=0)
    if query.data == '11':
        searcher(update, context, type_=1, ID=1)
    if query.data == '12':
        searcher(update, context, type_=1, ID=2)
    if query.data == '13':
        searcher(update, context, type_=1, ID=3)
    if query.data == '20':
        searcher(update, context, type_=2, ID=0)
    if query.data == '21':
        searcher(update, context, type_=2, ID=1)
    if query.data == '22':
        searcher(update, context, type_=2, ID=2)
    if query.data == '23':
        searcher(update, context, type_=2, ID=3)
    if query.data == '101':
        MAL = 44961
        detailed(update, context, type_=1)
    if query.data == '102':
        MAL = 48926
        detailed(update, context, type_=1)
    if query.data == '103':
        MAL = 45576
        detailed(update, context, type_=1)
    if query.data == '104':
        MAL = 48556
        detailed(update, context, type_=1)
    if query.data == '105':
        MAL = 48483
        detailed(update, context, type_=1)
    if query.data == '106':
        MAL = 46352
        detailed(update, context, type_=1)
    if query.data == '107':
        MAL = 47790
        detailed(update, context, type_=1)
    if query.data == '108':
        MAL = 48569
        detailed(update, context, type_=1)
    if query.data == '109':
        MAL = 49926
        detailed(update, context, type_=1)
    if query.data == '110':
        MAL = 48761
        detailed(update, context, type_=1)


def do_help(update, context):
    textile = f"Available Anime Search Bot functions"
    return do_keyboard(update, context, textile)


def do_credits(update, context):
    update.message.reply_text(creditors)


def do_release(update, context):

    keyboard = [
        [InlineKeyboardButton("Platinum End", callback_data='101')],
        [InlineKeyboardButton("Komi-san wa, Comyushou desu.", callback_data='102')],
        [InlineKeyboardButton("Mushoku Tensei: Isekai Ittara Honki Dasu Part 2", callback_data='103')],
        [InlineKeyboardButton("Takt Op. Destiny", callback_data='104')],
        [InlineKeyboardButton("Mieruko-chan", callback_data='105')],
        [InlineKeyboardButton("Blue Period", callback_data='106')],
        [InlineKeyboardButton("Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru", callback_data='107')],
        [InlineKeyboardButton("86 Part 2", callback_data='108')],
        [InlineKeyboardButton("Kimetsu no Yaiba: Mugen Ressha-hen", callback_data='109')],
        [InlineKeyboardButton("Saihate no Paladin", callback_data='110')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.callback_query.edit_message_text("Best Anime | Fall 2021", reply_markup=reply_markup)


def do_asearch(update, context):
    global STATE
    global TYPE
    global TEXT
    STATE = ANI_SEARCH
    TYPE = 1
    try:
        TEXT = update.message.text
        if TEXT == "/a_search":
            raise ValueError("invalid value")
        if len(TEXT) < 3:
            update.message.reply_text(f"Name must contain at least 3 characters")
            raise ValueError("invalid value")

        search = AnimeSearch(TEXT)

        keyboard = [
            [
                InlineKeyboardButton(search.results[0].title, callback_data='10'),
                InlineKeyboardButton(search.results[1].title, callback_data='11'),
            ],
            [InlineKeyboardButton(search.results[2].title, callback_data='12'),
             InlineKeyboardButton(search.results[3].title, callback_data='13')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text("Choose one of the suggested anime", reply_markup=reply_markup)

        STATE = None
    except:
        update.message.reply_text("Write the name of anime")


def do_msearch(update, context):
    global STATE
    global TYPE
    global TEXT
    STATE = MANGA_SEARCH
    TYPE = 2
    try:
        TEXT = update.message.text
        if TEXT == "/m_search":
            raise ValueError("invalid value")
        if len(TEXT) < 3:
            update.message.reply_text(f"Name must contain at least 3 characters")
            raise ValueError("invalid value")

        search = MangaSearch(TEXT)

        keyboard = [
            [
                InlineKeyboardButton(search.results[0].title, callback_data='20'),
                InlineKeyboardButton(search.results[1].title, callback_data='21'),
            ],
            [InlineKeyboardButton(search.results[2].title, callback_data='22'),
             InlineKeyboardButton(search.results[3].title, callback_data='23')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text("Choose one of the suggested manga", reply_markup=reply_markup)

        STATE = None
    except:
        update.message.reply_text("Write the name of manga")


def do_arand(update, context, type=2):
    isCorrect = True
    if type == 1:
        update.callback_query.edit_message_text("Loading data...\n\nPlease wait just a little")
        mess = update.callback_query.edit_message_text
    else:
        must_delete = update.message.reply_text("Loading data...\n\nPlease wait just a little")
        mess = update.message.reply_text

    while isCorrect:
        try:
            ID = random.randint(1, 43000)
            print(Anime(ID).title)
            isCorrect = False
        except:
            print("error")

    mess(f"Title: {Anime(ID).title}\n"
                            f"URL: {Anime(ID).url}\n"
                            f"Type: {Anime(ID).type}\n"
                            f"Episodes: {Anime(ID).episodes}\n"
                            f"Score: {Anime(ID).score}\n"
                            f"Status: {Anime(ID).status}\n\n"
                            f"{Anime(ID).synopsis}")
    if type == 2:
        context.bot.deleteMessage(message_id=must_delete.message_id,
                                chat_id=update.message.chat_id)


def do_mrand(update, context, type=2):
    isCorrect = True
    if type == 1:
        update.callback_query.edit_message_text("Loading data...\n\nPlease wait just a little")
        mess = update.callback_query.edit_message_text
    else:
        must_delete = update.message.reply_text("Loading data...\n\nPlease wait just a little")
        mess = update.message.reply_text

    while isCorrect:
        try:
            ID = random.randint(1, 43000)
            print(Manga(ID).title)
            isCorrect = False
        except:
            print("error")

    mess(f"Title: {Manga(ID).title}\n"
        f"URL: {Manga(ID).url}\n"
        f"Type: {Manga(ID).type}\n"
        f"Episodes: {Manga(ID).volumes}\n"
        f"Score: {Manga(ID).score}\n"
        f"Status: {Manga(ID).status}\n\n"
        f"{Manga(ID).synopsis}")
    if type == 2:
        context.bot.deleteMessage(message_id=must_delete.message_id,
                                  chat_id=update.message.chat_id)


def detailed(update, context, type_):
    global MAL
    update.callback_query.edit_message_text("Loading data...\n\nPlease wait just a little")
    if type_ == 1:
        ID = Anime
        epi = ID(MAL).episodes
        pub = ID(MAL).aired
        prem = f"Premiered: {ID(MAL).premiered}\n"
        broad = f"Broadcast: {ID(MAL).broadcast}\n"
        lic = f"Licensors: {', '.join(ID(MAL).licensors)}\n"
        stud = f"Studios: {','.join(ID(MAL).studios)}\n"
        src = f"Source: {ID(MAL).source}\n"
        dur = f"Duration: {ID(MAL).duration}\n"
        rate = f"Rating: {ID(MAL).rating}\n"
    else:
        ID = Manga
        epi = ID(MAL).chapters
        pub = ID(MAL).published
        prem = ""
        broad = ""
        lic = f"Authors: {', '.join(ID(MAL).authors)}\n"
        stud = ""
        src = ""
        dur = ""
        rate = ""

    update.callback_query.edit_message_text(f"Title: {ID(MAL).title} ({ID(MAL).title_japanese})\n"
                                            f"URL: {ID(MAL).url}\n"
                                            f"Type: {ID(MAL).type}\n"
                                            f"Episodes: {epi}\n"
                                            f"Score: {ID(MAL).score}\n"
                                            f"Status: {ID(MAL).status}\n"
                                            f"Genres: {', '.join(ID(MAL).genres)}\n"
                                            f"Scored By: {ID(MAL).scored_by}\n"
                                            f"Rank: {ID(MAL).score}\n"
                                            f"Popularity: {ID(MAL).popularity}\n"
                                            f"Members: {ID(MAL).members}\n"
                                            f"Favorites: {ID(MAL).favorites}\n"
                                            f"Published: {pub}\n"
                                            f"{prem}"
                                            f"{broad}"
                                            f"{lic}"
                                            f"{stud}"
                                            f"{src}"
                                            f"{dur}"
                                            f"{rate}\n\n"
                                            f"{ID(MAL).synopsis}\n")


def searcher(update, context, type_, ID):
    global MAL
    global TEXT
    if type_ == 1:
        search = AnimeSearch(TEXT)
        epi = search.results[ID].episodes
        data = 4
    else:
        search = MangaSearch(TEXT)
        epi = search.results[ID].volumes
        data = 5

    MAL = search.results[ID].mal_id
    update.callback_query.edit_message_text("Loading data...\n\nPlease wait just a little")
    textile = (f"Title: {search.results[ID].title}\n"
             f"URL: {search.results[ID].url}\n"
             f"Type: {search.results[ID].type}\n"
             f"Episodes: {epi}\n"
             f"Score: {search.results[ID].score}\n\n"
             f"{search.results[ID].synopsis}")

    keyboard = [
        [
            InlineKeyboardButton("More Detailed", callback_data=data),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.callback_query.edit_message_text(textile, reply_markup=reply_markup)


def text(update, context):
    global STATE

    if STATE == ANI_SEARCH:
        return do_asearch(update, context)
    if STATE == MANGA_SEARCH:
        return do_msearch(update, context)


def main():
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", do_start))
    dispatcher.add_handler(CommandHandler("help", do_help))
    dispatcher.add_handler(CommandHandler("a_search", do_asearch))
    dispatcher.add_handler(CommandHandler("m_search", do_msearch))
    dispatcher.add_handler(CommandHandler("rand_anime", do_arand))
    dispatcher.add_handler(CommandHandler("rand_manga", do_mrand))
    dispatcher.add_handler(CommandHandler("credits", do_credits))
    dispatcher.add_handler(CallbackQueryHandler(button))

    dispatcher.add_handler(MessageHandler(Filters.text, text))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
