#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-airbase
Version  : 78
Release  : 1
URL      : https://github.com/airlift/airbase/archive/78.tar.gz
Source0  : https://github.com/airlift/airbase/archive/78.tar.gz
Source1  : https://repo1.maven.org/maven2/io/airlift/airbase/78/airbase-78.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-airbase-data = %{version}-%{release}

%description
# Airbase
[![Maven Central](https://img.shields.io/maven-central/v/io.airlift/airbase.svg?label=Maven%20Central)](https://search.maven.org/#search%7Cga%7C1%7Cg%3A%22io.airlift%22%20AND%20a%3A%22airbase%22)
[![Build Status](https://travis-ci.org/airlift/airbase.svg?branch=master)](https://travis-ci.org/airlift/airbase)

%package data
Summary: data components for the mvn-airbase package.
Group: Data

%description data
data components for the mvn-airbase package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/airlift/airbase/78
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/io/airlift/airbase/78


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/io/airlift/airbase/78/airbase-78.pom