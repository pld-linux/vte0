
%include        /usr/lib/rpm/macros.python

Summary:	VTE terminal widget library
Summary(pl):	Biblioteka z kontrolk± terminala VTE
Name:		vte
Version:	0.11.6
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.11/%{name}-%{version}.tar.bz2
Patch0:		%{name}-keys.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	Xft-devel >= 2.1-2
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libart_lgpl-devel >= 2.3.10
BuildRequires:	libtool
BuildRequires:  rpm-pythonprov
BuildRequires:	python-pygtk-devel >= 1.99.13
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
Requires:	%{name} = %{version}
Requires:	glib2-devel >= 2.2.0
Requires:	gtk+2-devel >= 2.2.0
Requires:	libart_lgpl-devel >= 2.3.10
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
Requires:	%{name}-devel = %{version}
Conflicts:	gnome-libs-static < 1.4.1.2

%description static
Static version of VTE libraries.

%description static -l pl
Statyczna wersja bibliotek VTE.

%package -n python-vte
Summary:	Python VTE module
Summary(pl):	Modu³ VTE dla pythona
Group:		Libraries
Requires:	%{name} = %{version}

%description -n python-vte
Python VTE library.

%description -n python-vte -l pl
Biblioteka VTE dla pythona.

%prep
%setup -q
%patch0 -p1

%build
glib-gettextize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
CFLAGS="-I/usr/include/ncurses"
LDFLAGS="-lncurses"
%configure \
	--enable-gtk-doc \
	--with-html-path=%{_gtkdocdir} 
	
%{__make} pythonsiteexecdir=%{py_sitedir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	pythonsiteexecdir=%{py_sitedir} \
	HTML_DIR=%{_gtkdocdir}

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
%attr(755,root,root) %{py_sitedir}/*.so
