#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
#
Summary:	Disk management application
Name:		gnome-disk-utility
Version:	2.28.0
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-disk-utility/2.28/%{name}-%{version}.tar.bz2
# Source0-md5:	2ef95e6d5949c0d623b16bb98108cce8
BuildRequires:	DeviceKit-disks-devel >= 007
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-keyring-devel >= 2.22.0
BuildRequires:	gtk+2-devel >= 2:2.18.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.3}
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libatasmart-devel >= 0.14
BuildRequires:	libnotify-devel >= 0.3.0
BuildRequires:	libtool
BuildRequires:	libunique-devel >= 1.0.0
BuildRequires:	nautilus-devel >= 2.24.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,postun):	gtk+2
Requires:	%{name}-libs = %{version}-%{release}
Requires:	DeviceKit-disks >= 007
Requires:	hicolor-icon-theme
Requires:	nautilus >= 2.24.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Palimpsest disk management application.
Palimpsest supports partitioning, file system creation, encryption,
RAID, SMART monitoring, etc.

%package libs
Summary:	gnome-disk-utility libraries
Summary(pl.UTF-8):	Biblioteki gnome-disk-utility
Group:		X11/Libraries

%description libs
gnome-disk-utility libraries.

%description libs -l pl.UTF-8
Biblioteki gnome-disk-utility.

%package devel
Summary:	Header files for gnome-disk-utility libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek gnome-disk-utility
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.16.0
Requires:	gtk+2-devel >= 2:2.18.0

%description devel
Header files for gnome-disk-utility libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek gnome-disk-utility.

%package static
Summary:	Static gnome-disk-utility libraries
Summary(pl.UTF-8):	Statyczne biblioteki gnome-disk-utility
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gnome-disk-utility libraries.

%description static -l pl.UTF-8
Statyczne biblioteki gnome-disk-utility.

%package apidocs
Summary:	gnome-disk-utility libraries API documentation
Summary(pl.UTF-8):	Dokumentacja API bibliotek gnome-disk-utility
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gnome-disk-utility libraries API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek gnome-disk-utility.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/libnautilus-gdu.{a,la}

%find_lang gnome-disk-utility
%find_lang palimpsest --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%post libs	-p /sbin/ldconfig
%postun	libs	-p /sbin/ldconfig

%files -f palimpsest.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/palimpsest
%attr(755,root,root) %{_libdir}/gdu-format-tool
%attr(755,root,root) %{_libdir}/gdu-notification-daemon
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/libnautilus-gdu.so
%{_sysconfdir}/xdg/autostart/gdu-notification-daemon.desktop
%{_desktopdir}/palimpsest.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg

%files libs -f gnome-disk-utility.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdu-gtk.so.*.*.*
%attr(755,root,root) %{_libdir}/libgdu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdu-gtk.so.0
%attr(755,root,root) %ghost %{_libdir}/libgdu.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdu-gtk.so
%attr(755,root,root) %{_libdir}/libgdu.so
%{_libdir}/libgdu-gtk.la
%{_libdir}/libgdu.la
%{_includedir}/gnome-disk-utility
%{_pkgconfigdir}/gdu-gtk.pc
%{_pkgconfigdir}/gdu.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdu-gtk.a
%{_libdir}/libgdu.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gnome-disk-utility
%endif
