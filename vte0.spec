Summary:	VTE terminal widget library
Summary(pl.UTF-8):	Biblioteka z kontrolką terminala VTE
Name:		vte
Version:	0.28.0
Release:	2
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
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.13
BuildRequires:	gtk-doc-automake
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	python-pygtk-devel >= 2:2.12.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.592
Requires(pre):	utempter
Requires:	%{name}-common = %{version}-%{release}
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The vte package contains a terminal widget for GTK+ 3.x. It's used by
gnome-terminal among other programs.

%description -l pl.UTF-8
Ten pakiet zawiera kontrolkę terminala dla GTK+ 3.x. Jest używany przez
gnome-terminal oraz inne programy.

%package -n vte0
Summary:	VTE terminal widget library
Summary(pl.UTF-8):	Biblioteka z kontrolką terminala VTE
Group:		X11/Libraries
Requires:	%{name}-common = %{version}-%{release}

%description -n vte0
The vte package contains a terminal widget for GTK+ 2.x. It's used by
gnome-terminal among other programs.

%description -n vte0 -l pl.UTF-8
Ten pakiet zawiera kontrolkę terminala dla GTK+ 2.x. Jest używany przez
gnome-terminal oraz inne programy.

%package common
Summary:	Common files for vte and vte0
Group:		X11/Libraries

%description common
Common files for vte and vte0.

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
The vte package contains a terminal widget for GTK+ 3.x. It's used by
gnome-terminal among other programs.

You should install the vte-devel package if you would like to compile
applications that use the vte terminal widget. You do not need to
install vte-devel if you just want to use precompiled applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do kompilowania programów używających vte.

%package -n vte0-devel
Summary:	Headers for VTE
Summary(pl.UTF-8):	Pliki nagłówkowe VTE
Group:		X11/Development/Libraries
Requires:	vte0 = %{version}-%{release}
Requires:	glib2-devel >= 1:2.28.0
Requires:	gtk+2-devel >= 2:2.14.0
Requires:	ncurses-devel
Conflicts:	gnome-libs-devel < 1.4.1.2

%description -n vte0-devel
The vte package contains a terminal widget for GTK+ 2.x. It's used by
gnome-terminal among other programs.

You should install the vte-devel package if you would like to compile
applications that use the vte terminal widget. You do not need to
install vte-devel if you just want to use precompiled applications.

%description -n vte0-devel -l pl.UTF-8
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

%package -n vte0-static
Summary:	Static VTE library - GTK+ 2.x version
Summary(pl.UTF-8):	Statyczna biblioteka VTE - wersja dla GTK+ 2.x
Group:		X11/Development/Libraries
Requires:	vte0-devel = %{version}-%{release}
Conflicts:	gnome-libs-static < 1.4.1.2

%description -n vte0-static
Static version of VTE libraries - GTK+ 2.x version.

%description -n vte0-static -l pl.UTF-8
Statyczna wersja bibliotek VTE - wersja dla GTK+ 2.x.

%package -n python-vte
Summary:	Python VTE module
Summary(pl.UTF-8):	Moduł VTE dla pythona
Group:		Libraries/Python
%pyrequires_eq	python-libs
Requires:	vte0 = %{version}-%{release}
Requires:	python-pygtk-gtk >= 2:2.12.0

%description -n python-vte
Python VTE library.

%description -n python-vte -l pl.UTF-8
Biblioteka VTE dla pythona.

%package -n python-vte-devel
Summary:	Development files for VTE Python bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Pythona do VTE
Group:		Development/Languages/Python
Requires:	vte0-devel = %{version}-%{release}
Requires:	python-vte = %{version}-%{release}

%description -n python-vte-devel
Development files for VTE Python bindings.

%description -n python-vte-devel -l pl.UTF-8
Pliki programistyczne wiązań Pythona do VTE.

%package apidocs
Summary:	VTE API documentation
Summary(pl.UTF-8):	Dokumentacja API VTE
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
VTE API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API VTE.

%package -n vte0-apidocs
Summary:	VTE API documentation - GTK+ 2.x version
Summary(pl.UTF-8):	Dokumentacja API VTE - wersja dla GTK+ 2.x
Group:		Documentation
Requires:	gtk-doc-common

%description -n vte0-apidocs
VTE API documentation - GTK+ 2.x version.

%description -n vte0-apidocs -l pl.UTF-8
Dokumentacja API VTE - wersja dla GTK+ 2.x.

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
COMMON_OPTIONS="--disable-silent-rules \
	--enable-gtk-doc \
	--enable-introspection \
	--with-default-emulation=xterm \
	--with-html-dir=%{_gtkdocdir}
"
mkdir gtk{2,3}
cd gtk2
../%configure \
	--with-gtk=2.0 \
	$COMMON_OPTIONS
%{__make}
cd ../gtk3
../%configure \
	--with-gtk=3.0 \
	$COMMON_OPTIONS
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT

cd gtk2
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ../gtk3
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la \
	$RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/vtemodule.{la,a}

%find_lang %{name}-2.90
%find_lang %{name}-0.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f vte-2.90.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vte2_90
%attr(755,root,root) %{_libdir}/libvte2_90.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvte2_90.so.9
%{_libdir}/girepository-1.0/Vte-2.90.typelib

%files -n vte0 -f vte-0.0.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vte
%attr(755,root,root) %{_libdir}/libvte.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvte.so.9
%{_libdir}/girepository-1.0/Vte-0.0.typelib

%files common
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(2755,root,utmp) %{_libdir}/gnome-pty-helper
%{_datadir}/vte

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvte2_90.so
%{_includedir}/vte-2.90
%{_pkgconfigdir}/vte-2.90.pc
%{_datadir}/gir-1.0/Vte-2.90.gir

%files -n vte0-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvte.so
%{_includedir}/vte-0.0
%{_pkgconfigdir}/vte.pc
%{_datadir}/gir-1.0/Vte-0.0.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libvte2_90.a

%files -n vte0-static
%defattr(644,root,root,755)
%{_libdir}/libvte.a

%files -n python-vte
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/vtemodule.so

%files -n python-vte-devel
%defattr(644,root,root,755)
%{_datadir}/pygtk/2.0/defs/*.defs
%{_pkgconfigdir}/pyvte.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/vte-2.90

%files -n vte0-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/vte-0.0
