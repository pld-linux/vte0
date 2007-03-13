#
# Conditional build:
%bcond_with	glx	# drawing using GLX
#
Summary:	VTE terminal widget library
Summary(pl.UTF-8):	Biblioteka z kontrolką terminala VTE
Name:		vte
Version:	0.16.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/vte/0.16/%{name}-%{version}.tar.bz2
# Source0-md5:	6b85967ba75ed574d0e5782697fbc79f
Patch0:		%{name}-keys.patch
Patch1:		%{name}-link.patch
%{?with_glx:BuildRequires:	OpenGL-GLU-devel}
%{?with_glx:BuildRequires:	OpenGL-GLX-devel}
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1:1.6
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.9
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	python-pygtk-devel >= 2:2.10.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(pre):	utempter
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
%{?with_glx:Requires:	OpenGL-GLU-devel}
Requires:	gtk+2-devel >= 2:2.10.9
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

%package -n python-vte
Summary:	Python VTE module
Summary(pl.UTF-8):	Moduł VTE dla pythona
Group:		Libraries
%pyrequires_eq	python-libs
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygtk-gtk >= 2:2.10.4

%description -n python-vte
Python VTE library.

%description -n python-vte -l pl.UTF-8
Biblioteka VTE dla pythona.

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
%patch0 -p1
%patch1 -p1

%build
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
	--enable-gtk-doc \
	--with-default-emulation=xterm \
	%{?with_glx:--with-glX} \
	--with-html-dir=%{_gtkdocdir} \
	--with-pangox \
	--with-xft2

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/*.{la,a}

%find_lang vte

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f vte.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/vte
%attr(755,root,root) %{_libdir}/libvte.so.*.*.*
%dir %{_libdir}/vte
%attr(755,root,root) %{_libdir}/vte/*
%attr(2755,root,utmp) %{_libdir}/gnome-pty-helper
%{_datadir}/vte

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvte.so
%{_libdir}/libvte.la
%{_includedir}/vte
%{_pkgconfigdir}/vte.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvte.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/vte

%files -n python-vte
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/vtemodule.so
