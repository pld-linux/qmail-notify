Summary:	Delayed delivery notification for qmail
Summary(pl):	Powiadamianie o opó¼nionym dostarczaniu poczty dla qmaila
Name:		qmail-notify
Version:	0.93
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://untroubled.org/qmail-notify/%{name}-%{version}.tar.gz
# Source0-md5:	5afe9ac9fac10e999a278c78f17e31b0
Source1:	%{name}.1
URL:		http://untroubled.org/qmail-notify/
Requires:	qmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a program to notify senders about email that has
been held in the qmail queue.

%description -l pl
Ten pakiet zawiera program informuj±cy nadawców o poczcie, która
utkwi³a w kolejce qmaila.

%prep
%setup -q

%build
echo %{_bindir} >conf-bin
echo "%{__cc} %{rpmcflags}" >conf-cc
echo "%{__cc} %{rpmldflags}" >conf-ld
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

echo $RPM_BUILD_ROOT%{_bindir} >conf-bin
rm -f installer instcheck conf_bin.c insthier.o
%{__make} installer instcheck
./installer
./instcheck

install -d $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 cron.hourly $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly/qmail-notify
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README
%config /etc/cron.hourly/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
