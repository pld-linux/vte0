Summary:	VTE terminal widget library
Summary(pl.UTF-8):	Biblioteka z kontrolką terminala VTE
Name:		vte
Version:	0.28.2
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/vte/0.28/%{name}-%{version}.tar.bz2
# Source0-md5:	f07a4bf943194f94b7f142db8f7f36dc
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+2-devel >= 2:2.20.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.13
BuildRequires:	gtk-doc-automake >= 1.13
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	ncurses-devel
BuildRequires:	pango-devel >= 1:1.22.0
BuildRequires:	pkgconfig
BuildRequires:	python-pygtk-devel >= 2:2.12.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.592
Requires:	%{name}-common = %{version}-%{release}
Requires:	glib2 >= 1:2.28.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
Requires:	pango >= 1:1.22.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The vte package contains a terminal widget for GTK+ 3.x. It's used by
gnome-terminal among other programs.

%description -l pl.UTF-8
Ten pakiet zawiera kontrolkę terminala dla GTK+ 3.x. Jest używany
przez gnome-terminal oraz inne programy.

%package common
Summary:	Common files for vte and vte0
Summary(pl.UTF-8):	Pliki wspólne dla vte i vte0
Group:		X11/Libraries
Requires(pre):	utempter

%description common
Common files for GTK+ 3 based vte and GTK+ 2 based vte0.

%description common -l pl.UTF-8
Pliki wspólne dla vte opartego na GTK+ 3 oraz vte0 opartego na GTK+ 2.

%package devel
Summary:	Header files for VTE for GTK+ 3
Summary(pl.UTF-8):	Pliki nagłówkowe VTE dla GTK+ 3
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.28.0
Requires:	gtk+3-devel >= 3.0.0
Requires:	ncurses-devel
Requires:	pango-devel >= 1:1.22.0
Conflicts:	gnome-libs-devel < 1.4.1.2

%description devel
This package contains header files for GTK+ 3 based vte library.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do kompilowania programów używających
biblioteki vte opartej na GTK+ 3.

%package static
Summary:	Static VTE library for GTK+ 3
Summary(pl.UTF-8):	Statyczna biblioteka VTE dla GTK+ 3
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Conflicts:	gnome-libs-static < 1.4.1.2

%description static
Static version of VTE library for GTK+ 3.

%description static -l pl.UTF-8
Statyczna wersja biblioteki VTE dla GTK+ 3.

%package apidocs
Summary:	VTE API documentation (GTK+ 3 version)
Summary(pl.UTF-8):	Dokumentacja API VTE (wersja dla GTK+ 3)
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
VTE API documentation (GTK+ 3 version).

%description apidocs -l pl.UTF-8
Dokumentacja API VTE (wersja dla GTK+ 3).

%package -n vte0
Summary:	VTE terminal widget library for GTK+ 2
Summary(pl.UTF-8):	Biblioteka z kontrolką terminala VTE dla GTK+ 2
Group:		X11/Libraries
Requires:	%{name}-common = %{version}-%{release}
Requires:	glib2 >= 1:2.28.0
Requires:	gtk+2 >= 2:2.20.0
Requires:	pango >= 1:1.22.0

%description -n vte0
The vte package contains a terminal widget for GTK+ 2.x. It's used by
gnome-terminal among other programs.

%description -n vte0 -l pl.UTF-8
Ten pakiet zawiera kontrolkę terminala dla GTK+ 2.x. Jest używany
przez gnome-terminal oraz inne programy.

%package -n vte0-devel
Summary:	Header files for VTE for GTK+ 2
Summary(pl.UTF-8):	Pliki nagłówkowe VTE dla GTK+ 2
Group:		X11/Development/Libraries
Requires:	vte0 = %{version}-%{release}
Requires:	glib2-devel >= 1:2.28.0
Requires:	gtk+2-devel >= 2:2.20.0
Requires:	ncurses-devel
Requires:	pango-devel >= 1:1.22.0
Conflicts:	gnome-libs-devel < 1.4.1.2

%description -n vte0-devel
This package contains header files for GTK+ 2 based vte library.

%description -n vte0-devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do kompilowania programów używających
biblioteki vte opartej na GTK+ 2.

%package -n vte0-static
Summary:	Static VTE library for GTK+ 2
Summary(pl.UTF-8):	Statyczna biblioteka VTE dla GTK+ 2
Group:		X11/Development/Libraries
Requires:	vte0-devel = %{version}-%{release}
Conflicts:	gnome-libs-static < 1.4.1.2

%description -n vte0-static
Static version of VTE library for GTK+ 2.

%description -n vte0-static -l pl.UTF-8
Statyczna wersja biblioteki VTE dla GTK+ 2.

%package -n vte0-apidocs
Summary:	VTE API documentation - GTK+ 2.x version
Summary(pl.UTF-8):	Dokumentacja API VTE - wersja dla GTK+ 2.x
Group:		Documentation
Requires:	gtk-doc-common

%description -n vte0-apidocs
VTE API documentation - GTK+ 2.x version.

%description -n vte0-apidocs -l pl.UTF-8
Dokumentacja API VTE - wersja dla GTK+ 2.x.

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

%{__make} -C gtk2 install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} -C gtk3 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la \
	$RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/vtemodule.{la,a}

%find_lang %{name}-2.90
%find_lang %{name}-0.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n vte0 -p /sbin/ldconfig
%postun	-n vte0 -p /sbin/ldconfig

%files -f vte-2.90.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vte2_90
%attr(755,root,root) %{_libdir}/libvte2_90.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvte2_90.so.9
%{_libdir}/girepository-1.0/Vte-2.90.typelib

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

%files static
%defattr(644,root,root,755)
%{_libdir}/libvte2_90.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/vte-2.90

%files -n vte0 -f vte-0.0.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vte
%attr(755,root,root) %{_libdir}/libvte.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvte.so.9
%{_libdir}/girepository-1.0/Vte-0.0.typelib

%files -n vte0-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvte.so
%{_includedir}/vte-0.0
%{_pkgconfigdir}/vte.pc
%{_datadir}/gir-1.0/Vte-0.0.gir

%files -n vte0-static
%defattr(644,root,root,755)
%{_libdir}/libvte.a

%files -n vte0-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/vte-0.0

%files -n python-vte
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/vtemodule.so

%files -n python-vte-devel
%defattr(644,root,root,755)
%{_datadir}/pygtk/2.0/defs/vte.defs
%{_pkgconfigdir}/pyvte.pc
