Summary:	DarkIce live IceCast / ShoutCast streamer
Summary(pl):	DarkIce - dostarczyciel strumieni IceCast/ShoutCast
Name:		darkice
Version:	0.14
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/darkice/%{name}-%{version}.tar.gz
# Source0-md5:	e196487f376ab29c43277add33be15be
Patch0:		%{name}-shared.patch
Patch1:		%{name}-no_libnsl.patch
Patch2:		%{name}-am_fixes.patch
Patch3:		%{name}-ac25x.patch
URL:		http://darkice.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lame-libs-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DarkIce is an IceCast, IceCast2 and ShoutCast live audio streamer. It
takes audio input from a sound card, encodes it into MP3 and/or Ogg
Vorbis, and sends the MP3 stream to one or more IceCast and/or
ShoutCast servers, the Ogg Vorbis stream to one or more IceCast2
servers.

%description -l pl
DarkIce to dostarczyciel strumienia audio IceCast, IceCast2 oraz
ShoutCast. DarkIce enkoduje dane z karty d¼wiêkowej do MP3 i/lub Ogg
Vorbis, a nastêpnie wysy³a strumieñ MP3 do jednego lub wiêcej serwerów
IceCast i/lub ShoutCast, strumieñ Ogg Vorbis do jednego lub wiêcej
serwerów IceCast2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-lame \
	--with-vorbis

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%config(noreplace) %attr(600,root,root) %{_sysconfdir}/*.cfg
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
