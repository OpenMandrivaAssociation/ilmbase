%define major 6
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Abraction/convenience libraries for OpenEXR
Name:		ilmbase
Version:	1.0.2
Release:	5
Group:		System/Libraries
License:	BSD
URL:		http://www.openexr.com
Source0:	http://download.savannah.nongnu.org/releases/openexr/ilmbase-%{version}.tar.bz2
Patch0:		%{name}-1.0.0-pthread.patch
Patch1:		%{name}-1.0.2-gcc43.patch

%description
Half is a class that encapsulates the ilm 16-bit floating-point format.

IlmThread is a thread abstraction library for use with OpenEXR
and other software packages.

Imath implements 2D and 3D vectors, 3x3 and 4x4 matrices, quaternions
and other useful 2D and 3D math functions.

Iex is an exception-handling library.

%package -n %{libname}
Summary:	Abraction/convenience libraries for OpenEXR
Group:		System/Libraries

%description -n %{libname}
Half is a class that encapsulates the ilm 16-bit floating-point format.

IlmThread is a thread abstraction library for use with OpenEXR
and other software packages.

Imath implements 2D and 3D vectors, 3x3 and 4x4 matrices, quaternions
and other useful 2D and 3D math functions.

Iex is an exception-handling library.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Requires:	pkgconfig(glu)
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	OpenEXR-devel < 1.4.1

%description -n %{develname}
Development files for %{name}.

%prep
%setup -q
%patch0 -p1 -b .pthread
%patch1 -p1 -b .gcc43

./bootstrap

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog  NEWS README
%{_includedir}/OpenEXR/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-3mdv2011.0
+ Revision: 665507
- mass rebuild

* Mon Sep 20 2010 Tomas Kindl <supp@mandriva.org> 1.0.2-2mdv2011.0
+ Revision: 580288
- add missing header to ImathMatrix.h so OpenEXR 1.7.0 would compile...

* Sat Sep 04 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-1mdv2011.0
+ Revision: 575899
- update to new version 1.0.2
- disable tests

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-9mdv2010.1
+ Revision: 522921
- rebuilt for 2010.1

* Sat Sep 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-8mdv2010.0
+ Revision: 449342
- rebuild for missing binaries

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.1-7mdv2010.0
+ Revision: 425331
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-6mdv2009.0
+ Revision: 221625
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat Jan 12 2008 Anssi Hannula <anssi@mandriva.org> 1.0.1-5mdv2008.1
+ Revision: 149384
- devel conflicts with old OpenEXR-devel

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.1-4mdv2008.1
+ Revision: 133192
- fix provides for devel package

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.1-3mdv2008.1
+ Revision: 113732
- do not package COPYING file
- somehow ilmbase-devel is not on hdlist :/

* Sat Nov 17 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.1-2mdv2008.1
+ Revision: 109523
- somehow this version is missing on mirrors

* Tue Nov 06 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.1-1mdv2008.1
+ Revision: 106418
- new version

* Sun Oct 21 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-2mdv2008.1
+ Revision: 101047
- fix requires for devel package

* Sun Oct 21 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-1mdv2008.1
+ Revision: 100967
- import ilmbase


