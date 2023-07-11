import os
import json
import util
from telethon import TelegramClient

class Config:
    def __init__(self):
        self.dir = '.config'
        self.data = {}
        self.path = F'{self.dir}/config.json'
        
        if os.path.exists(self.path):
            try:
                with open(self.path) as json_file: 
                    self.data = json.load(json_file)
            except json.decoder.JSONDecodeError as error:
                self.data = {}


    def client(self):
        util.create_directory(self.dir)
        file_config = F'{self.dir}/config.json'
        client = None

        while True:
            # print('aa')
            try:
                # print('here1')
                api_id = self.get('api_id')
                api_hash = self.get('api_hash')
                client = TelegramClient(F'{self.dir}/session_name.session', int(api_id), api_hash)
                break
            except Exception as e:
                # print('here2')
                api_id = input('Enter api id: ').strip()
                api_hash = input('Enter api hash: ').strip()
                self.to_json('api_id', api_id)
                self.to_json('api_hash', api_hash)
                try:
                    # print('here3')
                    client = TelegramClient(F'{self.dir}/session_name.session', int(api_id), api_hash)
                    break
                except:
                    pass
                    # print('here4')
                
        return client

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None

    def to_json(self, key, some):
        if os.path.exists(self.path):
                try:
                    with open(self.path) as json_file: 
                        self.data = json.load(json_file)
                except json.decoder.JSONDecodeError as error:
                    self.data = {}
        self.data[key] = some
        with open(self.path, 'w', encoding='utf-8') as jsonf:
            jsonString = json.dumps(self.data, indent=4)
            jsonf.write(jsonString)