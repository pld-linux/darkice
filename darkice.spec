Summary:	DarkIce live IceCast / ShoutCast streamer
Summary(pl):	DarkIce - dostarczyciel strumieni IceCast/ShoutCast
Name:		darkice
Version:	0.17.1
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/darkice/%{name}-%{version}.tar.gz
# Source0-md5:	91221134cec3d52af842a9d50c06ee7d
Patch0:		%{name}-shared.patch
Patch1:		%{name}-no_libnsl.patch
Patch2:		%{name}-amd64.patch
URL:		http://darkice.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lame-libs-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	pkgconfig
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
ShoutCast. DarkIce enkoduje dane z karty d�wi�kowej do MP3 i/lub Ogg
Vorbis, a nast�pnie wysy�a strumie� MP3 do jednego lub wi�cej serwer�w
IceCast i/lub ShoutCast, strumie� Ogg Vorbis do jednego lub wi�cej
serwer�w IceCast2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
