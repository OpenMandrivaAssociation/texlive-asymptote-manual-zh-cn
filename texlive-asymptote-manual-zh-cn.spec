Name:		texlive-asymptote-manual-zh-cn
Version:	15878
Release:	2
Summary:	A Chinese translation of the asymptote manual
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/asymptote-manual-zh-cn
License:	lgpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asymptote-manual-zh-cn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asymptote-manual-zh-cn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is an (incomplete, simplified) Chinese translation of the
Asymptote manual.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/support/asymptote-manual-zh-cn

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
