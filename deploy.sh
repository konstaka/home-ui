#!/bin/bash -e

USER=home
HOST=homeassistant.local

scp main.py $USER@$HOST:~/home-ui/
scp requirements.txt $USER@$HOST:~/home-ui/
ssh -t $USER@$HOST "pip install -r /home/$USER/home-ui/requirements.txt && python3 /home/$USER/home-ui/main.py"
