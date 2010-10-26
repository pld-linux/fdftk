%include	/usr/lib/rpm/macros.perl
Summary:	Forms Data Format Toolkit
Summary(pl.UTF-8):	Zestaw narzędzi do formularzy PDF
Name:		fdftk
Version:	6
Release:	1
License:	restricted, no source
Group:		Libraries
Source0:	http://download.macromedia.com/pub/developer/acrobat/FDFToolkitForUnix.tar.gz
# NoSource0-md5:	c67eb1dc626f48dcb8e388c89106dd58
NoSource:	0
URL:		http://www.adobe.com/devnet/acrobat/fdftoolkit.html
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
Summary(pl.UTF-8):	Zestaw narzędzi do formularzy PDF - plik nagłówkowy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Acrobat Forms (PDF) Data Format Toolkit - header file.

%description devel -l pl.UTF-8
Zestaw narzędzi do formularzy w plikach PDF (Acrobat Forms) - plik
nagłówkowy.

%package doc
Summary:	Documentation and licensing information for Adobe FdfTk
Summary(pl.UTF-8):	Dokumentacja i treść licencji Adobe FdfTk
Group:		Documentation

%description doc
Documentation and licensing information for Adobe FdfTk - common for
C++ library and Perl module.

%description doc -l pl.UTF-8
Dokumentacja i treść licencji Adobe FdfTk - wspólne dla biblioteki w
C++ i modułu Perla.

%package -n perl-Acrobat-FDF
Summary:	Acrobat::FDF Perl module - Perl interface to Adobe FdfTk
Summary(pl.UTF-8):	Moduł Perla Acrobat::FDF - interfejs Perla do Adobe FdfTk
Group:		Development/Languages/Perl

%description -n perl-Acrobat-FDF
Acrobat Forms (PDF) Data Format Toolkit - Perl module.

%description -n perl-Acrobat-FDF -l pl.UTF-8
Zestaw narzędzi do formularzy w plikach PDF (Acrobat Forms) - moduł
Perla.

%prep
%setup -q -n FDFToolkitForUnix

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install -D 'Headers and Libraries/Headers/FdfTk.h' $RPM_BUILD_ROOT%{_includedir}/FdfTk.h
install -D 'Headers and Libraries/Headers/FDF.pm' $RPM_BUILD_ROOT%{perl_vendorarch}/Acrobat/FDF.pm
install -D 'Headers and Libraries/LINUX/libFdfTk.so' $RPM_BUILD_ROOT%{_libdir}/libFdfTk.so
install -D 'Headers and Libraries/LINUX/FDF.so' $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Acrobat/FDF/FDF.so

cp -rf Samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libFdfTk.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/FdfTk.h

%files doc
%defattr(644,root,root,755)
%doc ReadMe.txt Acrobat\ FDF\ Toolkit\ EULA.pdf Documentation/*.pdf
%{_examplesdir}/%{name}-%{version}

%files -n perl-Acrobat-FDF
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/Acrobat
%{perl_vendorarch}/Acrobat/FDF.pm
%dir %{perl_vendorarch}/auto/Acrobat
%dir %{perl_vendorarch}/auto/Acrobat/FDF
%attr(755,root,root) %{perl_vendorarch}/auto/Acrobat/FDF/FDF.so
