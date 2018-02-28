Name:           bombono-dvd
Version:        1.2.4
Release:        9%{?dist}
Summary:        DVD authoring program with nice and clean GUI
                # License breakdown in README.
License:        GPLv2 and GPLv2+ and Boost and Python and LGPLv2+
URL:            https://github.com/muravjov/bombono-dvd
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         filesys-include-path.patch
Patch1:         %{url}/pull/15.patch#/%{version}-ftbfs-fix-gcc-7-boost-1.64.patch

# needs to match TBB - from adobe-source-libraries
ExclusiveArch:  i686 x86_64 ia64

BuildRequires:  adobe-source-libraries-devel
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ffmpeg-devel
BuildRequires:  gettext
BuildRequires:  gtkmm24-devel
BuildRequires:  libdvdread-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libxml++-devel
BuildRequires:  mjpegtools-devel
BuildRequires:  pkgconfig
BuildRequires:  python2-scons
Requires:       dvd+rw-tools
Requires:       dvdauthor
Requires:       enca
Requires:       ffmpeg
Requires:       mjpegtools
#Suggests:      totem, gvfs, scons, twolame

# http://lists.rpmfusion.org/pipermail/rpmfusion-developers/2012-January/011438.html
Provides:       bundled(boost-logging) = 0.22.7.20120126svn76686

%global  boost_flags \\\
    -DBOOST_SYSTEM_NO_DEPRECATED -DBOOST_FILESYSTEM_VERSION=3
%global warn_flags  \
    -Wno-unused-variable
%global  scons       \
    scons  %{?_smp_mflags}                                 \\\
    BUILD_CFG=debug                                        \\\
    BUILD_BRIEF=false                                      \\\
    BUILD_QUICK=false                                      \\\
    CC="%__cc"                                             \\\
    CXX="%__cxx"                                           \\\
    CFLAGS="${RPM_OPT_FLAGS}"                              \\\
    CPPFLAGS="%{warn_flags} %{boost_flags}"                \\\
    LDFLAGS="${RPM_LD_FLAGS}"                              \\\
    PREFIX=%{_prefix}                                      \\\
    TEST=false                                             \\\
    TEST_BUILD=false                                       \\\
    USE_EXT_BOOST=true                                     \\\
    USE_EXT_ASL=true

%description
Bombono DVD is an easy to use program for making DVD-Video. The main features
are an excellent MPEG viewer with time line, a real WYSIWYG menu editor with
live thumbnails and monitor, and comfortable Drag-N-Drop support. Authoring
to folder, making an ISO-image or burning directly to DVD as well as
re-authoring by importing video from DVD discs is also supported.

%prep
%autosetup -p1

sed -i -e 's@#!/usr/bin/env python@#!/usr/bin/python2@g'  $(find . -name SCons\*) \
 resources/scons_authoring/menu_SConscript \
 resources/scons_authoring/ADVD.py
rm -r debian libs/boost-lib src/mlib/tests libs/mpeg2dec ./libs/asl/adobe

%build
%scons build

%install
rm config.opts
%scons DESTDIR=%{buildroot} install
rm -rf docs/man docs/TechTasks docs/Atom.planner

desktop-file-validate \
    %{buildroot}%{_datadir}/applications/bombono-dvd.desktop

%find_lang %{name}

%files -f  bombono-dvd.lang
%doc README docs
%license COPYING
%{_bindir}/*
%{_datadir}/bombono/
%{_datadir}/applications/bombono-dvd.desktop
%{_datadir}/pixmaps/bombono-dvd.png
%{_datadir}/icons/hicolor/*/apps/bombono-dvd.png
%{_datadir}/mime/packages/bombono.xml
%{_mandir}/man1/*

%changelog
* Wed Feb 28 2018 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.4-8
- Rebuild for boost-1.66
- Remove scriptlets

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.4-7
- Rebuilt for ffmpeg-3.5 git

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.2.4-5
- Clean up spec file and fix rpmlint errors
- Change url to github
- Pull patch from last commit directly

* Sat Jul 8 2017 Link Dupont <link.dupont@gmail.com> - 1.2.4-4
- patch for boost, g++ and ffmpeg changes

* Sat Mar 18 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 16 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.2.4-2
- Make the build hardened

* Sun Aug 14 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.2.4-1
- Update to 1.2.4 release

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1.2.2-14
- Rebuilt for ffmpeg-3.1.1

* Mon Jul 04 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.2.2-13
- rebuilt

* Sun Jul 03 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.2.2-12
- patch for boost, ffmpeg and c++11 changes

* Sun Oct 19 2014 Sérgio Basto <sergio@serjux.com> - 1.2.2-11
- Rebuilt for FFmpeg 2.4.3

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.2.2-10
- Rebuilt for FFmpeg 2.4.x

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 1.2.2-9
- Rebuilt for ffmpeg-2.3

* Sat Aug 02 2014 Sérgio Basto <sergio@serjux.com> - 1.2.2-8
- Rebuilt for boost-1.55

* Sat Mar 29 2014 Sérgio Basto <sergio@serjux.com> - 1.2.2-7
- Rebuilt for ffmpeg-2.2

* Fri Dec 27 2013 leamas@nowhere.net - 1.2.2-6
- Rebuild after F20 branching

* Sun May 26 2013 Alec Leamas <leamas@nowhere.net> - 1.2.2-5
- Build problems for f20.

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.2.2-2
- Rebuilt for x264/FFmpeg

* Sat Mar 9 2013 Alec Leamas <alec@nowhere.com> - 1.2.2-1
- Rebuilt for new upstream release

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-8.20120615gitcdab110
- Rebuilt for FFmpeg 1.0

* Wed Oct 24 2012 Alec Leamas <leamas@nowhere.net>    - 1.2.0-7.20120616gitcdab110
- Typos in spec file, stepping rel #
- Added patch for current boost available but not merged upstream.
- Fixed build flags (new patch)
- Removed insane release # from source filename.

* Mon Jul 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-4.20120616gitcdab110.2
- Add ExclusiveArch - inherited from TBB

* Tue Jun 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-4.20120616gitcdab110.1
- Rebuilt for FFmpeg

* Sat Jun 16 2012 Alec Leamas <alec@nowhere.com> 1.2.0-4.20120616gitcdab110
- Updating to git HEAD, solving build problems w ffmpeg 11.1

* Thu Apr 12 2012 Alec Leamas <alec@nowhere.com> 1.2.0-3.20120412gite9390e7
- Fixing source name error
- Updating to latest git (fixing f17 compile error).

* Thu Apr 12 2012 Alec Leamas <alec@nowhere.com> 1.2.0-2.20120412gite9390e7
- Bad version, not built

* Sun Apr 01 2012 Alec Leamas <alec@nowhere.com> 1.2.0-1.20120401git2278251
- New version-release scheme
- Minor fixes

* Wed Mar 28 2012 Alec Leamas <alec@nowhere.com> 1.2.0.20120128gitf39d5d5-1
- Adding BR: adobe-source-libraries-devel
- Removing copyright notices after email discussion with Ilya.
- Updating to latest git
- The upstream version unbundles adobe-source-libraries

* Sat Jan 28 2012 Alec Leamas <alec@nowhere.com> 1.2.0.20120128gitf39d5d5-1
- Adding  bundling exception for boost-logging.

* Wed Jan 25 2012 Alec Leamas <alec@nowhere.com> 1.2.0.20120125git3f4adbb-1
- Removing irrelevant files in docs/
- Updating deps to reflect bb7f789 "twolame is optional..."
- Removing bundled libmpeg2

* Sat Jan 21 2012 Alec Leamas <alec@nowhere.com>   1.2.0.20101210git2840c3a-1
- Updating to latest git source. Many patches accepted.
- Removing %%defattr.

* Sat Jan 14 2012 Alec Leamas <alec@nowhere.com>             1.2.0-4
- Refactoring scons parameters to rpm macro %%scons.
- Adding virtual provide for bundled mpeg lib.
- Use of Boost license, was BSD, handling license file.

* Sun Jan 8 2012 Alec Leamas <alec@nowhere.com>              1.2.0-3
- Using external boost lib, removing bundled one.
- Feeding standard rpm build flags to scons.
- Cleaning up post/posttrans snippets and deps.
- Restoring execute permissions on some scripts in %%prep

* Fri Jan 6 2012 Alec Leamas <alec@nowhere.com>              1.2.0-2
- Using manpages from debian dir, remove debian stuff.

* Wed Jan 4 2012 Alec Leamas <alec@nowhere.com>              1.2.0-1
- First attempt to modify Ilya Murav'jo's spec file for Fedora.
- Adding changelog
- Added find_lang handling of .mo files.
- Adjusted source URL, Fedora wants a complete public one.
- Adjusted License: tag to reflect README.
- Removed things not used and/or deprecated in Fedora.
- Added scriptlets handling icons and mime types.
- Added %%doc
- Modified arguments to scons build and install.
- Fixed various rpmlint warnings
- Adjusted dependencies after mock build test.

* Mon Jan 1 2007  Ilya Murav'jov <muravev@yandex.ru>         1.0.2-0
- Faked entry by Alec leamas to reflect initial packager.

