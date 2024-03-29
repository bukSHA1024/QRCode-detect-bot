import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from pyzbar.pyzbar import decode
from PIL import Image
from io import BytesIO

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer("Send me the picture containing QR code and I will decode it")


@dp.message(Command("help"))
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/help` command
    """
    await message.answer(
        "Send me the picture containing QR code and I will decode it. If you"
        " have any issues please create new issue here:"
        " https://github.com/bukSHA1024/QRCode-detect-bot"
    )


@dp.message()
async def detect_qr_code(message: types.Message) -> None:
    """
    Handler will correct text written using a wrong keyboard layout and send it back.
    """
    if message is not None and message.photo is not None:
        maxPhotoSize = max(message.photo, key=lambda photoSize: photoSize.file_size)
        photo_info = await bot.get_file(maxPhotoSize.file_id)
        photo_bytes = await bot.download_file(photo_info.file_path)
        qrcodes = decode(Image.open(photo_bytes))
        for qrcode in qrcodes:
            await message.answer("I found QR code with following content: " + qrcode.data.decode("utf-8"))

        if len(qrcodes) == 0:
            await message.answer("I didn't find anything on this picture")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
