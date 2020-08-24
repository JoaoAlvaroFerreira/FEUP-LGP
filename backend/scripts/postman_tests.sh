#!/bin/bash

docker-compose -f docker-compose.yml -f docker-compose.test.yml run newman run collection.json -e environment.json

printf '\n\nEnter password if you want to delete postgres folder, else, press CTRL-C'

sudo rm -rf postgres

printf '\n\n'