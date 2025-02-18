#Do not use the spec to build RPMS!!!!

Name:           linux
Version:        5.17
Release:        1%{?dist}
Summary:       The MR-Sun Kernel for Linux (Red Hat-based) Distrobutions

#Group:
License:      FRL
URL:  https://github.com/Morales-Research-Corporation/kernel
Source0:    https://github.com/Morales-Research-Corporation/kernel.git
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:
#Requires:

# This is a placeholder spec in order for tito to package, and we need to build a proper spec for the kernel

%description
Linux Kernel is an open-source kernel for Sun/OS Linux and supports all Linux distributions

%changelog
* Mon May 30 2022 Abdon Morales <abdon.morales@moralesresearch.org> 5.17-1
- Adding new kernel sources for new release (abdon.morales@moralesresearch.org)
- Removing old kernel source with a newer release (r5.17). Release v5.18 will
  be launched on 6/2/2022 (abdon.morales@moralesresearch.org)

* Sun May 29 2022 Abdon Morales <abdon.morales@moralesresearch.org> 5.16.2-1
- Adding missing files for the top-level (/)
  (abdon.morales@moralesresearch.org)
- Updating version number to follow the downstream versioning system (MRI)
  (abdon.morales@moralesresearch.org)
- Added the new vanilla Linux Kernel (5.16.15) with the newest patches for the
  downstream kernel (5.16.2) (abdon.morales@moralesresearch.org)
- Removing 5.16.1 kernel for the new patched kernel from kernel.org -->
  upstream (abdon.morales@moralesresearch.org)

* Thu Mar 10 2022 Abdon Morales <abdon.morales@moralesresearch.org> 5.16.1-1
- Adding new kernel from usptream (as of download, version 5.16.12)
  (abdon.morales@moralesresearch.org)
- Remvoing old kernel from 5.16 (usptream and downstream) with the newer 5.16.1
  (upstream - 5.16.12) (abdon.morales@moralesresearch.org)

* Fri Feb 18 2022 Abdon Morales <abdon.morales@moralesresearch.org> 5.16-1
- Adding new upstream kernel for the main branch with minor patches
  (abdon.morales@moralesresearch.org)
- Removing really old kernel from upstream with a refreshed kernel
  (abdon.morales@moralesresearch.org)

* Tue Dec 28 2021 Abdon Morales <abdon.morales@moralesresearch.org> 5.15.4-1
- Removing unpatched kernel (5.15.3) from the patching branch
- Adding new patched kernel from upstream @ kernel.org
- Incremented version number and changed the name from kernel >> linux 
* Mon Nov 22 2021 Abdon Morales <abdon.morales@moralesresearch.org> 5.15.3-1
- Added the new patched kernel from the upstream repository at kernel.org
  (abdon.morales@moralesresearch.org)

* Mon Nov 22 2021 Abdon Morales <abdon.morales@moralesresearch.org> 5.15.2-1
- Oops, forgot to change the code name for the kernel
  (abdon.morales13_2022@outlook.com)
- Adding new patched kernel to our repo and main branch
  (abdon.morales13_2022@outlook.com)
- Removing the old kernel and adding the new patched kernel from upstream
  (abdon.morales13_2022@outlook.com)

* Sat Nov 06 2021 Abdon Morales Jr <abdon.morales@moralesresearch.org> 5.15.1-1
- Adding kernel with new improvements from upstream patch kernel
  (abdon.morales@moralesresearch.org)
- Removing old kernel (v5.15.0) and adding new patched kernel
  (abdon.morales@moralesresearch.org)

* Tue Nov 02 2021 Abdon Morales <abdon.morales@moralesresearch.org> 5.15.0-1
- Update kernel.spec (abdon.morales13_2022@outlook.com)
- Create README.md (abdon.morales13_2022@outlook.com)
- Adding new upstream Linux kernel, we will release LTS kernels, but with some
  support (abdon.morales13_2022@outlook.com)
- Removing old kernel for the new vanilla Linux kernel, we will stop providing
  patches and will based on the upstream branch
  (abdon.morales13_2022@outlook.com)

* Tue Aug 31 2021 Abdon Morales <abdon.morales@moralesresearch.org> 5.13.7-1
- Adding minor patches for final small release for 5.13 and moving foward to
  release 5.14
  ------------------------------------------------------------------
  (abdon.morales13_2022@outlook.com)
- Removing old revised kernel (5.13.6) (abdon.morales13_2022@outlook.com)

* Sat Aug 28 2021 Abdon Morales <abdon.morales@moralesresearch.org> 5.13.6-1
- Adding new patched kernel for 5.13 (abdon.morales13_2022@outlook.com)

* Sat Aug 14 2021 Abdon Morales <abdon.morales@moralesresearch.org> 5.13.5-1
- Updating README for v5.13.5 (abdon.morales13_2022@outlook.com)
- Adding new kernel source code (v5.13.5) (abdon.morales13_2022@outlook.com)

* Tue Aug 03 2021 Abdon Morales <abdon.morales@moralesresearch.org> 5.13.4-1
- Update kernel.spec (abdon.morales13_2022@outlook.com)
- Update README.md (abdon.morales13_2022@outlook.com)
- Adding new 5.13.4 kernel (abdon.morales13_2022@outlook.com)
- Removing old stable 5.13.3 kernel with newer patched v5.13.4 kernel
  (abdon.morales13_2022@outlook.com)

* Thu Jul 15 2021 Abdon Morales Jr <abdon.morales@moralesresearch.org> 5.13.3-1
- Fixed kernel extravers to mark stable release
  (abdon.morales13_2022@outlook.com)
- Correcting makefile with stable as extraver
  (abdon.morales13_2022@outlook.com)
- Update README.md (abdon.morales13_2022@outlook.com)
- Adding new patch kernel for v5.13 MR-Linux kernel
  (abdon.morales13_2022@outlook.com)
- Removing base stable 5.13.2 kernel for the new 5.13.3 (based on Linux 5.13.2)
  (abdon.morales13_2022@outlook.com)

* Wed Jul 14 2021 Abdon Morales <abdon.morales@moralesresearch.org> 5.13.2-2
- Update kernel.spec (abdon.morales13_2022@outlook.com)
- Update README.md (abdon.morales13_2022@outlook.com)
- Delete release.yml (abdon.morales13_2022@outlook.com)

* Tue Jul 13 2021 Abdon Morales <abdon.morales@moralesresearch.org> 5.13.2-1
- Adding new source code for the following linux release
  (39339393+Server2356@users.noreply.github.com)
- Update README.md (abdon.morales13_2022@outlook.com)

* Mon Jun 28 2021 Abdon Morales <abdon.morales@moralesresearch.org> 5.13.1-1
- Fixing source #0 to point to the git repo and fixed some bugs within the spec
  file (abdon.morales@moralesresearch.org)
- Adding new version number for the kernel (abdon.morales@moralesresearch.org)
- Patching a few errors in the makefiles and Kconfig files (Patch #1)
  (abdon.morales@moralesresearch.org)
- Adding minor release support for future bug fixes
  (abdon.morales13_2022@outlook.com)

* Mon Jun 28 2021 Abdon Morales <abdon.morales@moralesresearch.org> 5.13-1
- Update kernel.spec (abdon.morales13_2022@outlook.com)
- Update README.md (abdon.morales13_2022@outlook.com)
- Removing .sol postfix in order to match releases
  (abdon.morales13_2022@outlook.com)
- We are using one license for the kernel (abdon.morales13_2022@outlook.com)
- Adding missing files after merge commit (abdon.morales@moralesresearch.org)
- Fixing merge conflicts (abdon.morales@moralesresearch.org)
- Fixing merge conflicts for v5.13 release to main/stable
  (abdon.morales@moralesresearch.org)
- Adding remaining files to v5.13 of the Linux-MRC kernel
  (abdon.morales@moralesresearch.org)
- Adding new kernel release (official release v5.13)
  (abdon.morales@moralesresearch.org)
- Update README.md (abdon.morales13_2022@outlook.com)
- Adding missing README (abdon.morales@moralesresearch.org)
- Adding missing license (abdon.morales@moralesresearch.org)
- Adding kernel spec (abdon.morales@moralesresearch.org)
- Removing old kernel and adding new development kernel (Linux 5.13)
  (abdon.morales@moralesresearch.org)
- Releasing Green Obsidian kernel

* Fri Jun 25 2021 Abdon Morales <abdon.morales@moralesresearch.org> 2.3.1-1.sol
- Bug fixes for the 3.x kernel (final MR-Sun Kernel major release)

* Mon May 31 2021 Abdon Morales <abdon.morales13_2022@outlook.com> 2.2.2
- Adding pacthes for some of kernel files
- Updated some of the core architectures (arm, ppc, x86)
* Fri Apr 30 2021 Abdon Morales <abdonmorales@sunoslinux.com> 2.2.1-2
- Updated placeholder spec
- Tito updated with the correct settings
- Small kernel update

* Fri Apr 30 2021 Abdon Morales - 2.2.1
- Updated spec file with placeholder so tito can work correctly
* Thu Apr 29 2021 Abdon Morales - 2.2.0
- Inital package commit for tito/rpm
