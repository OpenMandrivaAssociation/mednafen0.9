%define Werror_cflags %nil
%define oname mednafen
Name:			mednafen0.9
Version:		0.9.22pre1
Release:		%mkrel 1

Summary:	Multi-consoles Emulator
License:	GPLv2+
URL:		http://mednafen.sourceforge.net/
Group:		Emulators
Source0:	http://downloads.sourceforge.net/%{oname}/%{oname}-0.9.22-wip.tar.bz2
Patch0:		mednafen-9.17.1-formatfix.patch
BuildRequires:	libcdio-devel
BuildRequires:	libvorbis-devel
BuildRequires:	SDL_net-devel
BuildRequires:	libsndfile-devel
BuildRequires:	zlib-devel
BuildRequires:	bison
BuildRequires:	SDL-devel
%if %mdkversion >= 200700
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
%else
BuildRequires:	X11-devel
BuildRequires:	MesaGLU-devel
%endif
BuildRoot:	%{_tmppath}/%{oname}-%{version}

%description
Mednafen emulates several consoles :
-Atari Lynx
-GameBoy (Color)
-GameBoy Advance
-Neo Geo Pocket (Color)
-NES
-SNES
-PC Engine (TurboGrafx 16)
-PC-FX
-Sega Master System & Game Gear
-SuperGrafx
-Virtual Boy
-WonderSwan (Color)

%prep
%setup -q -n %{oname}
# %patch0 -p1
find ./src -type f -exec chmod 644 '{}' +
find ./src -type d -exec chmod 755 '{}' +

%build
autoreconf -i
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall
%find_lang %{oname}
mv %{buildroot}/%{_bindir}/%{oname} %{buildroot}/%{_bindir}/%{oname}0.9

%files -f %{oname}.lang
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog INSTALL TODO Documentation/*
%attr(0755,root,root) %{_bindir}/%{oname}0.9
%{_datadir}/mednafen/c68k_op0.inc
%clean
rm -rf %{buildroot}

