Summary:	VTE terminal widget library
Summary(pl.UTF-8):	Biblioteka z kontrolką terminala VTE
Name:		vte
Version:	0.29.1
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/vte/0.29/%{name}-%{version}.tar.xz
# Source0-md5:	91cd70995099ca7e534654e0679ab5a7
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.28.0
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
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-common = %{version}-%{release}
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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
	--enable-introspection \
	--with-default-emulation=xterm \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la \

%find_lang %{name}-2.90

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
