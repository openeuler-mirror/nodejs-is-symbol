%{?nodejs_find_provides_and_requires}
Name:                nodejs-is-symbol
Version:             1.0.2
Release:             1
Summary:             Determine if a value is an ES6 Symbol or not
License:             MIT
URL:                 https://github.com/ljharb/is-symbol
Source0:             https://registry.npmjs.org/is-symbol/-/is-symbol-%{version}.tgz
BuildArch:           noarch
ExclusiveArch:       %{nodejs_arches} noarch
BuildRequires:       nodejs-packaging npm(tape) npm(has-symbols)
%description
%{summary}.

%prep
%setup -q -n package
rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/is-symbol
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/is-symbol
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} --es-staging --harmony test/index.js

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/is-symbol

%changelog
* Thu Aug 20 2020 wangxiao <wangxiao65@huawei.com> - 1.0.2-1
- Package init
