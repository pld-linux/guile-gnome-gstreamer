Summary:	Guile wrapper for GStreamer library
Summary(pl.UTF-8):	Wrapper Guile dla biblioteki GStreamera
Name:		guile-gnome-gstreamer
Version:	0.9.91
Release:	1
License:	GPL v2+
Group:		Development/Languages/Scheme
Source0:	http://ftp.gnu.org/pub/gnu/guile-gnome/guile-gnome-gstreamer/%{name}-%{version}.tar.gz
# Source0-md5:	5c218bf7c4af91d81d4a3ca553b948f2
URL:		http://www.gnu.org/software/guile-gnome/
BuildRequires:	g-wrap-devel >= 1.9.8
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	guile-gnome-glib-devel >= 2.15.93
BuildRequires:	guile-devel >= 5:1.6.4
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	g-wrap >= 1.9.8
Requires:	guile >= 5:1.6.4
Requires:	guile-gnome-glib >= 2.15.93
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
guile-gnome-gstreamer is a Guile wrapper for GStreamer, a streaming
media framework.

%description -l pl.UTF-8
guile-gnome-gstreamer to wrapper Guile dla GStreamera - szkieletu dla
strumieni multimedialnych.

%prep
%setup -q

%build
%configure \
	--disable-Werror
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/guile-gnome-0/libgw-guile-gnome-*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc gstreamer/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/guile-gnome-0/libgw-guile-gnome-gstreamer.so*
%{_datadir}/guile-gnome-0/gnome/defs/gstreamer.defs
%{_datadir}/guile-gnome-0/gnome/defs/gstreamer-types.defs
%{_datadir}/guile-gnome-0/gnome/gstreamer.scm
%{_datadir}/guile-gnome-0/gnome/gw/gstreamer.scm
%{_datadir}/guile-gnome-0/gnome/gw/gstreamer-spec.scm
%{_datadir}/guile-gnome-0/gnome/overrides/gstreamer.defs*
%{_datadir}/guile-gnome-0/gnome/gstreamer
# devel?
%{_pkgconfigdir}/guile-gnome-gstreamer-0.pc
