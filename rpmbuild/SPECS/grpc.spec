Name:           grpc
Summary:        Implementation of the gRPC protocol
Version:        1.24.0

%{!?release: %define release 1}
Release: %{?release}%{?dist}

License:        BSD
URL:            http://www.grpc.io/
#%undefine       _disable_source_fetch
#Source:         https://github.com/grpc/grpc/archive/v%{version}.tar.gz
Source:         grpc-%{version}.tar.gz

BuildRequires:  libtool
BuildRequires:  openssl-devel

%description
Remote Procedure Calls (RPCs) provide a useful abstraction for
building distributed applications and services. The libraries
in this repository provide a concrete implementation of the gRPC
protocol, layered over HTTP/2. These libraries enable communication
between clients and servers using any combination of the supported
languages.


%package devel
Summary: gRPC headers
Requires: %{name} = %{version}-%{release}

%description devel
This package contains gRPC headers


%prep
%setup -q
#sed -r 's|^PROTOBUF_CHECK_CMD = \$\(PKG_CONFIG\) --atleast-version=[^[:space:]]+ protobuf|PROTOBUF_CHECK_CMD = $(PKG_CONFIG) --atleast-version=3.0.0 protobuf|' -i Makefile


%build
make %{?_smp_mflags} prefix=%{_prefix} libdir=%{_libdir}


%install
make install prefix=%{buildroot}%{_prefix} libdir=%{buildroot}%{_libdir}
# A kludge to fix grpc "make install". Proper fix should be done inside grpc build script.
cd %{buildroot}%{_prefix}/lib
ln -sf libgrpc++.so.%{version} libgrpc++.so.1
ln -sf libgrpc++_cronet.so.%{version} libgrpc++_cronet.so.1
ln -sf libgrpc++_error_details.so.%{version} libgrpc++_error_details.so.1
ln -sf libgrpc++_reflection.so.%{version} libgrpc++_reflection.so.1
ln -sf libgrpc++_unsecure.so.%{version} libgrpc++_unsecure.so.1

# Makefile fix
%{__mv} %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}


%files
%{_bindir}/*
%{_libdir}/lib*
%{_datarootdir}/%{name}
%doc CONTRIBUTING.md LICENSE README.md

%files devel
%{_includedir}/%{name}*
%{_libdir}/pkgconfig/*


%changelog
* Thu Jan 19 2017 Romain Acciari <romain.acciari@openio.io> - 1.0.1-1
- Bugfix release
* Wed Sep 07 2016 Romain Acciari <romain.acciari@openio.io> - 1.0.0-1
- Updated to 1.0.0
* Wed Feb 24 2016 Romain Acciari <romain.acciari@openio.io> - 0.13.0-1
- New release
- Fix pkgconfig
* Fri Dec 18 2015 Romain Acciari <romain.acciari@openio.io> - 0.11.1-1
- Initial release
