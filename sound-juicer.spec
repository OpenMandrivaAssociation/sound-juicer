Summary:	CD ripping tool using GTK+ and GStreamer
Name:		sound-juicer
Version:	3.4.0
Release:	2
License:	GPLv2+
Group:		Sound
URL:		http://www.burtonini.com/blog/computers/sound-juicer
Source0:	http://ftp.gnome.org/pub/GNOME/sources/sound-juicer/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(libbrasero-media3)
BuildRequires:	pkgconfig(libmusicbrainz3)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(gstreamer-pbutils-0.10)
#for autogen.sh
#BuildRequires:	gettext-devel
#BuildRequires:	gnome-common

Requires:	gstreamer0.10-plugins-bad
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-gnomevfs
Requires:	gstreamer0.10-cdparanoia
Suggests:	gstreamer0.10-vorbis
Suggests:	gstreamer0.10-flac
Suggests:	gstreamer0.10-lame
Suggests:	gstreamer0.10-faac

%description
This is Sound Juicer, a CD ripping tool using GTK+ and GStreamer.

%prep
%setup -q

%build
%configure2_5x \
	--disable-scrollkeeper \
	--disable-schemas-install

%make LIBS='-ldbus-1'

%install
%makeinstall_std
%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README ChangeLog
%{_sysconfdir}/gconf/schemas/sound-juicer.schemas
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/sound-juicer
%{_datadir}/icons/hicolor/*/apps/sound-juicer.*
%{_mandir}/man1/%{name}.1*
