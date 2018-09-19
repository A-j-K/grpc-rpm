#!/bin/bash
#
# Script to build grpc rpm in docker.
#

set -e
set -x

cd $(dirname $0)/..

BUILD_ROOT=./rpmbuild
BUILD_CONTAINER=docker.io/hexinwang/centos7-builder
BUILD_COMMAND=/rpmbuild/docker-build-rpm.sh

echo "Launching ${BUILD_CONTAINER} ${DOCKER_BUILD_COMMAND}"
docker run \
  --rm \
  --tty \
  --interactive \
  --volume $(readlink -f "${BUILD_ROOT}"):/rpmbuild:z \
  --env BUILD_ROOT=/rpmbuild \
  --workdir /rpmbuild \
  ${BUILD_CONTAINER} \
  ${BUILD_COMMAND}
