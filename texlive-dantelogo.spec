Name:		texlive-dantelogo
Version:	38599
Release:	1
Summary:	A font for DANTE's logo
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dantelogo
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dantelogo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dantelogo.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The DANTE font for the logo of DANTE (http://www.dante.de), the
German speaking TeX users group. The font includes only the
five characters d, a, n, t, and e. dantelogo.sty provides an
interface for LuaLaTeX/XeLaTeX/pdfLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/dantelogo
%{_texmfdistdir}/fonts/vf/public/dantelogo
%{_texmfdistdir}/fonts/type1/public/dantelogo
%{_texmfdistdir}/fonts/tfm/public/dantelogo
%{_texmfdistdir}/fonts/opentype/public/dantelogo
%{_texmfdistdir}/fonts/map/dvips/dantelogo
%{_texmfdistdir}/fonts/enc/dvips/dantelogo
%doc %{_texmfdistdir}/doc/fonts/dantelogo

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
