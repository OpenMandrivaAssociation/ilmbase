%define major 23
%define devname %mklibname %{name} -d

Summary:	Abraction/convenience libraries for OpenEXR
Name:		ilmbase
Version:	2.2.1
Release:	7
Group:		System/Libraries
License:	BSD
Url:		https://www.openexr.com
Source0:	http://download.savannah.nongnu.org/releases/openexr/%{name}-%{version}.tar.gz
# explicitly add $(PTHREAD_LIBS) to libIlmThread linkage (helps PTHREAD_LIBS workaround in %%build)
Patch0:		ilmbase-2.2.0-no_undefined.patch
# add Requires.private: gl glu to IlmBase.pc
Patch1:		ilmbase-1.0.3-pkgconfig.patch
# workaround glibc iszero macro
# https://bugzilla.redhat.com/show_bug.cgi?id=1383552
Patch2:		ilmbase-2.2.0-glibc_iszero.patch
#BuildRequires:	pkgconfig(gl)
#BuildRequires:	pkgconfig(glu)

%libpackage Iex 2_2 %{major}
%libpackage IlmThread 2_2 %{major}
%libpackage IexMath 2_2 %{major}
%libpackage Imath 2_2 %{major}
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
Requires:	%{mklibname Iex 2_2 %{major}} = %{EVRD}
Requires:	%{mklibname IlmThread 2_2 %{major}} = %{EVRD}
Requires:	%{mklibname IexMath 2_2 %{major}} = %{EVRD}
Requires:	%{mklibname Imath 2_2 %{major}} = %{EVRD}
Requires:	%{mklibname Half %{major}} = %{EVRD}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%prep
%autosetup -p1

./bootstrap

%build
%configure \
	--disable-static

%make PTHREAD_LIBS="-pthread -lpthread"

%install
%makeinstall_std

%files -n %{devname}
%doc AUTHORS ChangeLog  NEWS README
%{_includedir}/OpenEXR/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
