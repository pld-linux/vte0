# TODO:
# - fix gtk-doc location
%define		gtk2_version		2.0.3
%define		glib2_version		2.0.3
%define		libart_lgpl_version	2.3.8

Summary:	VTE terminal widget library
Summary(pl):	Biblioteka z widgetem terminala VTE
Name:		vte
Version:	0.10.3
Release:	0.1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/%{name}/0.10/%{name}-%{version}.tar.bz2
Patch0:		%{name}-Xft2.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= %{glib2_version}
BuildRequires:	gtk+2-devel >= %{gtk2_version}
BuildRequires:	libart_lgpl-devel >= %{libart_lgpl_version}
BuildRequires:	libtool
BuildRequires:	gnome-common
BuildRequires:	python-pygtk-devel >= 1.99.13
Requires(pre):	utempter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The vte package contains a terminal widget for GTK+. It's used by
gnome-terminal among other programs.

%description -l pl
Ten pakiet zawiera widget terminala dla GTK+. Jest u¿ywany przez
gnome-terminal oraz inne programy.

%package devel
Summary:	Headers for vte
Summary(pl):	Pliki nag³ówkowe vte
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	glib2-devel >= %{glib2_version}
Requires:	gtk+2-devel >= %{gtk2_version}
Requires:	libart_lgpl-devel >= %{libart_lgpl_version}
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
Summary:	Static vte library
Summary(pl):	Statyczna biblioteka vte
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}
Conflicts:	gnome-libs-static < 1.4.1.2

%description static
Static version of vte libraries.

%description static -l pl
Statyczna wersja bibliotek vte.

%prep
%setup -q

%build
#rm -f missing
#%{__libtoolize}
#%{__aclocal} -I %{_aclocaldir}/gnome2-macros
#%{__autoconf}
#%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}


%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README AUTHORS
%attr(755,root,root) %{_bindir}/vte
%attr(755,root,root) %{_libdir}/lib*.so.*.*
# FIXME: move to proper place
#%{_libdir}/python*
%dir %{_libdir}/vte
%attr(755,root,root) %{_libdir}/vte/*
%attr(2755,root,utmp) %{_libdir}/gnome-pty-helper

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
