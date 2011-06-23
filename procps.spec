Summary: System and process monitoring utilities
Name: procps
Version: 3.2.8
Release: 14%{?dist}
License: GPLv2+ and LGPLv2+
Group: Applications/System
URL: http://procps.sourceforge.net
Source: http://procps.sourceforge.net/procps-%{version}.tar.gz
Source1: FAQ
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Patch1: procps-3.2.7-selinux.patch
Patch2: procps-3.2.7-misc.patch
Patch3: procps-3.2.7-FAQ.patch
Patch4: procps-3.2.7-selinux-workaround.patch
Patch6: procps-3.2.7-noproc.patch
Patch7: procps-3.2.7-pseudo.patch
Patch8: procps-3.2.7-0x9b.patch
# 157725 - sysctl -A returns an error
Patch9: procps-3.2.7-sysctl-writeonly.patch
# 161449 - "top" ignores user and system toprc
Patch10: procps-3.2.7-top-rc.patch
# 161303 - 'top' failed when remove cpus
# 186017 - Top "Cpu0" line never updates on single processor machine
Patch11: procps-3.2.7-top-remcpu.patch
# Selinux
Patch12: procps-3.2.7-libselinux.patch
# 177453 - for VIRT use proc->vm_size rather then proc->size (workaround)
Patch14: procps-3.2.7-top-env-vmsize.patch
# 174619 - workaround for reliable Cpu(s) data in the first loop
Patch15: procps-3.2.7-top-env-cpuloop.patch
# 185299 - cpu steal time support
Patch16: procps-3.2.7-vmstat-cpusteal.patch
# 134516 - ps ignores /proc/#/cmdline if contents 2047 bytes
Patch17: procps-3.2.7-longcmd.patch
# 189349 - 32bit vmstat on 64bit kernel
Patch18: procps-3.2.7-vmstat-pgpg.patch
# 212637 - sysctl using deprecated syscall
# 228870 - process `sysctl' is using deprecated sysctl ...
Patch21: procps-3.2.7-sysctl-ignore.patch
# 140975 - top corrupts screen when sorting on first column
Patch22: procps-3.2.7-top-sorthigh.path
# 234546 - 'w' doesn't give correct information about what's being run.
Patch23: procps-3.2.7-w-best.patch
# 183029 - watch ignores unicode characters
Patch24: procps-3.2.7-watch-unicode.patch
# 222251 - STIME can jitter by one second
Patch26: procps-3.2.7-ps-stime.patch
#244152 - ps truncates eip and esp to 32-bit values on 64-bit systems
Patch28: procps-3.2.7-ps-eip64.patch
#244960 - ps manpage formatted incorrectly
Patch29: procps-3.2.7-psman.patch
#255441 - ldopen libselinux.so.1 instead of libselinux.so
Patch30: procps-3.2.7-ps-libselinux.patch
#185994 - error when using "Single Cpu = Off" option
Patch31: procps-3.2.7-top-cpu0.patch
#354001 - CPU value in top is reported as an integer
Patch32: procps-3.2.7-top-cpuint.patch
#296471 - update top man page
Patch33: procps-3.2.7-top-manpage.patch
#440694 - strange text after selecting few field
Patch34: procps-3.2.7-top-clrscr.patch
#435453 - errors with man -t formatting of ps man page
Patch35: procps-3.2.7-ps-man-fmt.patch
#472783 - 'vmstat -p <partition name>', 
# the detailed statistics of the partition name is not output.
Patch36: procps-3.2.7-vmstat-partstats-long.patch
# Fix vmstat header to be 80 chars not 81
Patch37: procps-3.2.7-vmstat-header.patch
# rhel bug #475963: slabtop -o should display the info once
Patch38: procps-3.2.7-slabtop-once.patch
#476134 - added timestamp to vmstat with new option -t
Patch39: procps-3.2.7-vmstat-timestamp.patch
#manual page updated to document the -t functionality
Patch40: procps-3.2.7-vmstat-timestamp-manpage.patch
#added cgroup display to ps
Patch41: procps-3.2.7-ps-cgroup.patch
# 'requested writes' display in partition statistics
Patch42: procps-3.2.7-vmstat-partstats-reqwrites.patch
# '-l' option of 'free' documented
Patch43: procps-3.2.7-free-hlmem.patch
# enable core dump generation
Patch44: procps-enable-core.patch
#554721 -  procps states a bug is hit when receiving a signal 
Patch45: procps-3.2.7-no-bug-on-sig.patch
#554674 -  vmstat command with -n and -m does not display header even once 
Patch46: procps-3.2.8-vmstat-mn.patch
#479703 -  [RFE] Additional option for 'top' 
Patch47: procps-3.2.8-rhel6-usedmem.patch
#565971 -  double free or corruption in ps
Patch48: procps-3.2.8-double-free.patch
#564371 -  Enhance top to display in MB vs KB
Patch49: procps-3.2.7-top-memunit.patch
#578799 - vmstat -SM doesn't work but vmstat -S M does
Patch50: procps-3.2.7-vmstat-sm.patch
#580877 - negative ETIME field in ps
Patch51: procps-3.2.8-etime.patch
#583629 - pmap does not display RSS values for a pid
Patch52: procps-3.2.8-pmap-smaps.patch
#583625 - document that usernames exceeding column width 
#         are substituted with user ID
Patch53: procps-3.2.7-ps-manpage-uid.patch
#581547 - add vmstat -w option for wider output
Patch54: procps-3.2.8-vmstat-width.patch
Patch55: procps-3.2.7-width-man.patch
#585938 - [abrt] crash in procps-3.2.8-3.fc12
Patch56: procps-3.2.8-setlocale.patch
#596948  - vmstat disk device field is not long enough
Patch57: procps-3.2.8-vmstat-devlen.patch
#598054  - add descriptions of columns to pmap(1) man page
Patch58: procps-3.2.8-pmap-man.patch
#fixes sorting in ps command
Patch59: procps-3.2.8-ps-sort.patch
#fixes #574413
Patch60: procps-3.2.8-pcpu-max-value.patch

BuildRequires: ncurses-devel

%description
The procps package contains a set of system utilities that provide
system information. Procps includes ps, free, skill, pkill, pgrep,
snice, tload, top, uptime, vmstat, w, watch and pdwx. The ps command
displays a snapshot of running processes. The top command provides
a repetitive update of the statuses of running processes. The free
command displays the amounts of free and used memory on your
system. The skill command sends a terminate command (or another
specified signal) to a specified set of processes. The snice
command is used to change the scheduling priority of specified
processes. The tload command prints a graph of the current system
load average to a specified tty. The uptime command displays the
current time, how long the system has been running, how many users
are logged on, and system load averages for the past one, five,
and fifteen minutes. The w command displays a list of the users
who are currently logged on and what they are running. The watch
program watches a running program. The vmstat command displays
virtual memory statistics about processes, memory, paging, block
I/O, traps, and CPU activity. The pwdx command reports the current 
working directory of a process or processes.

%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch26 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1

cp %SOURCE1 .

%build
make SHARED=1 CFLAGS="$RPM_OPT_FLAGS" W_SHOWFROM=-DW_SHOWFROM lib64=%{_lib}

%install
rm -rf %{buildroot}
make ldconfig=true DESTDIR=%{buildroot} lib64=%{_lib} install="install -D" \
	SKIP="/bin/kill /usr/share/man/man1/kill.1" install
mkdir -p %{buildroot}/%{_docdir}/procps-%{version}
# keep 'rpm' happy...
chmod -R u+w %{buildroot}/sbin
chmod -R u+w %{buildroot}/bin
chmod -R u+w %{buildroot}/usr/bin
chmod -R u+w %{buildroot}/lib*

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(0644,root,root,755)
%doc NEWS BUGS TODO FAQ COPYING COPYING.LIB
%attr(755,root,root) /%{_lib}/*
%attr(755,root,root) /bin/ps
%attr(755,root,root) /sbin/sysctl
%attr(755,root,root) /usr/bin/*

%attr(0644,root,root) %{_mandir}/man1/*
%attr(0644,root,root) %{_mandir}/man8/*
%attr(0644,root,root) %{_mandir}/man5/*

%changelog
* Wed Jun 30 2010 Jan Kaluza <jkaluza@redhat.com> 3.2.8-14
- fix #574413 - set max cpu usage in top command according
  to number of threads used by process

* Tue Jun 22 2010 Jan Görig <jgorig@redhat.com> 3.2.8-13
- fixes sorting in ps command (patch created by Petr Šplíchal)

* Tue Jun 1 2010 Jan Görig <jgorig@redhat.com> 3.2.8-12
- #598054 - add descriptions of columns to pmap(1) man page

* Fri May 28 2010 Jan Görig <jgorig@redhat.com> 3.2.8-11
- fix #596948 - vmstat disk device field is not long enough

* Mon Apr 26 2010 Daniel Novotny <dnovotny@redhat.com> 3.2.8-10
- fix #585938 - [abrt] crash in procps-3.2.8-3.fc12

* Tue Apr 20 2010 Daniel Novotny <dnovotny@redhat.com> 3.2.8-9
- fix #581547 - add vmstat -w option for wider output
- fix #583629 - pmap does not display RSS values for a pid
- fix #583625 - document that usernames exceeding column width are substituted with user ID

* Fri Apr 09 2010 Daniel Novotny <dnovotny@redhat.com> 3.2.8-8
- fix #580877 - negative ETIME field in ps

* Thu Apr 01 2010 Daniel Novotny <dnovotny@redhat.com> 3.2.8-7
- fix #578799 - vmstat -SM doesn't work but vmstat -S M does

* Thu Feb 25 2010 Daniel Novotny <dnovotny@redhat.com> 3.2.8-6
- added COPYING and COPYING.LIB to doc

* Mon Feb 22 2010 Daniel Novotny <dnovotny@redhat.com> 3.2.8-5
- fix #564371 -  Enhance top to display in MB vs KB
- fix #565971 -  double free or corruption in ps

* Wed Jan 13 2010 Daniel Novotny <dnovotny@redhat.com> 3.2.8-4
- fix #554674 -  vmstat command with -n and -m does not display header even once
- fix #554721 -  procps states a bug is hit when receiving a signal
- fix #479703 -  [RFE] Additional option for 'top'

* Mon Nov 16 2009 Daniel Novotny <dnovotny@redhat.com> 3.2.8-3
- patch for enabling core file generation (we don't trap the signal anymore)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 11 2009 Daniel Novotny <dnovotny@redhat.com> 3.2.8-1
- new upstream version; rebase patches and drop upstreamed patches

* Wed Apr 29 2009 Daniel Novotny <dnovotny@redhat.com> 3.2.7-28
- fix #498182 -  procps string size issue

* Tue Feb 24 2009 Daniel Novotny <dnovotny@redhat.com> 3.2.7-27
- included -l option in free man page

* Mon Feb 23 2009 Daniel Novotny <dnovotny@redhat.com> 3.2.7-26
- fix requested writes display in partition statistics
  for big-endian machines

* Mon Feb 16 2009 Daniel Novotny <dnovotny@redhat.com> 3.2.7-25
- added cgroup support to ps (Ivana Varekova)

*Tue Feb 03 2009 Daniel Novotny <dnovotny@redhat.com> 3.2.7-24
- slabtop -o should display the info once and then exit (RHEL bug #475963)
- added timestamp to vmstat with new option -t (#476134)

* Wed Jan 07 2009 Adam Jackson <ajax@redhat.com> 3.2.7-23
- procps-3.2.7-vmstat-header.patch: Fix vmstat header to fit on a single line.

* Thu Dec 04 2008 Daniel Novotny <dnovotny@redhat.com> 3.2.7-22
- fix #472783 vmstat -p <partition name> not working
- extended diskstat parameters to unsigned long to avoid overflow

* Mon Sep 01 2008 Tomas Smetana <tsmetana@redhat.com> 3.2.7-21
- rebase patches
- clear screen in top when switching windows
- fix #435453 - errors with man -t formatting of ps man page

* Tue Feb 12 2008 Tomas Smetana <tsmetana@redhat.com> 3.2.7-20
- rebuild (gcc-4.3)

* Thu Jan 24 2008 Tomas Smetana <tsmetana@redhat.com> 3.2.7-19.2
- install slabtop again: kernel was fixed

* Fri Jan 18 2008 Tomas Smetana <tsmetana@redhat.com> 3.2.7-19.1
- rebuild because of errors on x86_64

* Fri Jan 18 2008 Tomas Smetana <tsmetana@redhat.com> 3.2.7-19
- fix #296471 - update top man page
- fix #226319 - merge review

* Fri Jan 11 2008 Tomas Smetana <tsmetana@redhat.com> 3.2.7-18
- fix displaying the CPU column as integer (related #354001)
- don't install slabtop -- there's no /proc/slabinfo

* Wed Sep 12 2007 Tomas Smetana <tsmetana@redhat.com> 3.2.7-17
- fix #185994 - top "Cpu0" line never updates when using
  "Single Cpu = Off" option on single processor machine

* Mon Aug 27 2007 Tomas Smetana <tsmetana@redhat.com> 3.2.7-16.1
- bump release

* Mon Aug 27 2007 Tomas Smetana <tsmetana@redhat.com> 3.2.7-16
- fix #255441 - ps requires libselinux-devel to display security contexts

* Thu Aug 23 2007 Tomas Smetana <tsmetana@redhat.com> 3.2.7-15.1
- rebuild

* Mon Aug 20 2007 Tomas Smetana <tsmetana@redhat.com> 3.2.7-15
- fix #244960 - ps manpage formatted incorrectly
- update license tag

* Mon Jun 18 2007 Tomas Smetana <tsmetana@redhat.com> 3.2.7-14
- fix #244152 ps truncates eip and esp to 32-bit values on 64-bit systems

* Tue May 22 2007 Tomas Smetana <tsmetana@redhat.com> 3.2.7-13
- fix #208217 - ps does not accept '+' in sort specifier

* Wed Apr 25 2007 Tomas Smetana <tsmetana@redhat.com> 3.2.7-12
- fix #183029 - watch ignores multibyte characters
- fix #222251 - STIME column can jitter
- fix array overflow in sysctl

* Tue Apr  3 2007 Karel Zak <kzak@redhat.com> 3.2.7-11
- fix #234546 - 'w' doesn't give correct information about what's being run.
- fix #228870 - process `sysctl' is using deprecated sysctl
- cleanup spec file

* Mon Feb  5 2007 Karel Zak <kzak@redhat.com> 3.2.7-10
- fix #212637 - sysctl using deprecated syscall
- fix #140975 - top corrupts screen when sorting on first column

* Tue Jan 30 2007 Karel Zak <kzak@redhat.com> 3.2.7-9
- fix procps_version in FAQ patch (thanks to Ian Kent)

* Wed Sep 27 2006 Karel Zak <kzak@redhat.com> 3.2.7-8
- remove zombie patch (needs more investigation)
- fix #208100 - top command with '-c' option become not to display list of tasks
- fix #199174 - top returns with exit code 1 even if no error occurs

* Tue Sep 19 2006 Karel Zak <kzak@redhat.com> 3.2.7-7
- fix #206551 - top fails to convert to cpu single mode when hit '1'

* Tue Sep  5 2006 Karel Zak <kzak@redhat.com> 3.2.7-6
- fix minor bug in procps-3.2.6-top-env-cpuloop.patch

* Fri Aug  7 2006 Karel Zak <kzak@redhat.com> - 3.2.7-5
- fix #189349 - 32bit vmstat on 64bit kernel

* Thu Aug  3 2006 Karel Zak <kzak@redhat.com> - 3.2.7-4
- fix #139827 - ps(1) outputs a multi-threads process as a defunct process.

* Wed Jul 19 2006 Karel Zak <kzak@redhat.com> - 3.2.7-3
- spec file cleanup

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.2.7-2.1
- rebuild

* Mon Jul 10 2006 Karel Zak <kzak@redhat.com> 3.2.7-2
- fix #134516 - ps ignores /proc/#/cmdline if contents 2047 bytes

* Mon Jul 10 2006 Karel Zak <kzak@redhat.com> 3.2.7-1
- upgrade to 3.2.7 (and sync patches)

* Thu Jun  1 2006 Karel Zak <kzak@redhat.com> 3.2.6-4
- fix #191493 - watch -n doesn't handle large integers properly
- fix #186017 - top "Cpu0" line never updates on single processor machine
                (bugfix added to the 'remcpu' patch)
- fix #168444 - memory usage conflicts with /proc/meminfo
- fix #174619 - top reports wrong values for CPU(s) in batch mode
- fix #185299 - cpu steal time support

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.2.6-3.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.2.6-3.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Dec 13 2005 Dan Walsh <dwalsh@redhat.com> 3.2.6-3
- Translate context

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Nov  8 2005 Karel Zak <kzak@redhat.com> 3.2.6-2
- fix #157725 - sysctl -A returns an error

* Mon Oct 31 2005 Karel Zak <kzak@redhat.com> 3.2.6-1
- update to new upstream release

* Wed Oct 12 2005 Karel Zak <kzak@redhat.com> 3.2.5-8
- fix #170083 - Top showing bad cpu usage numbers

* Tue Sep  6 2005 Karel Zak <kzak@redhat.com> 3.2.5-7
- improve procps-3.2.5-sysctl-writeonly.patch
- fix #161449 - "top" ignores user and system toprc
- fix #161559 - top segfaults when resizing console
- fix #160796 - vmstat crashes when accessing LVM partition
- fix #161303 - 'top' failed when remove cpus

* Tue May 10 2005 Karel Zak <kzak@redhat.com> 3.2.5-6
- fix permissions in the spec install section

* Tue May 10 2005 Karel Zak <kzak@redhat.com> 3.2.5-5
- fix debuginfo

* Tue Apr 26 2005 Karel Zak <kzak@redhat.com> 3.2.5-4
- fix #144459 - sysctl reports error: unknown error <...> reading key '<key>'
  (now sysctl doesn't read data from write-only /proc/sys files)

* Thu Mar 17 2005 Karel Zak <kzak@redhat.com> 3.2.5-3
- fix top crashes when terminal window is resized (#149319)

* Sat Mar  5 2005 Karel Zak <kzak@redhat.com> 3.2.5-2
- rebuilt

* Tue Feb  1 2005 Karel Zak <kzak@redhat.com> 3.2.5-1
- update to new upstream 3.2.5
- recreate selinux patch
- remove errno, slabinfo21 and fullpath patches -- all fixed by upstream

* Mon Jan 25 2005 Karel Zak <kzak@redhat.com> 3.2.4-4
- pmap truncates filenames of mappings (#142751)

* Mon Jan 24 2005 Karel Zak <kzak@redhat.com> 3.2.4-3
- add support for /proc/slabinfo 2.1 (#145369)

* Fri Jan  7 2005 Karel Zak <kzak@redhat.com> 3.2.4-2
- fix sysctl errno usage (#144459)

* Wed Dec  1 2004 Karel Zak <kzak@redhat.com> 3.2.4-1
- update to new upstream release

* Mon Nov  1 2004 Karel Zak <kzak@redhat.com> 3.2.3-6
- update FAQ
- update spec description
- fix text in .noproc patch
- fix segv fault if cpu number exceeding 38 (#137159)

* Tue Sep 28 2004 Dan Walsh <dwalsh@redhat.com> 3.2.3-5
- Fix terminal handling when /proc is not available.
- Patch provided by Karel Zak

* Thu Sep 16 2004 Dan Walsh <dwalsh@redhat.com> 3.2.3-4
- Fix spec file to use makefile

* Mon Aug 30 2004 Dan Walsh <dwalsh@redhat.com> 3.2.3-3
- Fix batch mode to use dumb terminal

* Tue Aug 17 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- fix building as non-root, patch from Steve G <linux_4ever@yahoo.com>

* Tue Aug 10 2004 Dan Walsh <dwalsh@redhat.com> 3.2.3-1
- Latest from Upstream

* Tue Jul 20 2004 Dan Walsh <dwalsh@redhat.com> 3.2.2-2
- Reformat ps man page

* Mon Jul 19 2004 Dan Walsh <dwalsh@redhat.com> 3.2.2-1
- Update to upstream version.

* Sat Jun 26 2004 Dan Walsh <dwalsh@redhat.com> 3.2.1-7
- Add patch to display vm_size when STATSIZE env set

* Tue Jun 15 2004 Alan Cox <alan@redhat.com> 3.2.1-6
- Removed broken SELinux patch to w
- Added a better alternative whereby we get less data but don't fall for
  vanished processes when SELinux is running

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jun 14 2004 Dan Walsh <dwalsh@redhat.com> 3.2.1-5
- Fix FAQ Line

* Mon Apr 09 2004 Colin Walters <walters@redhat.com> 3.2.1-4
- Add little patch to make w/who work when getattr access
  to /proc/<pid> for the user's login process is denied

* Sun Mar 28 2004 Dan Walsh <dwalsh@redhat.com> 3.2.1-3
- bump for rhel3

* Sun Mar 28 2004 Dan Walsh <dwalsh@redhat.com> 3.2.1-2
- Removed addtask patch, very buggy,
- Added FAQ to docdir

* Sun Mar 28 2004 Dan Walsh <dwalsh@redhat.com> 3.2.1-1
- Update to latest from upstream

* Thu Mar 25 2004 Dan Walsh <dwalsh@redhat.com> 3.2.0-3
- Add addtask patch to total all threads times.

* Wed Mar 17 2004 Dan Walsh <dwalsh@redhat.com>
- Clean up spec file.

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 24 2004 Dan Walsh <dwalsh@redhat.com> 3.2.0-1
- New version from upstream

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jan 22 2004 Dan Walsh <dwalsh@redhat.com> 3.1.15-3
- Match -Z to --context

* Wed Jan 21 2004 Dan Walsh <dwalsh@redhat.com> 3.1.15-2
- Add back in -Z support

* Wed Jan 21 2004 Alexander Larsson <alexl@redhat.com> 3.1.15-1
- upgrade to procps3
- Some regressions, see bug #114012

* Tue Jan 20 2004 Dan Walsh <dwalsh@redhat.com> 2.0.17-7
- Remove LIBCURSES from skill and sysctl

* Wed Dec  10 2003 Dan Walsh <dwalsh@redhat.com> 2.0.17-6
- Turn on SELinux

* Mon Dec  8 2003 Alexander Larsson <alexl@redhat.com> 2.0.17-5
- Fix top total percentages (#109484)

* Wed Oct 15 2003 Dan Walsh <dwalsh@redhat.com> 2.0.17-4
- Turn off selinux

* Wed Oct 15 2003 Dan Walsh <dwalsh@redhat.com> 2.0.17-3.sel
- Fix help message

* Thu Oct 9 2003 Dan Walsh <dwalsh@redhat.com> 2.0.17-2.sel
- Turn on selinux

* Fri Oct  3 2003 Alexander Larsson <alexl@redhat.com> 2.0.17-1
- Update to 2.0.17, drop upstream patches, forward port remaining patches

* Fri Sep 5 2003 Dan Walsh <dwalsh@redhat.com> 2.0.13-11
- Turn off selinux

* Thu Aug 28 2003 Dan Walsh <dwalsh@redhat.com> 2.0.13-10.sel
- Add -Z switch for SELinux

* Sun Aug 17 2003 Doug Ledford <dledford@redhat.com> 2.0.13-9E
- Add patch to recognize irq and softirq time accounting in kernels that
  support this feature

* Mon Aug 11 2003 Alexander Larsson <alexl@redhat.com> 2.0.13-8
- rebuild

* Mon Aug 11 2003 Alexander Larsson <alexl@redhat.com> 2.0.13-7E
- Add swapped patch from rik van riel

* Wed Aug  6 2003 Alexander Larsson <alexl@redhat.com> 2.0.13-6
- rebuild

* Wed Aug  6 2003 Alexander Larsson <alexl@redhat.com> 2.0.13-5E
- Update iowait patch (#101657)
- Add wchan 64bit patch from Mark DeWandel

* Mon Jul 28 2003 Dan Walsh <dwalsh@redhat.com> 2.0.13-4E
- Add SELinux patch

* Wed Jul 16 2003 Matt Wilson <msw@redhat.com> 2.0.13-3E
- display iowait with procps-2.0.13-iowait.patch (#99061)

* Fri Jul 11 2003 Alexander Larsson <alexl@redhat.com> 2.0.13-2E
- Disable linuxthreads thread hack

* Mon Jul  7 2003 Alexander Larsson <alexl@redhat.com> 2.0.13-1E
- rebuild

* Fri Jul  4 2003 Alexander Larsson <alexl@redhat.com> 2.0.13-1
- update to 2.0.13
- Re-merged ntpl patch
- Add hertz fix from Ernie Petrides <petrides@redhat.com>

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri May 23 2003 Alexander Larsson <alexl@redhat.com> 2.0.12-1
- Update to 2.0.12
- Add patch to fix segfault on ps axl (#91453)

* Fri Mar 14 2003 Alexander Larsson <alexl@redhat.com> 2.0.11-7
- Add patch that fixes negative priorities in top.

* Thu Feb 20 2003 Alexander Larsson <alexl@redhat.com> 2.0.11-6
- New NPTL patch:
- Added skipthreads optimization to top
- Don't read threads in 'w'

* Thu Feb 20 2003 Alexander Larsson <alexl@redhat.com> 2.0.11-5
- Update the NPTL patch since the kernel /proc was fixed
- For kernels >= 2.4.20-2.50

* Mon Feb 17 2003 Alexander Larsson <alexl@redhat.com> 2.0.11-4
- Update nptl patch to new /proc layout. 

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 2.0.11-3
- rebuilt

* Wed Jan 22 2003 Alexander Larsson <alexl@redhat.com> 2.0.11-2
- Created nptl patch after discussion with ingo and arjan

* Tue Jan 21 2003 Alexander Larsson <alexl@redhat.com> 2.0.11-1
- Update to 2.0.11

* Mon Dec 16 2002 Elliot Lee <sopwith@redhat.com> 2.0.10-4
- Fix %%install in changelog

* Tue Nov 19 2002 Jakub Jelinek <jakub@redhat.com> 2.0.10-3
- Fix for Hammer

* Wed Oct 23 2002 Alexander Larsson <alexl@redhat.com> 2.0.10-2
- Remove uninstalled files in %%install. Add pmap to %%files

* Tue Oct  8 2002 Alexander Larsson <alexl@redhat.com> 2.0.10-1
- Update to 2.0.10
- Removed applied patches.

* Mon Aug 12 2002 Alexander Larsson <alexl@redhat.com> 2.0.7-25
- Add patch to protect against idle ticks going backwards. Fixes #71237

* Thu Aug  8 2002 Alexander Larsson <alexl@redhat.com> 2.0.7-24
- Fix saving of sort, fixes #32757
- Fix printing size, fixes #48224
- Fix float decimal point input #58163

* Thu Aug  8 2002 Alexander Larsson <alexl@redhat.com> 2.0.7-23
- Fix unsigned/signed bug. Closes #60998.
- Update threadbadhack to correctly propagate process time to the main thread.

* Wed Aug  7 2002 Alexander Larsson <alexl@redhat.com> 2.0.7-22
- Don't strip binaries

* Fri Jul 12 2002 Alexander Larsson <alexl@redhat.com> 2.0.7-21
- Remove the X11 subpackage

* Mon Jul  1 2002 Alexander Larsson <alexl@redhat.com> 2.0.7-19
- Added patch that fixes #35174

* Wed Jun 26 2002 Alexander Larsson <alexl@redhat.com> 2.0.7-18
- New thread badhack patch. Fixes a segfault.

* Mon Jun 24 2002 Alexander Larsson <alexl@redhat.com> 2.0.7-16
- New thread badhack. Now enabled by default.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun 20 2002 Alexander Larsson <alexl@redhat.com> 2.0.7-14
- Added badhack to support hiding threads

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Apr 15 2002 Bill Nottingham <notting@redhat.com> 2.0.7-12
- add ldconfig in postun section

* Mon Aug 27 2001 Trond Eivind Glomsrod <teg@redhat.com> 2.0.7-11
- Add ncurses-devel as a build dependency (#49562)

* Sat Jul 21 2001 Tim Powers <timp@redhat.com>
- removed applnk entry, one of the things that's cluttering our menus

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Thu Apr  5 2001 Jakub Jelinek <jakub@redhat.com>
- fix AIX style user defined formats (#34833)

* Thu Mar 22 2001 Bill Nottingham <notting@redhat.com>
- add a '-e' to sysctl to ignore errors (#31852)

* Mon Mar  5 2001 Preston Brown <pbrown@redhat.com>
- bigger buffer for reading /proc/stat fixes segfault (#27840)

* Thu Feb  1 2001 Preston Brown <pbrown@redhat.com>
- make sysctl return a value when errors occur (#18820).
- support big UIDs (#22683)

* Mon Jan 22 2001 Helge Deller <hdeller@redhat.com>
- work-around for negative CPU output (Bug #18380)

* Thu Aug 17 2000 Than Ngo <than@redhat.com>
- fix failing in RPM post script (Bug #16226)

* Wed Jul 26 2000 Michael K. Johnson <johnsonm@redhat.com>
- Added Jakub's locale patch

* Fri Jul 14 2000 Michael K. Johnson <johnsonm@redhat.com>
- procps-2.0.7
- integrated all patches except for signames patch, which is broken
  and unnecessary
- See NEWS for changes between 2.0.6 and 2.0.7
- Added patch to correctly install desktop file.  Oops.

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jul 03 2000 Preston Brown <pbrown@redhat.com>
- larger buffers for reading /proc/stat

* Tue Jun 13 2000 Preston Brown <pbrown@redhat.com>
- FHS paths

* Tue May 30 2000 Preston Brown <pbrown@redhat.com>
- add smp, signal name patches from VA Linux.  Thanks guys.

* Mon May 22 2000 Harald Hoyer <harald@redhat.com>
- added sysctl.conf (5) man page

* Wed May 10 2000 Bill Nottingham <notting@redhat.com>
- fix PAGE_SIZE mismatch on ia64

* Sun May  7 2000 Bill Nottingham <notting@redhat.com>
- rebuild with different optimizations for ia64

* Fri Mar 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- rebuild with current ncurses

* Tue Mar  7 2000 Bill Nottingham <notting@redhat.com>
- fix end-of-file behavior in sysctl

* Mon Feb 07 2000 Preston Brown <pbrown@redhat.com>
- wmconfig -> desktop

* Mon Feb  7 2000 Jakub Jelinek <jakub@redhat.com>
- don't try to load System.map (and spit error messages if it does not
  exist) if ps or top are not going to use it, both to speed things up
  and remove the ugly messages when they don't make sense.
- in top, print the possible error messages using standard top SHOWMESSAGE
  (because it will be now printed out when already in terminal mode).

* Thu Feb  3 2000 Matt Wilson <msw@redhat.com>
- added patch to prevent divide by zero on UltraSparc
- gzip man pages

