#
# Conditional build:
%bcond_with	glx # build for glX support
#
Summary:	VTE terminal widget library
Summary(pl):	Biblioteka z kontrolk� terminala VTE
Name:		vte
Version:	0.11.11
Release:	9
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.11/%{name}-%{version}.tar.bz2
# Source0-md5:	4d7a3674df5b8be7f1adffa981c1fc3d
Patch0:		%{name}-keys.patch
Patch1:		%{name}-localenames.patch
Patch2:		%{name}-atktextselection.patch
Patch3:		%{name}-types-include.patch
Patch4:		%{name}-performance.patch
Patch5:		%{name}-nozvt.patch
%{?with_glx:BuildRequires:	OpenGL-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	gtk-doc
BuildRequires:	libart_lgpl-devel >= 2.3.10
BuildRequires:	libtool
BuildRequires:	rpm-pythonprov
BuildRequires:	python-pygtk-devel >= 1.99.13
BuildRequires:	xft-devel >= 2.1.2
Requires(pre):	utempter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The vte package contains a terminal widget for GTK+. It's used by
gnome-terminal among other programs.

%description -l pl
Ten pakiet zawiera kontrolk� terminala dla GTK+. Jest u�ywany przez
gnome-terminal oraz inne programy.

%package devel
Summary:	Headers for VTE
Summary(pl):	Pliki nag��wkowe VTE
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.2.0
Requires:	gtk+2-devel >= 2.2.0
Requires:	libart_lgpl-devel >= 2.3.10
Requires:	OpenGL-devel
Conflicts:	gnome-libs-devel < 1.4.1.2

%description devel
The vte package contains a terminal widget for GTK+. It's used by
gnome-terminal among other programs.

You should install the vte-devel package if you would like to
compile applications that use the vte terminal widget. You do not need
to install vte-devel if you just want to use precompiled
applications.

%description devel -l pl
Pliki nag��wkowe potrzebne do kompilowania program�w u�ywaj�cych
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
Summary(pl):	Modu� VTE dla pythona
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygtk-gtk >= 1.99.13

%description -n python-vte
Python VTE library.

%description -n python-vte -l pl
Biblioteka VTE dla pythona.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p0
%patch5 -p1

mv -f po/{no,nb}.po

%build
glib-gettextize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
CFLAGS="-I/usr/include/ncurses"
%configure \
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
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files -n python-vte
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/*.so
