Summary:	DarkIce live IceCast / ShoutCast streamer
Summary(pl):	DarkIce live IceCast / ShoutCast streamer
Name:		darkice
Version:	0.10
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
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
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DarkIce is an IceCast, IceCast2 and ShoutCast live audio streamer. It
takes audio input from a sound card, encodes it into mp3 and/or Ogg
Vorbis, and sends the mp3 stream to one or more IceCast and/or
ShoutCast servers, the Ogg Vorbis stream to one or more IceCast2
servers.

%description -l pl
DarkIce to dostarczyciel strumienia audio IceCast, IceCast2 oraz
ShoutCast. DarkIce enkoduje dane z karty d�wi�kowej do mp3 i/lub Ogg
Vorbis, a nast�pnie wysy�a strumie� mp3 do jednego lub wi�cej serwer�w
IceCast i/lub ShoutCast, strumie� Ogg Vorbis do jednego lub wi�cej
serwer�w IceCast2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f missing
aclocal
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
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%config(noreplace) %attr(600,root,root) %{_sysconfdir}/*.cfg
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
