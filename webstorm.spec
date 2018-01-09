Name:          WebStorm
Version:       2017.3.2
Release:       1%{?dist}
Group:         Development/Tools

Summary:       Intelligent Javascript IDE
License:       Commercial
URL:           https://www.jetbrains.com/webstorm/

Source0:       http://download.jetbrains.com/webstorm/%{name}-%{version}.tar.gz

Source101:     webstorm.xml
Source102:     webstorm.desktop
Source103:     webstorm.appdata.xml

BuildRequires: desktop-file-utils
BuildRequires: /usr/bin/appstream-util

ExclusiveArch: x86_64

Requires:      java-devel
BuildRoot:     %{_tmppath}/%{name}-%{version}-root-%(id -u -n)

%description
Powerful IDE for modern JavaScript development

%package doc
Summary:       Documentation for modern Javascript IDE
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}

%description doc
This package contains documentation for modern Javascript IDE.

%prep
%setup -q -n %{name}-%{version}
%setup -q -n %{name}-%{version} -D -T -a 1

%install
mkdir -p %{buildroot}%{_javadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/appdata
mkdir -p %{buildroot}%{_bindir}

cp -arf ./{lib,bin,jre64,help,helpers,plugins} %{buildroot}%{_javadir}/%{name}/

rm -f %{buildroot}%{_javadir}/%{name}/bin/fsnotifier{,-arm}
# this will be in docs
rm -f %{buildroot}%{_javadir}/help/*.pdf
cp -af ./bin/webstorm.png %{buildroot}%{_datadir}/pixmaps/webstorm.png
cp -af %{SOURCE101} %{buildroot}%{_datadir}/mime/packages/%{name}.xml
cp -af %{SOURCE102} %{buildroot}%{_datadir}/webstorm.desktop
cp -a %{SOURCE103} %{buildroot}%{_datadir}/appdata
ln -s %{_javadir}/%{name}/bin/webstorm.sh %{buildroot}%{_bindir}/webstorm
desktop-file-install                          \
--add-category="Development"                  \
--delete-original                             \
--dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/webstorm.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/webstorm.appdata.xml

%files
%{_datadir}/applications/webstorm.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/webstorm.png
%{_datadir}/appdata/webstorm.appdata.xml
%{_javadir}/%{name}
%exclude %{_javadir}/%{name}/jre64
%{_bindir}/webstorm

%files doc
%doc *.txt
%doc help/*.pdf
%license license/

%files jre
%{_javadir}/%{name}/jre64

%changelog
* Thu Dec 14 2017 Ilya Reshetnikov <devxom@users.noreply.github.com> - 2017.3.2
- Updated to 2017.3.2. Initial package.
