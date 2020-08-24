# !/bin/bash

set - f

ssh -i "aws-lgp.pem" -oStrictHostKeyChecking=no ubuntu@$DEPLOY_STAGING_SERVER "cd ./lgp-3d && git stash && git fetch --all && git reset --hard origin/develop && cd backend && docker-compose down && sudo rm -rf postgres && docker-compose up -d --build"
