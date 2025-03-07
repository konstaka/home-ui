#!/bin/bash -e

while [[ $# -gt 0 ]]; do
    case $1 in
        -u|--user)
            DEPLOY_USER="$2"
            shift
            shift
            ;;
        -h|--host)
            DEPLOY_HOST="$2"
            shift
            shift
            ;;
    esac
done

if [ -z "$DEPLOY_USER" ] || [ -z "$DEPLOY_HOST" ]; then
    echo "Invalid arguments"
    exit 1
fi

pip freeze > requirements.txt

scp main.py $DEPLOY_USER@$DEPLOY_HOST:~/home-ui/
scp -r services $DEPLOY_USER@$DEPLOY_HOST:~/home-ui/
scp requirements.txt $DEPLOY_USER@$DEPLOY_HOST:~/home-ui/
scp setup_service.sh $DEPLOY_USER@$DEPLOY_HOST:~/home-ui/
scp home-ui.service $DEPLOY_USER@$DEPLOY_HOST:~/home-ui/
scp .env $DEPLOY_USER@$DEPLOY_HOST:~/home-ui/
ssh -t $DEPLOY_USER@$DEPLOY_HOST "pip install -r /home/$DEPLOY_USER/home-ui/requirements.txt && sudo systemctl restart home-ui.service"
