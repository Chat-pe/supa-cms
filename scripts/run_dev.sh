#add all the scripts here

#set the env variables for the development environment

#consider the variables in the env file and export them
export $(cat ./dev.env | xargs)



set -e

DEFAULT_MODULE_NAME=src.app

MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}
VARIABLE_NAME=${VARIABLE_NAME:-app}
export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}
export ENVIRONMENT=${ENVIRONMENT:-dev} 

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-9009}
LOG_LEVEL=${LOG_LEVEL:-info}
LOG_CONFIG=${LOG_CONFIG:-/src/logging.ini}

# Start Uvicorn with live reload
exec uvicorn --reload --proxy-headers --host $HOST --port $PORT "$APP_MODULE"