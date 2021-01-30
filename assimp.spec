#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : assimp
Version  : 3.3
Release  : 8
URL      : file:///insilications/build/clearlinux/packages/assimp/assimp-v3.3.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/assimp/assimp-v3.3.tar.gz
Summary  : Import various well-known 3D model formats in an uniform manner.
Group    : Development/Tools
License  : GPL-2.0+
Requires: assimp-bin = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : double-conversion-dev
BuildRequires : double-conversion-staticdev
BuildRequires : doxygen
BuildRequires : freeglut-dev
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : googletest-dev
BuildRequires : mesa-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pugixml-dev
BuildRequires : python3
BuildRequires : qtbase-extras
BuildRequires : utf8cpp-dev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
See Readme.md

%package bin
Summary: bin components for the assimp package.
Group: Binaries

%description bin
bin components for the assimp package.


%package dev
Summary: dev components for the assimp package.
Group: Development
Requires: assimp-bin = %{version}-%{release}
Provides: assimp-devel = %{version}-%{release}
Requires: assimp = %{version}-%{release}

%description dev
dev components for the assimp package.


%package staticdev
Summary: staticdev components for the assimp package.
Group: Default
Requires: assimp-dev = %{version}-%{release}

%description staticdev
staticdev components for the assimp package.


%prep
%setup -q -n assimp
cd %{_builddir}/assimp

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612046279
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
# -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
# gcc: -feliminate-unused-debug-types -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export CXXFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC"
#
export FCFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
export FFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
export CFFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
#
export LDFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
unset CCACHE_DISABLE
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
## altflags1 end
%cmake .. -DASSIMP_LIB_INSTALL_DIR=lib64 \
-DCMAKE_INSTALL_LIBDIR=lib64 \
-DBUILD_SHARED_LIBS=OFF \
-DASSIMP_DOUBLE_PRECISION=OFF \
-DASSIMP_BUILD_TESTS=OFF
make  %{?_smp_mflags}  -j12 V=1 VERBOSE=1
popd
mkdir -p clr-build-special
pushd clr-build-special
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
# -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
# gcc: -feliminate-unused-debug-types -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export CXXFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC"
#
export FCFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
export FFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
export CFFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
#
export LDFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
unset CCACHE_DISABLE
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
## altflags1 end
%cmake .. -DASSIMP_LIB_INSTALL_DIR=lib64 \
-DCMAKE_INSTALL_LIBDIR=lib64 \
-DBUILD_SHARED_LIBS=OFF \
-DASSIMP_DOUBLE_PRECISION=OFF \
-DASSIMP_BUILD_TESTS=OFF
make  %{?_smp_mflags}  -j12 V=1 VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1612046279
rm -rf %{buildroot}
pushd clr-build-special
%make_install_special  || :
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/assimp

%files dev
%defattr(-,root,root,-)
/usr/include/assimp/BaseImporter.h
/usr/include/assimp/Bitmap.h
/usr/include/assimp/BlobIOSystem.h
/usr/include/assimp/ByteSwapper.h
/usr/include/assimp/ColladaMetaData.h
/usr/include/assimp/Compiler/poppack1.h
/usr/include/assimp/Compiler/pstdint.h
/usr/include/assimp/Compiler/pushpack1.h
/usr/include/assimp/CreateAnimMesh.h
/usr/include/assimp/DefaultIOStream.h
/usr/include/assimp/DefaultIOSystem.h
/usr/include/assimp/DefaultLogger.hpp
/usr/include/assimp/Defines.h
/usr/include/assimp/Exceptional.h
/usr/include/assimp/Exporter.hpp
/usr/include/assimp/GenericProperty.h
/usr/include/assimp/Hash.h
/usr/include/assimp/IOStream.hpp
/usr/include/assimp/IOStreamBuffer.h
/usr/include/assimp/IOSystem.hpp
/usr/include/assimp/Importer.hpp
/usr/include/assimp/LineSplitter.h
/usr/include/assimp/LogAux.h
/usr/include/assimp/LogStream.hpp
/usr/include/assimp/Logger.hpp
/usr/include/assimp/MathFunctions.h
/usr/include/assimp/MemoryIOWrapper.h
/usr/include/assimp/NullLogger.hpp
/usr/include/assimp/ParsingUtils.h
/usr/include/assimp/Profiler.h
/usr/include/assimp/ProgressHandler.hpp
/usr/include/assimp/RemoveComments.h
/usr/include/assimp/SGSpatialSort.h
/usr/include/assimp/SceneCombiner.h
/usr/include/assimp/SkeletonMeshBuilder.h
/usr/include/assimp/SmallVector.h
/usr/include/assimp/SmoothingGroups.h
/usr/include/assimp/SmoothingGroups.inl
/usr/include/assimp/SpatialSort.h
/usr/include/assimp/StandardShapes.h
/usr/include/assimp/StreamReader.h
/usr/include/assimp/StreamWriter.h
/usr/include/assimp/StringComparison.h
/usr/include/assimp/StringUtils.h
/usr/include/assimp/Subdivision.h
/usr/include/assimp/TinyFormatter.h
/usr/include/assimp/Vertex.h
/usr/include/assimp/XMLTools.h
/usr/include/assimp/XmlParser.h
/usr/include/assimp/ZipArchiveIOSystem.h
/usr/include/assimp/aabb.h
/usr/include/assimp/ai_assert.h
/usr/include/assimp/anim.h
/usr/include/assimp/camera.h
/usr/include/assimp/cexport.h
/usr/include/assimp/cfileio.h
/usr/include/assimp/cimport.h
/usr/include/assimp/color4.h
/usr/include/assimp/color4.inl
/usr/include/assimp/commonMetaData.h
/usr/include/assimp/config.h
/usr/include/assimp/defs.h
/usr/include/assimp/fast_atof.h
/usr/include/assimp/importerdesc.h
/usr/include/assimp/light.h
/usr/include/assimp/material.h
/usr/include/assimp/material.inl
/usr/include/assimp/matrix3x3.h
/usr/include/assimp/matrix3x3.inl
/usr/include/assimp/matrix4x4.h
/usr/include/assimp/matrix4x4.inl
/usr/include/assimp/mesh.h
/usr/include/assimp/metadata.h
/usr/include/assimp/pbrmaterial.h
/usr/include/assimp/postprocess.h
/usr/include/assimp/qnan.h
/usr/include/assimp/quaternion.h
/usr/include/assimp/quaternion.inl
/usr/include/assimp/scene.h
/usr/include/assimp/texture.h
/usr/include/assimp/types.h
/usr/include/assimp/vector2.h
/usr/include/assimp/vector2.inl
/usr/include/assimp/vector3.h
/usr/include/assimp/vector3.inl
/usr/include/assimp/version.h
/usr/lib64/cmake/assimp-5.0/assimpConfig.cmake
/usr/lib64/cmake/assimp-5.0/assimpConfigVersion.cmake
/usr/lib64/cmake/assimp-5.0/assimpTargets-relwithdebinfo.cmake
/usr/lib64/cmake/assimp-5.0/assimpTargets.cmake
/usr/lib64/pkgconfig/assimp.pc

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libassimp.a
