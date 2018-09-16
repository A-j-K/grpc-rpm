Name:           protobuf
Version:        3.0.x
Summary:        Implementation of the google protobuf protocol

%{!?release: %define release 1}
Release: %{?release}%{?dist}

License:        BSD
URL:            https://github.com/google/protobuf.git
Source:         protobuf-3.0.x.tar.gz

BuildRequires:  libtool

%description
Google protobuf.

%package devel
Summary: protobuf headers
Requires: %{name} = %{version}-%{release}

%description devel
This package contains protobuf headers


%prep
%setup -q


%build
./autogen.sh
./configure prefix=%{_prefix} libdir=%{_libdir}
make %{?_smp_mflags} prefix=%{_prefix} libdir=%{_libdir}


%install
make install prefix=%{buildroot}%{_prefix} libdir=%{buildroot}%{_libdir}

# Makefile fix
#%{__mv} %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}


%files
%{_bindir}/*
%{_libdir}/lib*
%doc CONTRIBUTORS.txt LICENSE README.md

%files devel
%{_includedir}/google/%{name}*
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
