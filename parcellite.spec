Summary:	Lightweight GTK+ clipboard manager
Name:		parcellite
Version:	1.1.9
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/parcellite/%{name}-%{version}.tar.gz
# Source0-md5:	6c3b70165c2dee9341a81a2a8481e446
URL:		http://parcellite.sourceforge.net/
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lightweight GTK+ clipboard manager.

%prep
%setup -q

%{__sed} -i "s|GNOME;Application;||" data/parcellite.desktop.in

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/pl_PL

%find_lang %{name}

desktop-file-validate $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/parcellite-startup.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/parcellite.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/parcellite
%{_sysconfdir}/xdg/autostart/parcellite-startup.desktop
%{_desktopdir}/parcellite.desktop
%{_pixmapsdir}/parcellite.png
%{_mandir}/man1/parcellite.1*

