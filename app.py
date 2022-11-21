import logging

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

API_TOKEN = 'Your TOKEN'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

urlkb = InlineKeyboardMarkup(row_width=5)
Support1 = InlineKeyboardButton(text='Банка монобанк', url="https://send.monobank.ua/jar/8mMNQGAPgv")
urlkb.add(Support1)

@dp.message_handler(commands=['support'])
async def send_welcome(message: types.Message):
    await message.reply("Monobank: 5375411590830803 ", reply_markup=urlkb)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm Flerovium!\nType name of animal\n U can use /support")

@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Cats are here 😺')


@dp.message_handler(regexp='(^horse[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/horse.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Horses are here 🐴')

@dp.message_handler(regexp='(^dog[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/dog.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Dogs are here 🐶')

@dp.message_handler(regexp='(^capybara[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/capy.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Capybars are here 🤽‍♂️')

@dp.message_handler(regexp='(^crocodile[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/croc.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Crocodiles are here 🐊')

@dp.message_handler(regexp='(^dolphin[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/dolp.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Dolphins are here 🐬')

@dp.message_handler(regexp='(^fox[es]?$|puss)')
async def cats(message: types.Message):
    with open('data/fox.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Foxes are here 🦊')

@dp.message_handler(regexp='(^lion[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/lion.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Lions are here 🦁')

@dp.message_handler(regexp='(^pig[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/pig.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Pigs are here 🐖')

@dp.message_handler(regexp='(^hippo[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/Hippo.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Hippos are here 🦛')

@dp.message_handler(regexp='(^salamander[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/salamander.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Salamanders are here 💆‍♂️')

@dp.message_handler(regexp='(^alpaca[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/alpaca.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Alpacas are here 💆‍♂️')


@dp.message_handler(regexp='(^fish[more]?$|puss)')
async def cats(message: types.Message):
    with open('data/fish.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Fish are here 🐟')

@dp.message_handler(regexp='(^chicken[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/chicken.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Chickens are here 🐥')


@dp.message_handler(regexp='(^cow[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cow.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Cows are here 🐄')



@dp.message_handler(regexp='(^deer[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/deer.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Deers are here 🦌')


@dp.message_handler(regexp='(^elephant[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/elephant.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Elephants are here 🐘')


@dp.message_handler(regexp='(^elk[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/elk.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Elks are here 🦌')


@dp.message_handler(regexp='(^giraffe[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/girrafe.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Giraffes are here 🦒')


@dp.message_handler(regexp='(^goat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/goat.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Goats are here 🐐')


@dp.message_handler(regexp='(^gobbler[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/gobbler.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Gobblers are here 👺')


@dp.message_handler(regexp='(^hamster[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/hamster.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Hamsters are here 🐹')


@dp.message_handler(regexp='(^hyena[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/hyena.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Hyenas are here 🐱‍💻')


@dp.message_handler(regexp='(^jaguar[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/jaguar.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Jaguars are here 🎃')


@dp.message_handler(regexp='(^leopard[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/leopard.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Leopards are here 🐆')


@dp.message_handler(regexp='(^lynx[es]?$|puss)')
async def cats(message: types.Message):
    with open('data/goat.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Lynxes are here 🔬')

@dp.message_handler(regexp='(^mare[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/mare.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Mares are here 🏃‍♀️')


@dp.message_handler(regexp='(^mongoose[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/mongoose.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Mongooses are here Ⓜ')




@dp.message_handler(regexp='(^monkey[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/monkey.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Monkeys are here 🙉')



@dp.message_handler(regexp='(^panda[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/panda.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Pandas are here 🐼')


@dp.message_handler(regexp='(^panther[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/panther.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Panthers are here 🅿')


@dp.message_handler(regexp='(^parrot[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/parrot.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Parrots are here 🦜')


@dp.message_handler(regexp='(^polar[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/goat.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Polar Bears are here 🐻')


@dp.message_handler(regexp='(^puma[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/puma.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Pumas are here ⛽')


@dp.message_handler(regexp='(^rabbit[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/rabbit.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Rabbits are here 🐇')


@dp.message_handler(regexp='(^raccon[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/raccon.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Raccons are here 🦝')



@dp.message_handler(regexp='(^ram[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/ram.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Rams are here 🐏')


@dp.message_handler(regexp='(^rhinoceros[es]?$|puss)')
async def cats(message: types.Message):
    with open('data/rhinoceros.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Rhinoceroses are here 🦏')



@dp.message_handler(regexp='(^rooster[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/rooster.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Roosters are here 🐓')


@dp.message_handler(regexp='(^salamander[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/salamander.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Salamanders are here 🥗')


@dp.message_handler(regexp='(^sheep[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/sheep.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Sheeps are here 🐏')


@dp.message_handler(regexp='(^tiger[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/tiger.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Tigers are here 🐅')


@dp.message_handler(regexp='(^tortoise[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/tortoise.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Tortoise are here 🐢')


@dp.message_handler(regexp='(^turkey[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/turkey.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Turkeys are here 🦃')


@dp.message_handler(regexp='(^wolf[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/wolf.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Wolfs are here 🐺')


@dp.message_handler(regexp='(^yak[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/yak.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Yaks are here 🚢')


@dp.message_handler(regexp='(^zebra[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/zebra.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Zebras are here 🦓')

@dp.message_handler(regexp='(^Mouse[more]?$|puss)')
async def cats(message: types.Message):
    with open('data/mouse.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Mice are here 🐭')

@dp.message_handler(regexp='(^nigger[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/nigger.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Niggers are here 🏴  ')

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    msg = await message.answer("Cant find image")






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
