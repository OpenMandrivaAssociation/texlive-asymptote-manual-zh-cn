%global tl_name asymptote-manual-zh-cn
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A Chinese translation of the asymptote manual
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/asymptote-manual-zh-cn
License:	lgpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asymptote-manual-zh-cn.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asymptote-manual-zh-cn.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is an (incomplete, simplified) Chinese translation of the Asymptote
manual.

