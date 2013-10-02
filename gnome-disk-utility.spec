Summary:	Disk management application
Summary(pl.UTF-8):	Aplikacja do zarządzania dyskami
Name:		gnome-disk-utility
Version:	3.10.0
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-disk-utility/3.10/%{name}-%{version}.tar.xz
# Source0-md5:	d89ad8a648a2003266737c00e36c40e6
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-settings-daemon-devel >= 3.6
BuildRequires:	gtk+3-devel >= 3.6.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libcanberra-gtk3-devel >= 0.1
BuildRequires:	libdvdread-devel >= 4.2.0
BuildRequires:	libnotify-devel >= 0.7
BuildRequires:	libpwquality-devel >= 1.0.0
BuildRequires:	libsecret-devel >= 0.7
BuildRequires:	libtool >= 2.2
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	systemd-devel >= 44
BuildRequires:	tar >= 1:1.22
BuildRequires:	udisks2-devel >= 2.1.1
BuildRequires:	xz
BuildRequires:	xz-devel >= 1:5.0.5
Requires(post,postun):	glib2 >= 1:2.32.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.32.0
Requires:	gnome-themes-standard
Requires:	gtk+3 >= 3.6.0
Requires:	hicolor-icon-theme
Requires:	libdvdread >= 4.2.0
Requires:	libnotify >= 0.7
Requires:	libpwquality >= 1.0.0
Requires:	libsecret >= 0.7
Requires:	udisks2 >= 2.1.1
Suggests:	openssh-gnome-askpass
Obsoletes:	gnome-disk-utility-apidocs
Obsoletes:	gnome-disk-utility-devel
Obsoletes:	gnome-disk-utility-libs
Obsoletes:	gnome-disk-utility-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Palimpsest disk management application.
Palimpsest supports partitioning, file system creation, encryption,
RAID, SMART monitoring, etc.

%description -l pl.UTF-8
Ten pakiet zawiera aplikację do zarządzania dyskami Palimpsest.
Obsługuje ona partycjonowanie, tworzenie systemów plików, szyfrowanie,
RAID, monitorowanie SMART itp.

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
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon-3.0/*.la

%find_lang gnome-disk-utility

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache HighContrast
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache HighContrast
%update_icon_cache hicolor
%glib_compile_schemas

%files -f gnome-disk-utility.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/gnome-disk-image-mounter
%attr(755,root,root) %{_bindir}/gnome-disks
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libgdu-sd.so
%{_libdir}/gnome-settings-daemon-3.0/gdu-sd-plugin.gnome-settings-plugin
%{_datadir}/gnome-disk-utility
%{_desktopdir}/gnome-disk-image-mounter.desktop
%{_desktopdir}/gnome-disk-image-writer.desktop
%{_desktopdir}/gnome-disks.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Disks.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.gdu-sd.gschema.xml
%{_iconsdir}/HighContrast/*x*/apps/gnome-disks.png
%{_iconsdir}/hicolor/*x*/apps/gnome-disks.png
%{_iconsdir}/hicolor/scalable/apps/gnome-disks-state-standby-symbolic.svg
%{_mandir}/man1/gnome-disk-image-mounter.1*
%{_mandir}/man1/gnome-disks.1*
