%define name	xfishtank
%define version	2.1tp

Summary:	A graphic display of an animated aquarium
Name:		%{name}
Version:	%{version}
Release:	%mkrel 14
License:	MIT
Group:		Toys
BuildRequires:	libx11-devel libxext-devel imake

Source:		http://metalab.unc.edu/pub/Linux/X11/demos/xfishtank-%{version}.tar.bz2
Patch:		xfishtank-2.1tp-xf4.patch
BuildRoot:	%_tmppath/%name-%version-%release-root

%description
The xfishtank program displays an animated aquarium background on your
screen. It sets the X root window so will not work if your desktop
environment sets the background.

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
%{_bindir}/%{name}

