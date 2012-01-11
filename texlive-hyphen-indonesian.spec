# revision 23092
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-indonesian
Version:	20111103
Release:	2
Summary:	Indonesian hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-indonesian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Indonesian (Bahasa Indonesia) in ASCII
encoding.  They are probably also usable for Malay (Bahasa
Melayu).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-indonesian
%_texmf_language_def_d/hyphen-indonesian
%_texmf_language_lua_d/hyphen-indonesian

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-indonesian <<EOF
\%\% from hyphen-indonesian:
indonesian loadhyph-id.tex
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-indonesian <<EOF
\%\% from hyphen-indonesian:
\addlanguage{indonesian}{loadhyph-id.tex}{}{2}{2}
EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-indonesian <<EOF
-- from hyphen-indonesian:
	['indonesian'] = {
		loader = 'loadhyph-id.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-id.pat.txt',
		hyphenation = 'hyph-id.hyp.txt',
	},
EOF
