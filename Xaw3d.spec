Summary:	A version of the MIT Athena widget set for X
Name:		Xaw3d
Version:	1.6.2
Release:	1
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

%configure
 
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

%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5E-13mdv2011.0
+ Revision: 671975
- mass rebuild

* Tue Dec 21 2010 Funda Wang <fwang@mandriva.org> 1.5E-12mdv2011.0
+ Revision: 623568
- update build flag

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5E-12mdv2010.1
+ Revision: 521914
- rebuilt for 2010.1

* Wed Sep 09 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.5E-11mdv2010.0
+ Revision: 436106
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.5E-9mdv2009.0
+ Revision: 226015
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5E-8mdv2008.1
+ Revision: 178763
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 19 2007 Funda Wang <fwang@mandriva.org> 1.5E-7mdv2008.0
+ Revision: 66599
- New devel package policy
- Remove not working/needed %%post section

* Wed May 23 2007 Christiaan Welvaart <spturtle@mandriva.org> 1.5E-6mdv2008.0
+ Revision: 30164
- Import Xaw3d



* Wed Aug  9 2006 Götz Waschk <waschk@mandriva.org> 1.5E-6mdv2007.0
- rebuild with fixed xmkmf

* Tue Jun 06 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.5E-5mdv2007.0
- fix buildrequires
- drop useless prereq

* Sun May 21 2006 Götz Waschk <waschk@mandriva.org> 1.5E-4mdk
- move files to the new X location

* Wed Jan  4 2006 Warly <warly@mandriva.com> 1.5E-3mdk
- Rebuild to fix 'parent not composite' problem (in application linked with libXaw3d

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.5E-2mdk
- Rebuild

* Thu Jan 13 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.5E-1mdk
- 1.5E
- add P2 from fedora
- drop P0
- drop static library

* Wed Jul 30 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.5-13mdk
- BuildRequires: xpm-devel

* Tue Jul 22 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.5-12mdk
- rebuild
- macroize

* Thu Dec  5 2002 Frederic Lepied <flepied@mandrakesoft.com> 1.5-11mdk
- use %%mklibname

* Fri Sep 27 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.5-10mdk
- rpmlint fixes: strange-permission, hardcoded-library-path

* Fri Feb 23 2001 Francis Galiegue <fg@mandrakesoft.com> 1.5-9mdk
- Obsoletes and Provides Xaw3d

* Fri Feb 23 2001 Francis Galiegue <fg@mandrakesoft.com> 1.5-8mdk
- BuildRequires: flex, bison
- New library policy

* Wed Jan 10 2001 David BAUDENS <baudens@mandrakesoft.com> 1.5-7mdk
- BuildRequires: libxpm4-devel

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.5-6mdk
- automatically added BuildRequires

* Mon Mar 27 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.5-5mdk
- fix group.

* Sat Dec 18 1999 Stefan van der Eijk <s.vandereijk@chello.nl>
- adopted spec file to build on alpha (ifarch statement in build)
(pixel's rebuild)

* Tue Nov 02 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- build for new environment

* Sat Jul 17 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- 1.5
- update download URL
- remove obsolete R6.3 patch

* Tue May 04 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS
- add de locale

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 21)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Fri Nov 06 1998 Preston Brown <pbrown@redhat.com>
- added security/update patch from debian (the X11R6.3 patch). Thanks guys. :)

* Wed Oct 14 1998 Cristian Gafton <gafton@redhat.com>
- handle the symlink with triggers instead of getting rid of it

* Mon Oct  5 1998 Jeff Johnson <jbj@redhat.com>
- remove backward compatible symlink.

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- fixed the bad symlink
- BuildRoot

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Nov 04 1997 Erik Troan <ewt@redhat.com>
- don't lave an improper return code from %%pre

* Mon Nov 03 1997 Cristian Gafton <gafton@redhat.com>
- take care of the old location of the Xaw3d includes in case that one exist
- updated Prereq: field

* Mon Oct 26 1997 Cristian Gafton <gafton@redhat.com
- fixed the -devel package for the right include files path

* Mon Oct 13 1997 Donnie Barnes <djb@redhat.com>
- minor spec file cleanups

* Wed Oct 01 1997 Erik Troan <ewt@redhat.com>
- i18n widec.h patch needs to be applied on all systems

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- changed axp check to alpha

* Mon Jun 16 1997 Erik Troan <ewt@redhat.com>
- built against glibc
