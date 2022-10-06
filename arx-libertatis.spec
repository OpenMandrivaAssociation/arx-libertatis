Summary:	An open source port of Arx Fatalis, a 2002 first-person role-playing game
Name:		arx-libertatis
Version:	1.2.1
Release:	1
License:	GPLv3+
Group:		Games/Adventure
Url:		http://arx-libertatis.org/
Source0:	https://github.com/arx/ArxLibertatis/releases/download/%{version}/arx-libertatis-%{version}.tar.xz
Patch0:		arx-libertatis-link-curl.patch
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	boost-devel
BuildRequires:	devil-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)

%description
Arx Libertatis is a cross-platform, open source port of Arx Fatalis,
a 2002 first-person role-playing game developed by Arkane Studios.

Arx Fatalis features crafting, melee and ranged combat, as well as a
unique casting system where the player draws runes in real time to
effect the desired spell.

The Arx Libertatis source code is based on the publicly released Arx Fatalis
sources and available under the GPL 3+ license. This does however not include
the game data, so you need to obtain a copy of the original Arx Fatalis or
it's demo to play Arx Libertatis.

%files
%doc AUTHORS CHANGELOG README.md
%{_gamesbindir}/arx*
%dir %attr(777,-,-) %{_gamesdatadir}/arx
%{_datadir}/applications/%{name}.desktop
%{_datadir}/games/arx/*
%{_mandir}/man1/arx*.1*
%{_mandir}/man6/arx*.6*
%{_includedir}/ArxIO.h
%{_libdir}/libArxIO.so*
%{_datadir}/blender/scripts/addons/arx
%{_datadir}/icons/*/*/*/arx-libertatis.*

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake \
	-DCMAKE_INSTALL_LIBEXECDIR:PATH=%{_bindir} \
	-DUSE_QT5:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

mv %{buildroot}%{_bindir} %{buildroot}%{_gamesbindir}
mkdir -p %{buildroot}%{_gamesdatadir}/arx

sed -i s\|RolePlaying\|AdventureGame\|g %{buildroot}%{_datadir}/applications/%{name}.desktop
