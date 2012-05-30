# 
# 

%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
Name:       python-yaml
Summary:    YAML parser and emitter for Python
Version:    3.09
Release:    1
Group:      Development/Libraries
License:    MIT
URL:        http://pyyaml.org/
Source0:    http://pyyaml.org/download/pyyaml/PyYAML-%{version}.tar.gz
Source1001: packaging/python-yaml.manifest 
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Provides:   PyYAML
Obsoletes:   PyYAML


%description
YAML is a data serialization format designed for human readability and
interaction with scripting languages.  PyYAML is a YAML parser and
emitter for Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages.  PyYAML
supports standard YAML tags and provides Python-specific tags that allow
to represent an arbitrary Python object.

PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistance.




%prep
%setup -q -n PyYAML-%{version}


%build
cp %{SOURCE1001} .

CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%if 0%{?suse_version}
%{__python} setup.py install --root=$RPM_BUILD_ROOT --prefix=%{_prefix}
%else
%{__python} setup.py install --root=$RPM_BUILD_ROOT -O1 --prefix=%{_prefix}
%endif







%files
%manifest python-yaml.manifest
%defattr(-,root,root,-)
%doc PKG-INFO README LICENSE examples
%{python_sitearch}/*


