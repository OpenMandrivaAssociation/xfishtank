Summary:	An X Window System graphic display of an animated aquarium
Name:		xfishtank
Version:	2.1tp
Release:	8mdk
License:	MIT
Group:		Toys
BuildRequires:	XFree86-devel

Source:		http://metalab.unc.edu/pub/Linux/X11/demos/xfishtank-%{version}.tar.bz2
Patch:		xfishtank-2.1tp-xf4.patch.bz2
BuildRoot:	%_tmppath/%name-%version-%release-root

%description
The xfishtank program displays an animated aquarium background on your
screen.

%prep

%setup -q
%patch -p0

%build
xmkmf
%make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.Linux  README.TrueColor  README.Why.2.1tp
%defattr(755,root,root,755)
%{_prefix}/X11R6/bin/xfishtank
