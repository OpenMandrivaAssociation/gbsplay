Summary:	Gameboy Music Player
Name:		gbsplay
Version:	0.0.91
Release:	3
License:	GPL
Group:		Sound
URL:		http://www.cgarbs.de/gbsplay.en.html
Source0:	http://www.cgarbs.de/stuff/%{name}-%{version}.tar.gz
BuildRequires:	nas-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	splint

%description
This is a Gameboy sound player.

%prep
%setup -q

%build
./configure
%make prefix=%{_prefix} localedir=%{_datadir}/locale

%install
%makeinstall \
		man1dir=%{buildroot}%{_mandir}/man1 \
        man5dir=%{buildroot}%{_mandir}/man5 \
        docdir=installed-docs \
        localedir=%{buildroot}%{_datadir}/locale

%find_lang %{name}

%files -f %{name}.lang
%doc installed-docs/*
%{_bindir}/gbsinfo
%{_bindir}/gbsplay
%{_mandir}/man1/gbsinfo.1*
%{_mandir}/man1/gbsplay.1*
%{_mandir}/man5/gbsplayrc.5*

%changelog
* Wed Aug 03 2011 Andrey Bondrov <abondrov@mandriva.org> 0.0.91-2mdv2012.0
+ Revision: 693058
- imported package gbsplay


* Mon Sep  1 2008 Götz Waschk <goetz@zarb.org> 0.0.91-1plf2009.0
- update build deps
- fix build
- new version

* Mon Jul 14 2008 Götz Waschk <goetz@zarb.org> 0.0.9-1plf2009.0
- new version

* Mon Jan 21 2008 Götz Waschk <goetz@zarb.org> 0.0.8-4plf2008.1
- fix plf reason

* Mon Aug 28 2006 Götz Waschk <goetz@zarb.org> 0.0.8-3plf2007.0
- rebuild

* Sun Jan 22 2006 Götz Waschk <goetz@zarb.org> 0.0.8-2plf
- mkrel

* Sun Jan 22 2006 GÃ¶tz Waschk <goetz@zarb.org> 0.0.8-1plf
- New release 0.0.8

* Mon Sep 20 2004 Götz Waschk <goetz@zarb.org> 0.0.7-2plf
- rebuild

* Sat Jul 17 2004 Götz Waschk <goetz@plf.zarb.org> 0.0.7-1plf
- new version

* Wed Apr 28 2004 Götz Waschk <goetz@plf.zarb.org> 0.0.6-1plf
- fix description
- fix buildrequires
- fix source URL
- new version

* Sun Jan 18 2004 Götz Waschk <goetz@plf.zarb.org> 0.0.5-1plf
- fix installation
- drop the patch
- new version

* Sun Jan 18 2004 Götz Waschk <goetz@plf.zarb.org> 0.0.4-2plf
- fix i18n

* Mon Jan  5 2004 Götz Waschk <goetz@plf.zarb.org> 0.0.4-1plf
- add locale files
- drop patch
- new version

* Mon Dec  8 2003 Götz Waschk <goetz@plf.zarb.org> 0.0.3-1plf
- initial package
