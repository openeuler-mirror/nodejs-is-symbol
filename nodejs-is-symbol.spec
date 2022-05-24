%{?nodejs_find_provides_and_requires}
Name:                nodejs-is-symbol
Version:             1.0.2
Release:             2
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
%if "%{_build_arch}" == "riscv64"
%{__nodejs} --harmony test/index.js
%else
%{__nodejs} --es-staging --harmony test/index.js
%endif

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/is-symbol

%changelog
* Tue May 24 2022 YukariChiba <i@0x7f.cc> - 1.0.2-2
- Remove `--es-staging` flag which is not exist.

* Thu Aug 20 2020 wangxiao <wangxiao65@huawei.com> - 1.0.2-1
- Package init
