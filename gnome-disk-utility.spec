Summary:	Disk management application
Summary(pl.UTF-8):	Aplikacja do zarządzania dyskami
Name:		gnome-disk-utility
Version:	46.1
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-disk-utility/46/%{name}-%{version}.tar.xz
# Source0-md5:	bfc4d0cfbf186ba5bd487f3fddbf07d2
URL:		https://wiki.gnome.org/Apps/Disks
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-settings-daemon-devel >= 3.8
BuildRequires:	gtk+3-devel >= 3.16.0
BuildRequires:	libcanberra-gtk3-devel >= 0.1
BuildRequires:	libdvdread-devel >= 4.2.0
BuildRequires:	libhandy1-devel >= 1.5.0
BuildRequires:	libnotify-devel >= 0.7
BuildRequires:	libpwquality-devel >= 1.0.0
BuildRequires:	libsecret-devel >= 0.7
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	systemd-devel >= 1:209
BuildRequires:	tar >= 1:1.22
BuildRequires:	udisks2-devel >= 2.7.6
BuildRequires:	xz
BuildRequires:	xz-devel >= 1:5.0.5
Requires(post,postun):	glib2 >= 1:2.32.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.32.0
Requires:	gnome-settings-daemon >= 3.8
Requires:	gtk+3 >= 3.16.0
Requires:	hicolor-icon-theme
Requires:	libcanberra-gtk3 >= 0.1
Requires:	libdvdread >= 4.2.0
Requires:	libhandy1 >= 1.5.0
Requires:	libnotify >= 0.7
Requires:	libpwquality >= 1.0.0
Requires:	libsecret >= 0.7
Requires:	udisks2 >= 2.7.6
Requires:	xz-libs >= 1:5.0.5
Suggests:	openssh-gnome-askpass
Obsoletes:	gnome-disk-utility-apidocs < 3.4
Obsoletes:	gnome-disk-utility-devel < 3.4
Obsoletes:	gnome-disk-utility-libs < 3.4
Obsoletes:	gnome-disk-utility-static < 3.4
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
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

# not supported by glibc (as of 2.37)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang gnome-disk-utility

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f gnome-disk-utility.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md TODO
%attr(755,root,root) %{_bindir}/gnome-disk-image-mounter
%attr(755,root,root) %{_bindir}/gnome-disks
%attr(755,root,root) %{_libexecdir}/gsd-disk-utility-notify
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.DiskUtilityNotify.desktop
%{_datadir}/dbus-1/services/org.gnome.DiskUtility.service
%{_datadir}/glib-2.0/schemas/org.gnome.Disks.gschema.xml
%{_datadir}/metainfo/org.gnome.DiskUtility.appdata.xml
%{_desktopdir}/gnome-disk-image-mounter.desktop
%{_desktopdir}/gnome-disk-image-writer.desktop
%{_desktopdir}/org.gnome.DiskUtility.desktop
%{_iconsdir}/hicolor/scalable/apps/gnome-disks-state-standby-symbolic.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.DiskUtility.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.DiskUtility.Devel.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.DiskUtility-symbolic.svg
%{_mandir}/man1/gnome-disk-image-mounter.1*
%{_mandir}/man1/gnome-disks.1*
