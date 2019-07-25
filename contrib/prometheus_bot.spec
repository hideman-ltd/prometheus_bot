Name:           prometheus-bot
Version:        1.%{_git_ver}
Release:        %{_git_hash}.el7
Summary:        This bot is designed to alert messages from alertmanager to Telegram chats.
License:        MIT License
BuildArch:      x86_64
Group:          Unspecified
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
This bot is designed to alert messages from alertmanager to Telegram chats.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/bin
install -d $RPM_BUILD_ROOT/etc/%{name}
install -d $RPM_BUILD_ROOT/etc/systemd/system

install -D -m 644 contrib/config.yml $RPM_BUILD_ROOT/etc/%{name}/
install -D -m 644 contrib/hideman.tmpl $RPM_BUILD_ROOT/etc/%{name}/
install -D -m 644 contrib/%{name}.service $RPM_BUILD_ROOT/etc/systemd/system/
install -D -m 755 prometheus_bot $RPM_BUILD_ROOT/usr/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config /etc/%{name}/config.yml
%config /etc/%{name}/hideman.tmpl
/etc/systemd/system/%{name}.service
/usr/bin/prometheus_bot
