%define _disable_rebuild_configure 1

Summary:	CD ripping tool using GTK+ and GStreamer
Name:		sound-juicer
Version:	3.38.0
Release:	1
License:	GPLv2+
Group:		Sound
URL:		http://www.burtonini.com/blog/computers/sound-juicer
Source0:	http://ftp.gnome.org/pub/GNOME/sources/sound-juicer/3.38/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(iso-codes)
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
BuildRequires:	meson

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
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

rm -Rf %{buildroot}%{_prefix}/doc/%{name}

%files -f %{name}.lang
%doc README.md NEWS
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/sound-juicer
%{_datadir}/icons/hicolor/*/apps/org.gnome.SoundJuicer.*
%{_mandir}/man1/%{name}.1*
%{_datadir}/GConf/gsettings/sound-juicer.convert
%{_datadir}/glib-2.0/schemas/org.gnome.sound-juicer.gschema.xml
%{_datadir}/metainfo/*.xml
%{_datadir}/dbus-1/services/org.gnome.SoundJuicer.service
