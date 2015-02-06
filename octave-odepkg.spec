%define	pkgname odepkg

Summary:	Octave package for solving ODEs
Name:       octave-%{pkgname}
Version:	0.8.2
Release:        6
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/odepkg/
BuildRequires:  octave-devel >= 3.2.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
Octave package for solving ordinary differential equations and more.

%prep
%setup -q -c %{pkgname}-%{version}
cp %{SOURCE0} .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
%__install -m 755 -d %{buildroot}%{_libdir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
export OCT_ARCH_PREFIX=%{buildroot}%{_libdir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX $OCT_ARCH_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %{SOURCE0} 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .

mv %{buildroot}%{_datadir}/octave/packages/%{pkgname}-%{version}/doc/%{pkgname}.pdf .

%clean

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%doc COPYING DESCRIPTION *.pdf
%{_datadir}/octave/packages/%{pkgname}-%{version}
%{_libdir}/octave/packages/%{pkgname}-%{version}
