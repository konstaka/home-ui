#!/bin/bash -e

sudo cp home-ui.service /etc/systemd/system/
sudo systemctl enable home-ui.service

# Add the following line to /etc/sudoers (sudo visudo):
# home ALL=(ALL) NOPASSWD: /bin/systemctl restart home-ui.service
