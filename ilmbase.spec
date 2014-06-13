%define major	11
%define devname %mklibname %{name} -d

Summary:	Abraction/convenience libraries for OpenEXR
Name:		ilmbase
Version:	2.1.0
Release:	2
Group:		System/Libraries
License:	BSD
Url:		http://www.openexr.com
Source0:	http://download.savannah.nongnu.org/releases/openexr/%{name}-%{version}.tar.gz
Patch0:		ilmbase-1.0.0-pthread.patch

%libpackage Iex 2_1 %{major}
%libpackage IlmThread 2_1 %{major}
%libpackage IexMath 2_1 %{major}
%libpackage Imath 2_1 %{major}
%libpackage Half %{major}

%description
Half is a class that encapsulates the ilm 16-bit floating-point format.

IlmThread is a thread abstraction library for use with OpenEXR
and other software packages.

Imath implements 2D and 3D vectors, 3x3 and 4x4 matrices, quaternions
and other useful 2D and 3D math functions.

Iex is an exception-handling library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{mklibname Iex 2_1 %{major}} = %{EVRD}
Requires:	%{mklibname IlmThread 2_1 %{major}} = %{EVRD}
Requires:	%{mklibname IexMath 2_1 %{major}} = %{EVRD}
Requires:	%{mklibname Imath 2_1 %{major}} = %{EVRD}
Requires:	%{mklibname Half %{major}} = %{EVRD}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%prep
%setup -q
%apply_patches

./bootstrap

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{devname}
%doc AUTHORS ChangeLog  NEWS README
%{_includedir}/OpenEXR/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

