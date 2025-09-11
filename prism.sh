#!/bin/bash
set -e

rm -rf prism && mkdir -p prism && cd prism
git clone --depth 1 https://${GITHUB_TOKEN}@github.com/sendgrid/sendgrid-oai .
cd prism

docker-compose build --parallel

if [ -z "$command" ]; then
  docker-compose up --force-recreate --abort-on-container-exit --remove-orphans
else
  docker-compose run helper-runner "$command"
  docker-compose down
fi
