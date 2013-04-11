# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       GhostCluster
Summary:    Automotive Meter Cluster Application
Version:    0.2013.4.4
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
mkdir -p %{buildroot}/opt/share/crash/
touch %{buildroot}/opt/share/crash/curbs.log

wrt-installer -i %{_datadir}/GhostCluster/GhostCluster.wgt

# >> install post
# << install post






%files
%defattr(-,root,root,-)
%{_datadir}/GhostCluster
#%{_datadir}/applications/GhostCluster.desktop
#%{_datadir}/pixmaps/GhostCluster.png
# >> files
# << files


