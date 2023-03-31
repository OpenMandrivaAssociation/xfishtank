%define name	xfishtank
%define version	2.1tp

Summary:	A graphic display of an animated aquarium
Name:		%{name}
Version:	%{version}
Release:	29
License:	MIT
Group:		Toys
BuildRequires:	pkgconfig(x11) 
BuildRequires:  pkgconfig(xext)
BuildRequires:  imake

Source:		http://metalab.unc.edu/pub/Linux/X11/demos/xfishtank-%{version}.tar.bz2
Patch:		xfishtank-2.1tp-xf4.patch

%description
The xfishtank program displays an animated aquarium background on your
screen. It sets the X root window so will not work if your desktop
environment sets the background.

%prep

%setup -q
%patch -p0

%build
xmkmf
%make_build CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.Linux  README.TrueColor  README.Why.2.1tp
%defattr(755,root,root,755)
%{_bindir}/%{name}



%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1tp-15mdv2011.0
+ Revision: 671311
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1tp-14mdv2011.0
+ Revision: 608206
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1tp-13mdv2010.1
+ Revision: 524442
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.1tp-12mdv2009.1
+ Revision: 351153
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.1tp-11mdv2009.0
+ Revision: 226037
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 2.1tp-10mdv2008.1
+ Revision: 179510
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Jun 16 2007 Adam Williamson <awilliamson@mandriva.org> 2.1tp-9mdv2008.0
+ Revision: 40341
- spec clean, new X layout, rebuild for new era
- Import xfishtank



* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.1tp-8mdk
- Rebuild

* Sat Jul 12 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.1tp-7mdk
- rebuild
- macroize
- rm -rf $RPM_BUILD_ROOT at the beginning of %%install
- compile with $RPM_OPT_FLAGS
- fix permissions
- fix spec filename

* Tue May 01 2001 David BAUDENS <baudens@mandrakesoft.com> 2.1tp-6mdk
- Use %%_tmppath for BuildRoot

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.1tp-5mdk
- automatically added BuildRequires

* Fri May 26 2000 Adam Lebsack <adam@mandrakesoft.com> 2.1tp-4mdk
- Imake bugfix for XFree86-4.0

* Sat Mar 25 2000 DindinX <odin@mandrakesoft.com> 2.1tp-3mdk
- Fix Group, installed doc.

* Fri Nov 5 1999 Damien Krotkine <damien@mandrakesoft.com>
- Mandrake release

* Tue Nov  2 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 2.1tp (whork with 16 and 24 display).

* Thu May  6 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 14)

* Wed Mar 17 1999 Preston Brown <pbrown@redhat.com>
- wmconfig entry removed.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
