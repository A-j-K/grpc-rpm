# grpc-rpm
Build grpc related RPMs:
  tools/build.sh

RPMs are outputed under rpmbuild/RPMS/x86_64/.

grpc source code is downloaded from grpc github:
  git clone https://github.com/grpc/grpc.git grpc-1.24.0
  cd grpc-1.24.0
  git checkout v1.24.0
  git clean -f -d -x
  git submodule foreach --recursive git clean -f -d -x
  git submodule update --init
  cd ../; tar --exclude=.git -czvf /rpmbuild/SOURCES/grpc-1.24.0.tar.gz grpc-1.24.0
