#!/bin/bash

BASE_DIR=$(dirname "$0")
DOCKERFILE_DIR="${BASE_DIR}/.."
BUILD_VARIABLES="${BASE_DIR}/variables.sh"

source "${BUILD_VARIABLES}"

docker build --tag "${IMAGE_TAG}:${IMAGE_VERSION}" "${DOCKERFILE_DIR}"
