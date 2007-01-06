# TODO:
# - logrotate support?
# - add /etc/sysconfig/darkice with log level selection and maybe not dropping
#   privs (so that realtime=yes could work)
# - or some other way to keep realtime scheduling while not running as root
Summary:	DarkIce live IceCast / ShoutCast streamer
Summary(pl):	DarkIce - dostarczyciel strumieni IceCast/ShoutCast
Name:		darkice
Version:	0.17.1
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/darkice/%{name}-%{version}.tar.gz
# Source0-md5:	91221134cec3d52af842a9d50c06ee7d
Source1:	%{name}.init
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
BuildRequires:  rpmbuild(macros) >= 1.165
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/lib/rpm/user_group.sh
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(pre):	/usr/sbin/usermod
Requires:	daemon
Requires:	rc-scripts
Provides:	group(darkice)
Provides:	user(darkice)
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
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-lame \
	--with-vorbis \
	--with-alsa \
	--without-twolame \
	--without-faac

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,/var/run/darkice,/var/log}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/darkice
touch $RPM_BUILD_ROOT/var/log/darkice.log

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 85 darkice
%useradd -u 59 -r -d /usr/share/empty -s /bin/false -c "Darkice" -g darkice darkice
%addusertogroup darkice audio

%post
/sbin/chkconfig --add darkice
%service darkice restart "darkice daemon"

%preun
if [ "$1" = "0" ] ; then
	%service darkice stop
	/sbin/chkconfig --del darkice
fi

%postun
if [ "$1" = "0" ]; then
	%userremove darkice
	%groupremove darkice
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%config(noreplace) %attr(640,root,darkice) %{_sysconfdir}/*.cfg
%attr(754,root,root) /etc/rc.d/init.d/darkice
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%dir %attr(775,root,darkice) /var/run/darkice
%attr(660,root,darkice) /var/log/darkice.log
