#!/bin/bash

docker-compose -f docker-compose.yml exec -T web pylint --load-plugins pylint_django martin_helder unit_tests
