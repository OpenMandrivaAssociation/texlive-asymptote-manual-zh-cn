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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is an (incomplete, simplified) Chinese translation of the Asymptote
manual.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/doc/support
%dir %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn
%dir %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/README
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/asymptote-manual-zh-cn.pdf
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/CDlabel.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/CLEAN.bat
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/Coons.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/Gouraud.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/MAKEPDF.bat
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/Pythagoras.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/adobefonts.tex
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/asycolors.sty
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/asysyntex.tex
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/axialshade.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/bezier2.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/beziercurve.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/bigsquare.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/cleantmp
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/clippath.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/colons.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/colors.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/cube.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/diagonal.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/dots.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/fzfonts.tex
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/hatch.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/join.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/labelalign.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/labelsquare.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/latticeshading.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/linecap.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/linejoin.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/linetype.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/logo.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/main.tex
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/makepdf
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/makepen.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/mexicanhat.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/quartercircle.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/shadedtiling.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/shadestroke.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/square.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/subpictures.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/superpath.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/tile.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/transparency.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/windingnumber.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-manual-zh-cn/src/winfonts.tex
