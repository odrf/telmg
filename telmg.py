# from telethon import TelegramClient
from tqdm import tqdm 
from config import Config
import util
import args

client = Config().client()

def callback(current, total):
    global pbar
    global prev_curr
    pbar.update(current-prev_curr)
    prev_curr = current

async def download(desde, quantity):
    quantity = int(quantity)
    me = await client.get_me()
    util.create_directory('downloads')
    global pbar
    global prev_curr
    async for message in client.iter_messages(desde, limit=quantity):
        # print(message.media.document)
        if(message.document):
            name = F'{message.message}'
            pbar = tqdm(total=message.document.size, desc=F"Downloading {name}", unit='B', unit_scale=True)
        elif(message.media.photo):
                # print( message.media.photo.sizes[1].size)
                sz = message.media.photo.sizes[1].size
                name = F'{message.message}'
                pbar = tqdm(total=sz, desc=F"Downloading {name}", unit='B', unit_scale=True)
            
            # ext = message.media.document.mime_type.split('/')[1]
        prev_curr = 0
        path = await message.download_media('{}/{}'.format('downloads',name), progress_callback=callback)
        pbar.close()

if __name__ == '__main__':
    opt = args.train_options()
    if(opt.chat):
        with client:
            if(opt.quantity):
                client.loop.run_until_complete(download(opt.chat, opt.quantity))
            else:
                client.loop.run_until_complete(download(opt.chat, 1))

    