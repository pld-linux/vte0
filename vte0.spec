#
# Conditional build:
%bcond_with	glx # build for GLX support
#
Summary:	VTE terminal widget library
Summary(pl):	Biblioteka z kontrolk± terminala VTE
Name:		vte
Version:	0.13.5
Release:	2
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/vte/0.13/%{name}-%{version}.tar.bz2
# Source0-md5:	47ea2c90bd64a7e8749cf7640dc82a28
Patch0:		%{name}-keys.patch
%{?with_glx:BuildRequires:	OpenGL-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.1
BuildRequires:	gtk+2-devel >= 2:2.10.1
BuildRequires:	gtk-doc
BuildRequires:	libart_lgpl-devel >= 2.3.10
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	python-pygtk-devel >= 2:2.9.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(pre):	utempter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The vte package contains a terminal widget for GTK+. It's used by
gnome-terminal among other programs.

%description -l pl
Ten pakiet zawiera kontrolkê terminala dla GTK+. Jest u¿ywany przez
gnome-terminal oraz inne programy.

%package devel
Summary:	Headers for VTE
Summary(pl):	Pliki nag³ówkowe VTE
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_glx:Requires:	OpenGL-devel}
Requires:	glib2-devel >= 1:2.12.1
Requires:	gtk+2-devel >= 2:2.10.1
Requires:	libart_lgpl-devel >= 2.3.10
Requires:	ncurses-devel
Conflicts:	gnome-libs-devel < 1.4.1.2

%description devel
The vte package contains a terminal widget for GTK+. It's used by
gnome-terminal among other programs.

You should install the vte-devel package if you would like to
compile applications that use the vte terminal widget. You do not need
to install vte-devel if you just want to use precompiled
applications.

%description devel -l pl
Pliki nag³ówkowe potrzebne do kompilowania programów u¿ywaj±cych
vte.

%package static
Summary:	Static VTE library
Summary(pl):	Statyczna biblioteka VTE
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Conflicts:	gnome-libs-static < 1.4.1.2

%description static
Static version of VTE libraries.

%description static -l pl
Statyczna wersja bibliotek VTE.

%package -n python-vte
Summary:	Python VTE module
Summary(pl):	Modu³ VTE dla pythona
Group:		Libraries
%pyrequires_eq	python-libs
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygtk-gtk >= 2:2.9.3

%description -n python-vte
Python VTE library.

%description -n python-vte -l pl
Biblioteka VTE dla pythona.

%package apidocs
Summary:	VTE API documentation
Summary(pl):	Dokumentacja API VTE
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
VTE API documentation.

%description apidocs -l pl
Dokumentacja API VTE.

%prep
%setup -q
%patch0 -p1

%build
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
	LIBS='-ltinfo' \
	--with-xft2 \
	--with-pangox \
	%{?with_glx:--with-glX} \
	--with-default-emulation=xterm \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/*.{la,a}
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ug

%find_lang vte

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f vte.lang
%defattr(644,root,root,755)
%doc NEWS README AUTHORS
%attr(755,root,root) %{_bindir}/vte
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/vte
%attr(755,root,root) %{_libdir}/vte/*
%attr(2755,root,utmp) %{_libdir}/gnome-pty-helper
%{_datadir}/vte

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/*

%files -n python-vte
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/*.so
