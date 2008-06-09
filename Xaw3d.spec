Summary:	A version of the MIT Athena widget set for X
Name:		Xaw3d
Version:	1.5E
Release:	%mkrel 8
Group:		System/Libraries
BuildRequires:	X11-devel xpm-devel bison flex imake

Source0:	ftp://ftp.x.org/contrib/widgets/Xaw3d/R6.3/%{name}-%{version}.tar.bz2
#Patch0:	Xaw3d-1.1-shlib.patch.bz2
Patch1:		Xaw3d-1.3-glibc.patch.bz2
Patch2:		Xaw3d-1.5E-xorg-imake.patch.bz2

Url:            ftp://ftp.x.org/contrib/widgets/Xaw3d/
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Xaw3d is an enhanced version of the MIT Athena Widget set for
the X Window System.  Xaw3d adds a three-dimensional look to applications
with minimal or no source code changes.

You should install Xaw3d if you are using applications which incorporate
the MIT Athena widget set and you'd like to incorporate a 3D look into
those applications.

#
# (fg) Lib policy stuff
#

%define major 7
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

%package -n	%{libname}
Summary:	A version of the MIT Athena widget set for X
Group:		System/Libraries
Obsoletes:	%{name}
Provides:	%{name}

%description -n	%{libname}
Xaw3d is an enhanced version of the MIT Athena Widget set for
the X Window System.  Xaw3d adds a three-dimensional look to applications
with minimal or no source code changes.

You should install Xaw3d if you are using applications which incorporate
the MIT Athena widget set and you'd like to incorporate a 3D look into
those applications.

%package -n	%{develname}
Summary:	Header files and static libraries for development using Xaw3d
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %version-%release
Obsoletes:	%{libname}-devel 

%description -n	%{develname}
Xaw3d is an enhanced version of the MIT Athena widget set for
the X Window System.  Xaw3d adds a three-dimensional look to those
applications with minimal or no source code changes. Xaw3d-devel includes
the header files and static libraries for developing programs that take
full advantage of Xaw3d's features.

You should install Xaw3d-devel if you are going to develop applications
using the Xaw3d widget set.  You'll also need to install the Xaw3d
package.

%prep
%setup -q -c
cd xc/lib/Xaw3d
#%patch0 -p0
ln -s .. X11
%patch1 -p4
%patch2 -p0
 
%build
cd xc/lib/Xaw3d
xmkmf
%ifarch alpha
# alpha was giving internal compiler errors...
make CDEBUGFLAGS=""
%else
%make CDEBUGFLAGS="$RPM_OPT_FLAGS" CXXDEBUGFLAGS="$RPM_OPT_FLAGS"
%endif

%install
rm -rf $RPM_BUILD_ROOT
cd xc/lib/Xaw3d
%{makeinstall_std}


%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%_libdir/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%_libdir/*.so
%{_includedir}/X11/Xaw3d
