import argparse

def train_options():
    parser = argparse.ArgumentParser()
    # parser.add_argument('-d','--download', action='store', help='video to download')
    parser.add_argument('-c','--chat', action='store', help='chat')
    opt = parser.parse_args()
    return opt