%include	/usr/lib/rpm/macros.perl
Summary:	Forms Data Format Toolkit
Summary(pl.UTF-8):   Zestaw narzędzi do formularzy PDF
Name:		fdftk
Version:	5
Release:	2
License:	restricted, no source
Group:		Libraries
# note: to download source, you must use a browser with cookies
# enabled and accept license that appears under Source0 URL at the first time
#Source0:	http://partners.adobe.com/asn/developer/acrosdk/fdftk/%{name}v%{version}.tar.gz
Source0:	%{name}v%{version}.tar.gz
URL:		http://partners.adobe.com/asn/developer/acrosdk/forms.html
NoSource:	0
BuildRequires:	rpm-perlprov >= 4.1-13
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Acrobat Forms (PDF) Data Format Toolkit - C library.

%description -l pl.UTF-8
Zestaw narzędzi do formularzy w plikach PDF (Acrobat Forms) -
biblioteka C.

%package devel
Summary:	Forms Data Format Toolkit - header file
Summary(pl.UTF-8):   Zestaw narzędzi do formularzy PDF - plik nagłówkowy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Acrobat Forms (PDF) Data Format Toolkit - header file.

%description devel -l pl.UTF-8
Zestaw narzędzi do formularzy w plikach PDF (Acrobat Forms) - plik
nagłówkowy.

%package doc
Summary:	Documentation and licensing information for fdftk
Summary(pl.UTF-8):   Dokumentacja i treść licencji fdftk
Group:		Documentation

%description doc
Documentation and licensing information for fdftk - common for C++
library and Perl module.

%description doc -l pl.UTF-8
Dokumentacja i treść licencji fdftk - wspólne dla biblioteki w C++ i
modułu Perla.

%package -n perl-Acrobat-FDF
Summary:	Acrobat::FDF Perl module
Summary(pl.UTF-8):   Moduł Perla Acrobat::FDF
Group:		Development/Languages/Perl

%description -n perl-Acrobat-FDF
Acrobat Forms (PDF) Data Format Toolkit - Perl module.

%description -n perl-Acrobat-FDF -l pl.UTF-8
Zestaw narzędzi do formularzy w plikach PDF (Acrobat Forms) - moduł
Perla.

%prep
%setup -q -n FDFToolkitForUNIX

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_examplesdir}/%{name}-%{version}}

install HeadersAndLibraries/headers/fdftk.h $RPM_BUILD_ROOT%{_includedir}
install -D HeadersAndLibraries/headers/FDF.pm $RPM_BUILD_ROOT%{perl_vendorarch}/Acrobat/FDF.pm
install HeadersAndLibraries/linux/C/libfdftk.so $RPM_BUILD_ROOT%{_libdir}
install -D HeadersAndLibraries/linux/PERL/fdf.so $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Acrobat/FDF/fdf.so

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
%{perl_vendorarch}/Acrobat
%attr(755,root,root) %{perl_vendorarch}/auto/Acrobat
