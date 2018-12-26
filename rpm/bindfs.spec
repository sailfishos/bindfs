Name:    bindfs
Version: 1.13.10
Release: 1
Summary: Fuse filesystem to mirror a directory
Group:   System Environment/Base
License: GPLv2+
URL:     http://bindfs.org/
Source0: %{name}-%{version}.tar.bz2

BuildRequires: ruby
BuildRequires: fuse-devel
Requires:      fuse

%description
Bindfs allows you to mirror a directory and also change the the permissions in
the mirror directory.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
DESTDIR=${RPM_BUILD_ROOT} make install
rm ${RPM_BUILD_ROOT}/usr/share/man/man1/bindfs.1

%files
%{_bindir}/%{name}

