import pyrogram
import os
from rembg import remove
import io
from PIL import Image
import os
from dotenv import load_dotenv
load_dotenv()


api_id = os.environ['24324252']
api_hash = os.environ['7f5a95a95508059acc07a7c3e3697081']
bot_token=os.environ['7786409745:AAF0pJMOGZHj5RuDkPUzi_zu5MDaE8CbFWA']

# Create a new client
app = pyrogram.Client("cutimagebg_bot", api_id, api_hash, bot_token)


@app.on_message(pyrogram.filters.command("start"))
async def start(app,message):
   await message.reply_text("""
Hi! I am a <b>Background 🖼️ Remover</b> can remove the background from images. 
Just send an image and let the <b>AI</b> do its magic.""")


@app.on_message()
async def handle_messages(app, message):
    if message.photo:
        # Download the image
        image_file = message.photo.file_id
        image_path = await app.download_media(image_file)
        #open the image file
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()
            new_image = remove(image_bytes)
        #save the file as valid image and send it
        image = Image.open(io.BytesIO(new_image))
        with io.BytesIO() as f:
            image.save(f, format='png')
            f.seek(0)
            await message.reply_photo(f)
        # remove the image after it has been processed and sent
        os.remove(image_path)

# Start the bot
app.run()
