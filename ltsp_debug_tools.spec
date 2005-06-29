%define		_arch	i386
%define		_pver	4.1

Summary:	Linux Terminal Server Project - Core system for terminals
Summary(pl):	Podstawowy system dla terminali z Linux Terminal Server Project
Name:		ltsp_debug_tools
Version:	4.0.1
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.ltsp.org/ltsp-utils-0.11.tgz
# Source0-md5:	b17b350b18b04d769fcadcd12885a573
Source1:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-gdb-1.1-0-%{_arch}.tgz
# Source1-md5:	7b606b9f2bb3cec90bc36a6189cc9ed9
Source2:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-strace-1.1-0-%{_arch}.tgz
# Source2-md5:	fc4cb561779f6d70fc5139f054dee8a7
URL:		http://www.ltsp.org/
Requires:	ltsp_core
AutoProv:	0
AutoReq:	0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ltspdir	/home/services/ltsp

%description
LTSP is an add-on package for Linux that allows you to connect lots of
low-powered thin client terminals to a Linux server. Applications
typically run on the server and accept input and display their output
on the thin client display. LTSP is available as a set of packages that
can be installed on any Linux system.

This package contains debug tools for LTSP terminals.

%description -l pl
- Jak obni¿yæ koszty I ocaliæ planetê?
- Przekszta³ciæ te stare pecety na X-terminale z u¿yciem LTSP.

Ten pakiet zawiera narzêdzia dla terminali LTSP.

%prep
%setup -q -n ltsp-utils

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ltspdir}
tar zxf %{SOURCE1}
tar zxf %{SOURCE2}
cd i386
cp -r {bin,lib,share} $RPM_BUILD_ROOT%{_ltspdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc README
%dir %{_ltspdir}
%attr(755,root,root) %{_ltspdir}/bin
%attr(755,root,root) %{_ltspdir}/lib
%{_ltspdir}/share
