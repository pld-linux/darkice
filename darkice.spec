Summary:	DarkIce live IceCast / ShoutCast streamer
Summary(pl):	DarkIce live IceCast / ShoutCast streamer
Name:		darkice
Version:	0.7
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-shared.patch
URL:		http://darkice.sourceforge.net/
BuildRequires:	readline-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lame-libs-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libstdc++-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DarkIce is an IceCast, IceCast2 and ShoutCast live audio streamer. It
takes audio input from a sound card, encodes it into mp3 and/or Ogg
Vorbis, and sends the mp3 stream to one or more IceCast and/or
ShoutCast servers, the Ogg Vorbis stream to one or more IceCast2
servers.

%description -l pl
DarkIce to dostarczyciel strumienia audio IceCast, IceCast2 oraz
ShoutCast. DarkIce enkoduje dane z karty d¼wiêkowej do mp3 i/lub Ogg
Vorbis, a nastêpnie wysy³a strumieñ mp3 do jednego lub wiêcej serwerów
IceCast i/lub ShoutCast, strumieñ Ogg Vorbis do jednego lub wiêcej
serwerów IceCast2.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure \
	--with-lame \
	--with-vorbis

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%config(noreplace) %attr(600,root,root) %{_sysconfdir}/*.cfg
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
