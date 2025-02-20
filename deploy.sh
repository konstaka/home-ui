#!/bin/bash -e

USER=home
HOST=home-ui.local

pip freeze > requirements.txt

scp main.py $USER@$HOST:~/home-ui/
scp -r services $USER@$HOST:~/home-ui/
scp requirements.txt $USER@$HOST:~/home-ui/
scp setup_service.sh $USER@$HOST:~/home-ui/
scp home-ui.service $USER@$HOST:~/home-ui/
ssh -t $USER@$HOST "pip install -r /home/$USER/home-ui/requirements.txt && sudo systemctl restart home-ui.service"
