Name:		arx-libertatis
Version:	1.0.1
Release:	%mkrel 1
Summary:	An open source port of Arx Fatalis, a 2002 first-person role-playing game
Group:		Games/Adventure
License:	GPLv3+
URL:		http://arx-libertatis.org/
Source:		https://github.com/downloads/arx/ArxLibertatis/%{name}-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	devil-devel
BuildRequires:	glew-devel
BuildRequires:	mesagl-devel
BuildRequires:	png-devel
BuildRequires:	qt4-devel
BuildRequires:	SDL-devel
BuildRequires:	zlib-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(xrender) >= 0.9.6


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

%prep
%setup -q

%build
%setup_compile_flags
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DCMAKE_INSTALL_LIBEXECDIR:PATH=%{_bindir}
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%__mv %{buildroot}%{_bindir} %{buildroot}%{_gamesbindir}
%__mkdir_p %{buildroot}%{_gamesdatadir}/arx

%__sed -i s\|RolePlaying\|AdventureGame\|g %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
%__rm -rf %{buildroot}

%files
%doc ARX_PUBLIC_LICENSE.txt AUTHORS CHANGELOG README.md
%{_gamesbindir}/arx*
%dir %{_gamesdatadir}/arx
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/arx*.1*
%{_mandir}/man6/arx*.6*

