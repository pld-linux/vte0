Summary:	VTE terminal widget library
Summary(pl.UTF-8):	Biblioteka z kontrolką terminala VTE
Name:		vte
Version:	0.28.0
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/vte/0.28/%{name}-%{version}.tar.bz2
# Source0-md5:	c21e08e973a47a9d105c24506e537848
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.13
BuildRequires:	gtk-doc-automake
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.592
Requires(pre):	utempter
Obsoletes:	python-vte
Obsoletes:	python-vte-devel
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The vte package contains a terminal widget for GTK+. It's used by
gnome-terminal among other programs.

%description -l pl.UTF-8
Ten pakiet zawiera kontrolkę terminala dla GTK+. Jest używany przez
gnome-terminal oraz inne programy.

%package devel
Summary:	Headers for VTE
Summary(pl.UTF-8):	Pliki nagłówkowe VTE
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.28.0
Requires:	gtk+3-devel >= 3.0.0
Requires:	ncurses-devel
Conflicts:	gnome-libs-devel < 1.4.1.2

%description devel
The vte package contains a terminal widget for GTK+. It's used by
gnome-terminal among other programs.

You should install the vte-devel package if you would like to compile
applications that use the vte terminal widget. You do not need to
install vte-devel if you just want to use precompiled applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do kompilowania programów używających vte.

%package static
Summary:	Static VTE library
Summary(pl.UTF-8):	Statyczna biblioteka VTE
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Conflicts:	gnome-libs-static < 1.4.1.2

%description static
Static version of VTE libraries.

%description static -l pl.UTF-8
Statyczna wersja bibliotek VTE.

%package apidocs
Summary:	VTE API documentation
Summary(pl.UTF-8):	Dokumentacja API VTE
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
VTE API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API VTE.

%prep
%setup -q

%build
%{__gtkdocize}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
cd gnome-pty-helper
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
cd ..
%configure \
	--disable-silent-rules \
	--enable-gtk-doc \
	--with-gtk=3.0 \
	--enable-introspection \
	--with-default-emulation=xterm \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}-2.90

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f vte-2.90.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/vte2_90
%attr(755,root,root) %{_libdir}/libvte2_90.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvte2_90.so.9
%{_libdir}/girepository-1.0/Vte-2.90.typelib
%attr(2755,root,utmp) %{_libdir}/gnome-pty-helper
%{_datadir}/vte

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvte2_90.so
%{_includedir}/vte-2.90
%{_pkgconfigdir}/vte-2.90.pc
%{_datadir}/gir-1.0/Vte-2.90.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libvte2_90.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/vte-2.90
