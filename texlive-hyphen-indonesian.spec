%global tl_name hyphen-indonesian
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Indonesian hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-indonesian
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-indonesian.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Indonesian (Bahasa Indonesia) in ASCII
encoding. They are probably also usable for Malay (Bahasa Melayu).

