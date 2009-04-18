Name:    quassel
Summary: QT4 Based distrubuted IRC system
Version: 0.4.1
Release: 1%{?dist}

License: GPLv2 or GPLv3
Group:	 Applications/Internet
URL:     http://quassel-irc.org/
Source0: http://quassel-irc.org/system/files/quassel-%{version}.tar.bz2
Source1: %{name}.desktop
Source2: %{name}core.desktop
Source3: %{name}client.desktop
Source4: %{name}.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: qt-sqlite, openssl
BuildRequires: qt-devel, openssl-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils

%description
Quassel IRC is a modern, distributed IRC client, 
meaning that one (or multiple) client(s) can attach 
to and detach from a central core -- 
much like the popular combination of screen and a 
text-based IRC client such as WeeChat, but graphical

%package core
Summary: Quassel core component
Group: Applications/Internet
%description core
The Quassel IRC Core maintains a connection with the 
server, and allows for multiple clients to connect

%package client
Summary: Quassel client
Group: Applications/Internet
%description client
Quassel client 

%prep
%setup -q -n quassel-%{version}

%build

mkdir build
cd build
cmake .. -DWANT_MONO=1 
make 

%install
rm -rf %{buildroot}
cd build
install -d -m755 %{buildroot}%{_bindir}
install -m755 quassel %{buildroot}%{_bindir}
install -m755 quasselclient %{buildroot}%{_bindir}
install -m755 quasselcore %{buildroot}%{_bindir}
%{__install} -p -D %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

desktop-file-install --vendor="fedora" --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}
desktop-file-install --vendor="fedora" --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2}
desktop-file-install --vendor="fedora" --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE3}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/quassel
%doc COPYING gpl-2.0.txt gpl-3.0.txt README
%{_datadir}/applications/fedora-quassel.desktop
%attr(644,root,root) %{_datadir}/pixmaps/quassel.png

%files core
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/quasselcore
%doc COPYING gpl-2.0.txt gpl-3.0.txt README
%{_datadir}/applications/fedora-quasselcore.desktop
%attr(644,root,root) %{_datadir}/pixmaps/quassel.png

%files client
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/quasselclient
%doc COPYING gpl-2.0.txt gpl-3.0.txt README
%{_datadir}/applications/fedora-quasselclient.desktop
%attr(644,root,root) %{_datadir}/pixmaps/quassel.png

%changelog
* Tue Apr 16 2009 Nicolas Doualot <public@slubman.info> - 0.4.1-1
- New upstream release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Steven M. Parirsh <tuxbrewr@fedoraproject.org> 0.4.0-1
- New upstream release

* Mon Dec 29 2008 Steven M. Parrish <tuxbrewr@fedoraproject.org> 0.3.1-2
- Fix bug #477850

* Fri Nov 28 2008 Steven M. Parrish <smparrish@shallowcreek.net> 0.3.1-1
- New upstream release

* Wed Nov 12 2008 Steven M. Parrish <smparrish@shallowcreek.net> 0.3.0.3-1
- New upstream release fixes a security issue with CTCP handling in 
- Quassel Core, that could potentially be exploited to send 
- arbitrary IRC commands on your behalf.

* Tue Sep 16 2008 Steven M. Parrish <smparrish@shallowcreek.net> 0.3.0.1-1
- New upstream release

* Fri Jul 04 2008 Steven Parrish <smparrish@shallowcreek.net> 0.1.rc1
- New upstream release.  Now uses cmake instead of qmake

* Wed Jul 02 2008 Steven Parrish <smparrish@shallowcreek.net> - 0.3.beta1
- Final spec for initial release to F9 and rawhide

* Tue Jun 24 2008 Steven Parrish <smparrish[at]shallowcreek.net>
- Revised spec file based on comments from package reviewer. 

* Mon Jun 23 2008 Steven Parrish <smparrish[at]shallowcreek.net>
- initial RPM
