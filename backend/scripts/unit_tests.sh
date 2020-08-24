#!/bin/bash

docker-compose -f docker-compose.yml -f docker-compose.test.yml exec -T web coverage run --source='.' ./manage.py test unit_tests