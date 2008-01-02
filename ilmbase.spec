%define major 6
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Abraction/convenience libraries for OpenEXR
Name:		ilmbase 
Version:	1.0.1
Release:	%mkrel 4
Group:		System/Libraries
License:	BSD
URL:		http://www.openexr.com
Source0:	http://download.savannah.nongnu.org/releases/openexr/ilmbase-%{version}.tar.bz2
Patch0:		%{name}-1.0.0-pthread.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
Requires:	mesaglu-devel
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files for %{name}.

%prep
%setup -q
%patch0 -p1 -b .pthread

./bootstrap

%build
%configure2_5x \
	--disable-static

%make

%check
make check

%install
rm -rf %{buildroot}

%makeinstall_std

rm -f  %{buildroot}%{_libdir}/lib*.la

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog  NEWS README
%{_includedir}/OpenEXR/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
