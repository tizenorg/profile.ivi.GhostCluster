Name:       GhostCluster
Summary:    Automotive Meter Cluster Application
Version:    0.2013.10.16
Release:    1
Group:      Applications/System
License:    Apache 2.0
URL:        http://www.tizen.org
Source0:    %{name}-%{version}.tar.gz
BuildRequires: zip
Requires: crosswalk
Requires: tizen-platform-config

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
source %_sysconfdir/tizen-platform.conf
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/5000/dbus/user_bus_socket"

su app -c "xwalkctl -i /opt/usr/apps/.preinstallWidgets/GhostCluster.wgt"

%postun

su app -c "xwalkctl -u $(su %{MODELLO_INSTALL_USER} -c "xwalkctl" | grep GhostCluster | cut -c 1-32)

%files
%defattr(-,root,root,-)
#%manifest gc.manifest
/opt/usr/apps/.preinstallWidgets/GhostCluster.wgt
