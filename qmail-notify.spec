Name:		qmail-notify
Summary:	Delayed delivery notification for qmail
Version:	0.93
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://em.ca/~bruceg/qmail-notify/0.93/%{name}-%{version}.tar.gz
Source1:	%{name}.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://em.ca/~bruceg/qmail-notify/
Requires:	qmail

%description
This package contains a program to notify senders about email that has
been held in the qmail queue.

%description -l pl
Ten pakiet zawiera program informuj±cy u¿ytkowników o ich poczcie,
która jest w kolejce qmaila.

%prep
%setup -q
echo %{_bindir} >conf-bin
echo gcc "%{optflags}" >conf-cc
echo gcc -s >conf-ld

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}
echo $RPM_BUILD_ROOT%{_bindir} >conf-bin
rm -f installer instcheck conf_bin.c insthier.o
%{__make} installer instcheck
./installer
./instcheck

install -d $RPM_BUILD_ROOT/%{_sysconfdir}/cron.hourly
install -d $RPM_BUILD_ROOT/%{_mandir}/man1/
install -m 755 cron.hourly $RPM_BUILD_ROOT/%{_sysconfdir}/cron.hourly/qmail-notify
install %{SOURCE1} $RPM_BUILD_ROOT/%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README
%config /etc/cron.hourly/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_mandir}/man1/*
