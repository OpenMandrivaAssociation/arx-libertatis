Summary:	An open source port of Arx Fatalis, a 2002 first-person role-playing game
Name:		arx-libertatis
Version:	1.1.2
Release:	2
License:	GPLv3+
Group:		Games/Adventure
Url:		http://arx-libertatis.org/
Source0:	http://github.com/downloads/arx/ArxLibertatis/%{name}-%{version}.tar.xz
# Use current screen resolution by default because sometimes max resolution
# is not detected properly and the game doesn't start
Patch0:		arx-libertatis-1.1.1-default-resolution.patch
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	devil-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(zlib)

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
%doc ARX_PUBLIC_LICENSE.txt AUTHORS CHANGELOG README.md
%{_gamesbindir}/arx*
%dir %attr(777,-,-) %{_gamesdatadir}/arx
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/arx*.1*
%{_mandir}/man6/arx*.6*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%cmake \
	-DCMAKE_INSTALL_LIBEXECDIR:PATH=%{_bindir} \
	-DUSE_QT5:BOOL=OFF
%make

%install
%makeinstall_std -C build

mv %{buildroot}%{_bindir} %{buildroot}%{_gamesbindir}
mkdir -p %{buildroot}%{_gamesdatadir}/arx

sed -i s\|RolePlaying\|AdventureGame\|g %{buildroot}%{_datadir}/applications/%{name}.desktop

