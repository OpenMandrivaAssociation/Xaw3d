Summary:	A version of the MIT Athena widget set for X
Name:		Xaw3d
Version:	1.6.2
Release:	9
Group:		System/Libraries
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	bison flex
BuildRequires:	libtool-base
BuildRequires:	x11-util-macros
Source0:	http://xorg.freedesktop.org/individual/lib/lib%name-%version.tar.bz2
Patch0:		libXaw3d-soname-7.patch
Url:            http://xorg.freedesktop.org/individual/lib/
License:	MIT

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
%define staticname %mklibname %name -d -s

%package -n	%{libname}
Summary:	A version of the MIT Athena widget set for X
Group:		System/Libraries
Obsoletes:	%{name} < %EVRD
Provides:	%{name} = %EVRD

%description -n	%{libname}
Xaw3d is an enhanced version of the MIT Athena Widget set for
the X Window System.  Xaw3d adds a three-dimensional look to applications
with minimal or no source code changes.

You should install Xaw3d if you are using applications which incorporate
the MIT Athena widget set and you'd like to incorporate a 3D look into
those applications.

%package -n	%{develname}
Summary:	Header files for development using Xaw3d
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %version-%release
%if "%{develname}" != "%{libname}-devel"
Obsoletes:	%{libname}-devel 
%endif

%description -n	%{develname}
Xaw3d is an enhanced version of the MIT Athena widget set for
the X Window System.  Xaw3d adds a three-dimensional look to those
applications with minimal or no source code changes. Xaw3d-devel includes
the header files and static libraries for developing programs that take
full advantage of Xaw3d's features.

You should install Xaw3d-devel if you are going to develop applications
using the Xaw3d widget set.  You'll also need to install the Xaw3d
package.

%package -n %{staticname}
Summary:	Library files needed for linking statically to %name
Group:		Development/C
Requires:	%develname = %EVRD

%description -n %{staticname}
Library files needed for linking statically to %name

%prep
%setup -q -n lib%name-%version
%apply_patches

libtoolize --force
aclocal
automake -a
autoconf

%configure2_5x \
		--enable-arrow-scrollbars \
		--enable-gray-stipples \
        --enable-static
 
%build
%make

%install
%makeinstall_std

# Useless as it contains mostly build instructions
rm -rf %buildroot%_docdir/lib%name

%files -n %{libname}
%_libdir/*.so.%{major}*

%files -n %{develname}
%_libdir/*.so
%_includedir/X11/Xaw3d
%_libdir/pkgconfig/*.pc

%files -n %staticname
%_libdir/*.a