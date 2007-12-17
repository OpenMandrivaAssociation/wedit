%define name wedit
%define version 0.9.8
%define release %mkrel 6

Summary: 	User-friendly IDE
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}-libc6-src.tar.bz2
License: 	GPL
URL: 		http://www.q-software-solutions.com/weditlinux/
Group: 		Development/Other
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
mkdir -p ./usr/lib/menu
cat > ./usr/lib/menu/%{name} <<EOF
?package(%{name}):\
command="/usr/bin/wedit"\
title="Wedit"\
longtitle="User-friendly IDE"\
needs="x11"\
icon="development_environment_section.png"\
section="Applications/Development/Development Environments"
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
%{_menudir}/*

