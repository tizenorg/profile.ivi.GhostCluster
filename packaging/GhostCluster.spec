Name:       GhostCluster
Summary:    Automotive Meter Cluster Application
Version:    0.2013.9.16
Release:    1
Group:      Applications/System
License:    Apache 2.0
URL:        http://www.tizen.org
Source0:    %{name}-%{version}.tar.gz
Requires:   automotive-message-broker-plugins-websocket
Requires:   wrt-installer
Requires:   wrt-plugins-ivi
BuildRequires: zip

%description
Example guage cluster for tizen ivi

%prep
%setup -q -n %{name}-%{version}

%build
make widget

%install
rm -rf %{buildroot}

%make_install

%post
if [ -f /opt/usr/apps/.preinstallWidgets/preinstallDone ]; then
    wrt-installer -i /opt/usr/apps/.preinstallWidgets/GhostCluster.wgt;
fi

%files
%defattr(-,root,root,-)
#%manifest gc.manifest
/opt/usr/apps/.preinstallWidgets/GhostCluster.wgt
