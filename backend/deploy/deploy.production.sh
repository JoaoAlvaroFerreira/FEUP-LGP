# !/bin/bash

set - f

ssh -i "aws-production.pem" -oStrictHostKeyChecking=no ubuntu@$DEPLOY_PRODUCTION_SERVER "cd ./lgp-3d && git stash && git fetch --all && git reset --hard origin/master && cd backend && docker-compose -f docker-compose.prod.yml down && docker-compose -f docker-compose.prod.yml up -d --build"
