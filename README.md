# TELMG

## Install requeriments:
    
    pip install -r requeriments.txt
    
## HELP
    usage: telman.py [-h] [-c CHAT] [-q QUANTITY]

    options:
      -h, --help            show this help message and exit
      -c CHAT, --chat CHAT  chat
      -q QUANTITY, --quantity QUANTITY
                            Quantity messages for download

## Examples:
### Download last media message
    python3 telmg.py -c me
### Download last N media messages
    python3 telmg.py -c me -q <N>

