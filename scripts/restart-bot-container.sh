#!/bin/bash

BASE_DIR=$(dirname "$0")
BUILD_VARIABLES="${BASE_DIR}/variables.sh"

source "${BUILD_VARIABLES}"

BOT_TOKEN_FILE="${BASE_DIR}/../secret-token"
BOT_TOKEN="$(cat "${BOT_TOKEN_FILE}")"

docker stop "${CONTAINER_NAME}"
docker rm "${CONTAINER_NAME}"
docker run --restart unless-stopped -dit -e BOT_TOKEN="${BOT_TOKEN}" --name "${CONTAINER_NAME}" "${IMAGE_TAG}:${IMAGE_VERSION}"
