%define _disable_rebuild_configure 1

Summary:	CD ripping tool using GTK+ and GStreamer
Name:		sound-juicer
Version:	3.18.1
Release:	1
License:	GPLv2+
Group:		Sound
URL:		http://www.burtonini.com/blog/computers/sound-juicer
Source0:	http://ftp.gnome.org/pub/GNOME/sources/sound-juicer/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	iso-codes
BuildRequires:	itstool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(libbrasero-media3)
BuildRequires:	pkgconfig(libdiscid)
BuildRequires:	pkgconfig(libmusicbrainz5)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:	gstreamer1.0-plugins-good
BuildRequires:	gstreamer1.0-plugins-base
BuildRequires:	gstreamer1.0-flac
BuildRequires:	gstreamer-tools
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
#for autogen.sh
#BuildRequires:	gettext-devel
#BuildRequires:	gnome-common

Requires:	gstreamer1.0-plugins-bad
Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-cdparanoia
Suggests:	gstreamer1.0-flac
Suggests:	gstreamer1.0-lame
Suggests:	gstreamer1.0-faac

%description
This is Sound Juicer, a CD ripping tool using GTK+ and GStreamer.

%prep
%setup -q

%build
%configure \
	--enable-compile-warnings=no

%make LIBS='-ldbus-1'

%install
%makeinstall_std
%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README ChangeLog
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/sound-juicer
%{_datadir}/icons/hicolor/*/apps/sound-juicer.*
%{_mandir}/man1/%{name}.1*
%{_datadir}/GConf/gsettings/sound-juicer.convert
%{_datadir}/glib-2.0/schemas/org.gnome.sound-juicer.gschema.xml
%{_datadir}/appdata/sound-juicer.appdata.xml
