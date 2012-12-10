Name:		arx-libertatis
Version:	1.0.3
Release:	1
Summary:	An open source port of Arx Fatalis, a 2002 first-person role-playing game
Group:		Games/Adventure
License:	GPLv3+
URL:		http://arx-libertatis.org/
Source:		http://github.com/downloads/arx/ArxLibertatis/%{name}-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	devil-devel
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(sdl)
BuildRequires:	zlib-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(openal)

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
%makeinstall_std -C build

mv %{buildroot}%{_bindir} %{buildroot}%{_gamesbindir}
mkdir -p %{buildroot}%{_gamesdatadir}/arx

sed -i s\|RolePlaying\|AdventureGame\|g %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc ARX_PUBLIC_LICENSE.txt AUTHORS CHANGELOG README.md
%{_gamesbindir}/arx*
%dir %{_gamesdatadir}/arx
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/arx*.1*
%{_mandir}/man6/arx*.6*


%changelog
* Mon Jun 18 2012 Andrey Bondrov <abondrov@mandriva.org> 1.0.2-1
- New version 1.0.2

* Thu May 31 2012 Andrey Bondrov <abondrov@mandriva.org> 1.0.1-1mdv2012.0
+ Revision: 801450
- Update BuildRequires
- imported package arx-libertatis

