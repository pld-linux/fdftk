%include	/usr/lib/rpm/macros.perl
Summary:	Forms Data Format Toolkit
Summary(pl):	Zestaw narzêdzi do formularzy PDF
Name:		fdftk
Version:	5
Release:	1
License:	restricted, no source
Group:		Libraries
# note: to download source, you must use a browser with cookies
# enabled and accept license that appears under Source0 URL at the first time
Source0:	http://partners.adobe.com/asn/developer/acrosdk/fdftk/%{name}v%{version}.tar.gz
URL:		http://partners.adobe.com/asn/developer/acrosdk/forms.html
NoSource:	0
BuildRequires:	rpm-perlprov
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Acrobat Forms (PDF) Data Format Toolkit - C library.

%description -l pl
Zestaw narzêdzi do formularzy w plikach PDF (Acrobat Forms) -
biblioteka C.

%package devel
Summary:	Forms Data Format Toolkit - header file
Summary(pl):	Zestaw narzêdzi do formularzy PDF - plik nag³ówkowy
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Acrobat Forms (PDF) Data Format Toolkit - header file.

%description devel -l pl
Zestaw narzêdzi do formularzy w plikach PDF (Acrobat Forms) - plik
nag³ówkowy.

%package doc
Summary:	Documentation and licensing information for fdftk
Summary(pl):	Dokumentacja i tre¶æ licencji fdftk
Group:		Documentation

%description doc
Documentation and licensing information for fdftk - common for C++
library and Perl module.

%description doc -l pl
Dokumentacja i tre¶æ licencji fdftk - wspólne dla biblioteki w C++ i
modu³u Perla.

%package -n perl-Acrobat-FDF
Summary:	Acrobat::FDF Perl module
Summary(pl):	Modu³ Perla Acrobat::FDF
Group:		Development/Languages/Perl

%description -n perl-Acrobat-FDF
Acrobat Forms (PDF) Data Format Toolkit - Perl module.

%description -n perl-Acrobat-FDF -l pl
Zestaw narzêdzi do formularzy w plikach PDF (Acrobat Forms) - modu³
Perla.

%prep
%setup -q -n FDFToolkitForUNIX

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_examplesdir}/%{name}-%{version}}

install HeadersAndLibraries/headers/fdftk.h $RPM_BUILD_ROOT%{_includedir}
install -D HeadersAndLibraries/headers/FDF.pm $RPM_BUILD_ROOT%{perl_sitearch}/Acrobat/FDF.pm
install HeadersAndLibraries/linux/C/libfdftk.so $RPM_BUILD_ROOT%{_libdir}
install -D HeadersAndLibraries/linux/PERL/fdf.so $RPM_BUILD_ROOT%{perl_sitearch}/auto/Acrobat/FDF/fdf.so

cp -rf FormsExamples Samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfdftk.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/fdftk.h

%files doc
%defattr(644,root,root,755)
%doc Documentation/*.pdf LicenseAgreements/SDKEnglish4.03.01.pdf
%lang(fr) %doc LicenseAgreements/SDKFrench\ 4.03.01.pdf
%lang(de) %doc LicenseAgreements/SDKGerman4.3.01.pdf
%lang(ja) %doc LicenseAgreements/SDKJapanese4.3.01.pdf
%{_examplesdir}/%{name}-%{version}

%files -n perl-Acrobat-FDF
%defattr(644,root,root,755)
%{perl_sitearch}/Acrobat
%attr(755,root,root) %{perl_sitearch}/auto/Acrobat
