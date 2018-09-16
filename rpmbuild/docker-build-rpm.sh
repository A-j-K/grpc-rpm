#!/bin/bash

set -e
set -x

# Run the build with the same uid as the outside user so that
# the build output has the same permission.
extuid=$(stat -c %u /rpmbuild)
extgid=$(stat -c %g /rpmbuild)
if [ $(id -u) != "$extuid" ]; then
  groupadd build --gid $extgid
  useradd build --groups wheel \
    --home-dir /rpmbuild \
    --uid $extuid \
    --gid $extgid \
    --no-create-home
  su build "$0" "$@"
  exit 0
fi

echo "Building grpc RPMs..."
rpmbuild -ba \
  -D "_topdir ${BUILD_ROOT}" \
  -D "release 1" \
  -without check \
  "${BUILD_ROOT}/SPECS/grpc.spec"

echo "Building protobuf RPMs..."
rpmbuild -ba \
  -D "_topdir ${BUILD_ROOT}" \
  -D "release 1" \
  -without check \
  "${BUILD_ROOT}/SPECS/protobuf.spec"
