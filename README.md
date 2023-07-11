# TELMG

## Install requeriments:
    
    pip install -r requeriments.txt
    
## HELP
    usage: telman.py [-h] [-c CHAT] [-q QUANTITY]

    options:
      -h, --help            show this help message and exit
      -c CHAT, --chat CHAT  chat
      -q QUANTITY, --quantity QUANTITY
                            Quantity of messages to download

## Examples:
### Download last media message from @me (saved messages)
    python3 telman.py -c me
### Download last N media messages from @me (saved messages)
    python3 telman.py -c me -q <N>

