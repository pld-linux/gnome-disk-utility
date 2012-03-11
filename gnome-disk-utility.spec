Summary:	Disk management application
Summary(pl.UTF-8):	Aplikacja do zarządzania dyskami
Name:		gnome-disk-utility
Version:	3.3.93
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-disk-utility/3.3/%{name}-%{version}.tar.xz
# Source0-md5:	2a4b9c005677a62a519b8197e6bba02f
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.31.0
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel >= 3.3.11
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool >= 2.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	tar >= 1:1.22
BuildRequires:	udisks2-devel >= 1.90.0
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	udisks2 >= 1.90.0
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
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang gnome-disk-utility

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f gnome-disk-utility.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/palimpsest
%{_datadir}/gnome-disk-utility
%{_desktopdir}/palimpsest.desktop
%{_iconsdir}/hicolor/*/*/*.png
