Summary:	VTE terminal widget library for GTK+ 2
Summary(pl.UTF-8):	Biblioteka z kontrolką terminala VTE for GTK+ 2
Name:		vte0
Version:	0.28.2
Release:	19
License:	LGPL v2+
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/vte/0.28/vte-%{version}.tar.bz2
# Source0-md5:	f07a4bf943194f94b7f142db8f7f36dc
Patch0:		vte-alt-meta.patch
Patch1:		repaint-bug.patch
Patch2:		vte-0.28.2-control.patch
Patch3:		vte-0.28.2-limit-arguments.patch
Patch4:		vte-0.28.2-paste-fix.diff
Patch5:		vte-python-bugfixes.patch
URL:		https://wiki.gnome.org/Apps/Terminal/VTE
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+2-devel >= 2:2.20.0
BuildRequires:	gtk-doc >= 1.13
BuildRequires:	gtk-doc-automake >= 1.13
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	ncurses-devel
BuildRequires:	pango-devel >= 1:1.22.0
BuildRequires:	pkgconfig
BuildRequires:	python-pygtk-devel >= 2:2.12.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.592
Requires(pre):	utempter
Requires:	glib2 >= 1:2.28.0
Requires:	gtk+2 >= 2:2.20.0
Requires:	pango >= 1:1.22.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The vte package contains a terminal widget for GTK+ 2.x. It's used by
gnome-terminal among other programs.

%description -l pl.UTF-8
Ten pakiet zawiera kontrolkę terminala dla GTK+ 2.x. Jest używany
przez gnome-terminal oraz inne programy.

%package devel
Summary:	Header files for VTE for GTK+ 2
Summary(pl.UTF-8):	Pliki nagłówkowe VTE dla GTK+ 2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.28.0
Requires:	gtk+2-devel >= 2:2.20.0
Requires:	ncurses-devel
Requires:	pango-devel >= 1:1.22.0
Conflicts:	gnome-libs-devel < 1.4.1.2

%description devel
This package contains header files for GTK+ 2 based vte library.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do kompilowania programów używających
biblioteki vte opartej na GTK+ 2.

%package static
Summary:	Static VTE library for GTK+ 2
Summary(pl.UTF-8):	Statyczna biblioteka VTE dla GTK+ 2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Conflicts:	gnome-libs-static < 1.4.1.2

%description static
Static version of VTE library for GTK+ 2.

%description static -l pl.UTF-8
Statyczna wersja biblioteki VTE dla GTK+ 2.

%package apidocs
Summary:	VTE API documentation - GTK+ 2.x version
Summary(pl.UTF-8):	Dokumentacja API VTE - wersja dla GTK+ 2.x
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
VTE API documentation - GTK+ 2.x version.

%description apidocs -l pl.UTF-8
Dokumentacja API VTE - wersja dla GTK+ 2.x.

%package -n python-vte0
Summary:	Python VTE module
Summary(pl.UTF-8):	Moduł VTE dla pythona
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-libs
Requires:	python-pygtk-gtk >= 2:2.12.0
Provides:	python-vte
Obsoletes:	python-vte < 0.30

%description -n python-vte0
Python VTE library.

%description -n python-vte0 -l pl.UTF-8
Biblioteka VTE dla pythona.

%package -n python-vte0-devel
Summary:	Development files for VTE Python bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Pythona do VTE
Group:		Development/Languages/Python
Requires:	%{name}-devel = %{version}-%{release}
Requires:	python-vte0 = %{version}-%{release}
Provides:	python-vte-devel
Obsoletes:	python-vte-devel < 0.30

%description -n python-vte0-devel
Development files for VTE Python bindings.

%description -n python-vte0-devel -l pl.UTF-8
Pliki programistyczne wiązań Pythona do VTE.

%prep
%setup -q -n vte-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
%configure \
	--libexecdir=%{_libexecdir}/vte-0.0 \
	--with-gtk=2.0 \
	--disable-silent-rules \
	--enable-gtk-doc \
	--enable-introspection \
	--with-default-emulation=xterm \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la \
	$RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/vtemodule.{la,a}

%find_lang vte-0.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f vte-0.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/vte
%attr(755,root,root) %{_libdir}/libvte.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvte.so.9
%{_libdir}/girepository-1.0/Vte-0.0.typelib
%dir %{_libexecdir}/vte-0.0
%attr(2755,root,utmp) %{_libexecdir}/vte-0.0/gnome-pty-helper
%{_datadir}/vte

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvte.so
%{_includedir}/vte-0.0
%{_pkgconfigdir}/vte.pc
%{_datadir}/gir-1.0/Vte-0.0.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libvte.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/vte-0.0

%files -n python-vte0
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/vtemodule.so

%files -n python-vte0-devel
%defattr(644,root,root,755)
%{_datadir}/pygtk/2.0/defs/vte.defs
%{_pkgconfigdir}/pyvte.pc
