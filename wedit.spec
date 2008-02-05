%define name wedit
%define version 0.9.8
%define release %mkrel 7

Summary: 	User-friendly IDE
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}-libc6-src.tar.bz2
License: 	GPL
URL: 		http://www.q-software-solutions.com/weditlinux/
Group: 		Development/Other
Buildroot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	gtk+-devel >= 1.2

%description
User-friendly IDE with many advanced features like real-time code parsing,
auto-complete and more 
Project wizard, automatic generation of GNU makefiles and Automake/Autoconf
skeletons 
Powerful search and grep capabilities, change-tracking and visual diff 
Drag & drop 
Fully supports GNU C and LCC compilers, customizable makefile generation and 
build. 
Fast run-time source parsing supports syntax coloring and autoformating of C, 
Fortran, and Eiffel sources. 
Complete analysis of source code and object files, many charts and plots 
Intergated debugger that allows local or remote debugging 

%prep
rm -rf $RPM_BUILD_ROOT

%setup -n %{name}-%{version}

%build

%configure

sed -e s/"-O2 -w"/"\${RPM_OPT_FLAGS}"/ src/Makefile > src/Makefile.new
rm -f src/Makefile
mv src/Makefile.new src/Makefile

%make

%install

make DESTDIR=$RPM_BUILD_ROOT install

(cd $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=/usr/bin/wedit
Name=Wedit
Comment=User-friendly IDE
Icon=development_environment_section
Categories=Development;IDE / GUIDesigner;
EOF
)
 
%post
%update_menus
 
%postun
%clean_menus

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc AUTHORS INSTALL COPYING NEWS README ChangeLog
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-*.desktop

