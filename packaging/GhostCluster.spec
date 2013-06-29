# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       GhostCluster
Summary:    Automotive Meter Cluster Application
Version:    0.2013.6.28
Release:    1
Group:      Applications/System
License:    Apache 2.0
URL:        http://www.tizen.org
Source0:    %{name}-%{version}.tar.gz
Requires:   automotive-message-broker-plugins-websocket
Requires:   wrt-installer
BuildRequires: zip

%description
Example guage cluster for tizen ivi

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre


make widget


# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre

%make_install

%post
if [ -f /opt/usr/apps/.preinstallWidgets/preinstallDone ]; then
    wrt-installer -i /opt/usr/apps/.preinstallWidgets/GhostCluster.wgt;
fi

# >> install post
# << install post






%files
%defattr(-,root,root,-)
/opt/usr/apps/.preinstallWidgets/GhostCluster.wgt
# >> files
# << files


