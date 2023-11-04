#!/bin/bash

APP_NAME="petco-assignment"

while IFS="=" read -r key value; do
  heroku config:set "${key}=${value}" --app "$APP_NAME"
done < .env
