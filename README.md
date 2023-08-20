# TELMG

##
    Note that you need an api_id & api_hash to be able to use telmg, please visit https://my.telegram.org or send me an email to odrf@ciencias.unam.mx

## Install requeriments: 
    
    pip install -r requeriments.txt
    
## HELP
    usage: telmg.py [-h] [-c CHAT] [-q QUANTITY]

    options:
        -h, --help            show this help message and exit
        -c CHAT, --chat CHAT  chat
        -q QUANTITY, --quantity QUANTITY
                        Quantity of messages to download
        -u UPLOAD, --upload UPLOAD
                        Path file to upload

## Examples:
### Download last media message from @me (saved messages)
    python3 telmg.py -c me
### Download last N media messages from @me (saved messages)
    python3 telmg.py -c me -q <N>
### Upload file to @me (saved messages)
    python3 telmg.py -c me -u photo.jpg

