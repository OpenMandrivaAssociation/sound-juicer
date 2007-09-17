Summary: CD ripping tool using GTK+ and GStreamer
Name: sound-juicer
Version: 2.20.0
Release: %mkrel 1
License: GPL
Group: Sound
URL: http://www.burtonini.com/blog/computers/sound-juicer
Source0: http://ftp.gnome.org/pub/GNOME/sources/sound-juicer/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: librsvg
BuildRequires: libmusicbrainz-devel >= 2.0.0
BuildRequires: libgnomeui2-devel
BuildRequires: libglade2.0-devel
BuildRequires: libgstreamer-plugins-base-devel >= 0.8
BuildRequires: libnautilus-burn-devel >= 2.13.93
BuildRequires: gnome-media >= 2.13.7
BuildRequires: libcdio-devel
BuildRequires: scrollkeeper
BuildRequires: hal-devel
BuildRequires: libcddb-slave2-devel
BuildRequires: gnome-doc-utils
BuildRequires: perl-XML-Parser
BuildRequires: taglib-devel
BuildRequires: desktop-file-utils
BuildRequires: gnome-common intltool
Requires(post): scrollkeeper
Requires(postun): scrollkeeper
Requires: gstreamer0.10-plugins-good
Requires: gstreamer0.10-gnomevfs
Requires: gstreamer0.10-cdparanoia
Suggests: gstreamer0.10-vorbis
Suggests: gstreamer0.10-flac
Suggests: gstreamer0.10-lame
Suggests: gstreamer0.10-faac

%description
This is Sound Juicer, a CD ripping tool using GTK+ and GStreamer.

%prep
%setup -q

%build

%configure2_5x --enable-hal --disable-scrollkeeper --enable-taglib

make

%install
rm -rf $RPM_BUILD_ROOT

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std 

%find_lang %{name} --with-gnome


# menu entry
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):\
	needs="X11" \
	section="Multimedia/Sound" \
	title="Sound Juicer CD Ripper" \
	longtitle="Rip music from your CDs" \
	command="%{_bindir}/sound-juicer" \
	icon="sound-juicer.png" \
	startup_notify="true" xdg="true"
EOF
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

# icons
mkdir -p %buildroot%_liconsdir
rsvg -w 48 -h 48 data/sound-juicer.svg $RPM_BUILD_ROOT%{_liconsdir}/sound-juicer.png
rsvg -w 32 -h 32 data/sound-juicer.svg $RPM_BUILD_ROOT%{_iconsdir}/sound-juicer.png
install -D -m 644 data/sound-juicer-16.png $RPM_BUILD_ROOT%{_miconsdir}/sound-juicer.png

for omf in %buildroot%_datadir/omf/*/*-{??,??_??}.omf;do
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed s!%buildroot!!)" >> %name.lang
done


%clean
rm -rf $RPM_BUILD_ROOT

%post
%post_install_gconf_schemas %name
%{update_menus}
%update_scrollkeeper
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas %name

%postun
%{clean_menus}
%clean_scrollkeeper
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README ChangeLog
%{_sysconfdir}/gconf/schemas/sound-juicer.schemas
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/sound-juicer
%_datadir/icons/hicolor/*/apps/sound-juicer.*
%_mandir/man1/%name.1*
%{_menudir}/*
%{_liconsdir}/*.png
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%dir %{_datadir}/omf/*
%{_datadir}/omf/*/*-C.omf
