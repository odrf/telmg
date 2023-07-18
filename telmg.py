from tqdm import tqdm 
from config import Config
import util
import args
import os

client = Config().client()

def callback(current, total):
    global pbar
    global prev_curr
    pbar.update(current-prev_curr)
    prev_curr = current

async def download(chat, quantity):
    quantity = int(quantity)
    util.create_directory('downloads')
    global pbar
    global prev_curr
    async for message in client.iter_messages(chat, limit=quantity):
        if(message.document):
            name = F'{message.message}'
            pbar = tqdm(total=message.document.size, desc=F"Downloading {name}", unit='B', unit_scale=True)
        elif(message.media.photo):
                sz = message.media.photo.sizes[1].size
                name = F'{message.message}'
                pbar = tqdm(total=sz, desc=F"Downloading {name}", unit='B', unit_scale=True)
        prev_curr = 0
        await message.download_media('{}/{}'.format('downloads',name), progress_callback=callback)
        pbar.close()

async def upload(chat, file):
    global pbar
    global prev_curr
    sz = os.path.getsize(file)
    pbar = tqdm(total=sz, desc=F"Uploading {file}", unit='B', unit_scale=True)
    prev_curr = 0
    stream = True if 'mp4' in util.get_extension(file) else False
    thumb = util.get_thumb(file) if stream else None
    await client.send_file(chat, file, caption=file, supports_streaming=stream, thumb=thumb, progress_callback=callback)
    pbar.close()
    if thumb:
        os.remove(thumb)

if __name__ == '__main__':
    opt = args.train_options()
    chat = opt.chat if opt.chat else 'me'
    with client:
        if opt.upload:
            client.loop.run_until_complete(upload(chat, opt.upload))
        else:
            quantity = opt.quantity if opt.quantity else 1
            client.loop.run_until_complete(download(chat, quantity))
    