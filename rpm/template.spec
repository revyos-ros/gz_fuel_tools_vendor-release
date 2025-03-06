%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-gz-fuel-tools-vendor
Version:        0.0.6
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS gz_fuel_tools_vendor package

License:        Apache License 2.0
URL:            https://github.com/gazebosim/gz-fuel-tools
Source0:        %{name}-%{version}.tar.gz

Requires:       gflags-devel
Requires:       jsoncpp-devel
Requires:       libcurl-devel
Requires:       libyaml-devel
Requires:       libzip-devel
Requires:       ros-jazzy-gz-cmake-vendor
Requires:       ros-jazzy-gz-common-vendor
Requires:       ros-jazzy-gz-math-vendor
Requires:       ros-jazzy-gz-msgs-vendor
Requires:       ros-jazzy-gz-tools-vendor
Requires:       ros-jazzy-gz-utils-vendor
Requires:       tinyxml2-devel
Requires:       ros-jazzy-ros-workspace
BuildRequires:  cmake3
BuildRequires:  gflags-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libcurl-devel
BuildRequires:  libyaml-devel
BuildRequires:  libzip-devel
BuildRequires:  ros-jazzy-ament-cmake-core
BuildRequires:  ros-jazzy-ament-cmake-test
BuildRequires:  ros-jazzy-ament-cmake-vendor-package
BuildRequires:  ros-jazzy-gz-cmake-vendor
BuildRequires:  ros-jazzy-gz-common-vendor
BuildRequires:  ros-jazzy-gz-math-vendor
BuildRequires:  ros-jazzy-gz-msgs-vendor
BuildRequires:  ros-jazzy-gz-tools-vendor
BuildRequires:  ros-jazzy-gz-utils-vendor
BuildRequires:  tinyxml2-devel
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-cmake-copyright
BuildRequires:  ros-jazzy-ament-cmake-lint-cmake
BuildRequires:  ros-jazzy-ament-cmake-xmllint
%endif

%description
Vendor package for: gz-fuel_tools9 9.1.1 Gazebo Fuel Tools: Classes and tools
for interacting with Gazebo Fuel

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Thu Mar 06 2025 Addisu Z. Taddese <addisuzt@intrinsic.ai> - 0.0.6-1
- Autogenerated by Bloom

