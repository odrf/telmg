import os
import errno
import json
import ffmpeg

def create_directory(dir):
    if not (os.path.exists(dir)):
        try:
            os.mkdir(dir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
            
def get_extension(file):
    ext = file.split(".")
    return ext[len(ext)-1]

def to_json(file, key, some):
    data = {}
    if os.path.exists(file):
            try:
                with open(file) as json_file: 
                    data = json.load(json_file)
            except json.decoder.JSONDecodeError as error:
                data = {}
    data[key] = some
    with open(file, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(data, indent=4)
        jsonf.write(jsonString)

def get_json(file, key, some):
    data = {}
    if os.path.exists(file):
            try:
                with open(file) as json_file: 
                    data = json.load(json_file)
            except json.decoder.JSONDecodeError as error:
                data = {}
    data[key] = some
    with open(file, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(data, indent=4)
        jsonf.write(jsonString)

def get_thumb(file):
    create_directory('.tmp')
    path = F'.tmp/{file.split(".")[0]}.jpg'
    (
        ffmpeg.input(file, ss=0)
        .filter('scale', 320, -1)
        .output(path, vframes=1)
        .run(capture_stdout=True, capture_stderr=True)
    )
    return path