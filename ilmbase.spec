%define major	6
%define	libHalf %mklibname Half %{major}
%define	libIex %mklibname Iex %{major}
%define	libIlmThread %mklibname IlmThread %{major}
%define	libImath %mklibname Imath %{major}
%define devname %mklibname %{name} -d

Summary:	Abraction/convenience libraries for OpenEXR
Name:		ilmbase
Version:	1.0.2
Release:	9
Group:		System/Libraries
License:	BSD
Url:		http://www.openexr.com
Source0:	http://download.savannah.nongnu.org/releases/openexr/%{name}-%{version}.tar.bz2
Patch0:		ilmbase-1.0.0-pthread.patch
Patch1:		ilmbase-1.0.2-gcc43.patch
Patch2:		ilmbase-automake-1.13.patch

%description
Half is a class that encapsulates the ilm 16-bit floating-point format.

IlmThread is a thread abstraction library for use with OpenEXR
and other software packages.

Imath implements 2D and 3D vectors, 3x3 and 4x4 matrices, quaternions
and other useful 2D and 3D math functions.

Iex is an exception-handling library.

%package -n %{libHalf}
Summary:	Abraction/convenience libraries for OpenEXR
Group:		System/Libraries
Obsoletes:	%{_lib}ilmbase6 < 1.0.2-7

%description -n %{libHalf}
Half is a class that encapsulates the ilm 16-bit floating-point format.

%package -n %{libIex}
Summary:	Abraction/convenience libraries for OpenEXR
Group:		System/Libraries
Conflicts:	%{_lib}ilmbase6 < 1.0.2-7

%description -n %{libIex}
Iex is an exception-handling library.

%package -n %{libIlmThread}
Summary:	Abraction/convenience libraries for OpenEXR
Group:		System/Libraries
Conflicts:	%{_lib}ilmbase6 < 1.0.2-7

%description -n %{libIlmThread}
IlmThread is a thread abstraction library for use with OpenEXR
and other software packages.

%package -n %{libImath}
Summary:	Abraction/convenience libraries for OpenEXR
Group:		System/Libraries
Conflicts:	%{_lib}ilmbase6 < 1.0.2-7

%description -n %{libImath}
Imath implements 2D and 3D vectors, 3x3 and 4x4 matrices, quaternions
and other useful 2D and 3D math functions.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libHalf} = %{version}-%{release}
Requires:	%{libIex} = %{version}-%{release}
Requires:	%{libIlmThread} = %{version}-%{release}
Requires:	%{libImath} = %{version}-%{release}
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

%files -n %{libHalf}
%{_libdir}/libHalf.so.%{major}*

%files -n %{libIex}
%{_libdir}/libIex.so.%{major}*

%files -n %{libIlmThread}
%{_libdir}/libIlmThread.so.%{major}*

%files -n %{libImath}
%{_libdir}/libImath.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog  NEWS README
%{_includedir}/OpenEXR/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

