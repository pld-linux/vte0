Summary:	VTE terminal widget library
Summary(pl.UTF-8):	Biblioteka z kontrolką terminala VTE
Name:		vte
Version:	0.27.3
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/vte/0.27/%{name}-%{version}.tar.bz2
# Source0-md5:	fa241fdb9c3ea52622c570a4be705093
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.22.0
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection-devel >= 0.6.7
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc >= 1.13
BuildRequires:	gtk-doc-automake
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
#BuildRequires:	python-pygtk-devel >= 2:2.12.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.592
Requires(pre):	utempter
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
Requires:	glib2-devel >= 1:2.22.0
Requires:	gtk+3-devel
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

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/en@shaw

%find_lang %{name}-2.90

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%glib_compile_schemas

%postun
/sbin/ldconfig
%glib_compile_schemas

%files -f vte-2.90.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/vte2_90
%attr(755,root,root) %{_libdir}/libvte2_90.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvte2_90.so.9
%{_libdir}/girepository-1.0/Vte-2.90.typelib
%attr(2755,root,utmp) %{_libdir}/gnome-pty-helper
%{_datadir}/vte
%{_datadir}/glib-2.0/schemas/org.gnome.vte.v0.enums.xml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvte2_90.so
%{_libdir}/libvte2_90.la
%{_includedir}/vte-2.90
%{_pkgconfigdir}/vte-2.90.pc
%{_datadir}/gir-1.0/Vte-2.90.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libvte2_90.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/vte-2.90
