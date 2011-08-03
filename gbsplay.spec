%define name gbsplay
%define version 0.0.91
%define release %mkrel 2

Summary: Gameboy Music Player
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.cgarbs.de/stuff/%{name}-%{version}.tar.gz
URL: http://www.cgarbs.de/gbsplay.en.html
License: GPL
Group: Sound
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: xmms
BuildRequires: xmms-devel
BuildRequires: nas-devel
BuildRequires: glib2-devel
BuildRequires: splint

%description
This is a Gameboy sound player, it includes both a command line player
and a xmms plugin.

%prep
%setup -q

%build
./configure --with-xmmsplugin
%make prefix=%{_prefix} localedir=%{_datadir}/locale

%install
rm -rf %{buildroot} installed-docs
%makeinstall XMMS_INPUT_PLUGIN_DIR=%{buildroot}%{_libdir}/xmms/Input man1dir=%{buildroot}%{_mandir}/man1 man5dir=%{buildroot}%{_mandir}/man5 docdir=installed-docs localedir=%{buildroot}%{_datadir}/locale
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc installed-docs/*
%_bindir/gbsinfo
%_bindir/gbsplay
%_libdir/xmms/Input/gbsxmms.so
%_mandir/man1/gbsinfo.1*
%_mandir/man1/gbsplay.1*
%_mandir/man5/gbsplayrc.5*

