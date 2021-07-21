#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lwgeom
Version  : 0.2.5
Release  : 30
URL      : https://cran.r-project.org/src/contrib/lwgeom_0.2-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lwgeom_0.2-5.tar.gz
Summary  : Bindings to Selected 'liblwgeom' Functions for Simple Features
Group    : Development/Tools
License  : GPL-2.0
Requires: R-lwgeom-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-sf
Requires: R-sp
Requires: R-units
BuildRequires : R-Rcpp
BuildRequires : R-sf
BuildRequires : R-sp
BuildRequires : R-units
BuildRequires : buildreq-R
BuildRequires : geos-dev
BuildRequires : proj-dev
BuildRequires : sqlite-autoconf-dev

%description
liblwgeom code obtained from from https://github.com/postgis/postgis
git commit d9a98c5be3c8644699220729f11ed48488548bad
configured with:
./configure --without-pgconfig --without-sfcgal --without-libiconv-prefix --without-libintl-prefix --without-json --without-protobuf --without-topology --without-raster

%package lib
Summary: lib components for the R-lwgeom package.
Group: Libraries

%description lib
lib components for the R-lwgeom package.


%prep
%setup -q -c -n lwgeom
cd %{_builddir}/lwgeom

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592415252

%install
export SOURCE_DATE_EPOCH=1592415252
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lwgeom
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lwgeom
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lwgeom
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc lwgeom || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lwgeom/COPYRIGHTS
/usr/lib64/R/library/lwgeom/DESCRIPTION
/usr/lib64/R/library/lwgeom/INDEX
/usr/lib64/R/library/lwgeom/Meta/Rd.rds
/usr/lib64/R/library/lwgeom/Meta/features.rds
/usr/lib64/R/library/lwgeom/Meta/hsearch.rds
/usr/lib64/R/library/lwgeom/Meta/links.rds
/usr/lib64/R/library/lwgeom/Meta/nsInfo.rds
/usr/lib64/R/library/lwgeom/Meta/package.rds
/usr/lib64/R/library/lwgeom/NAMESPACE
/usr/lib64/R/library/lwgeom/NEWS.md
/usr/lib64/R/library/lwgeom/R/lwgeom
/usr/lib64/R/library/lwgeom/R/lwgeom.rdb
/usr/lib64/R/library/lwgeom/R/lwgeom.rdx
/usr/lib64/R/library/lwgeom/help/AnIndex
/usr/lib64/R/library/lwgeom/help/aliases.rds
/usr/lib64/R/library/lwgeom/help/lwgeom.rdb
/usr/lib64/R/library/lwgeom/help/lwgeom.rdx
/usr/lib64/R/library/lwgeom/help/paths.rds
/usr/lib64/R/library/lwgeom/html/00Index.html
/usr/lib64/R/library/lwgeom/html/R.css
/usr/lib64/R/library/lwgeom/tests/azimuth.R
/usr/lib64/R/library/lwgeom/tests/azimuth.Rout.save
/usr/lib64/R/library/lwgeom/tests/dist.R
/usr/lib64/R/library/lwgeom/tests/dist.Rout.save
/usr/lib64/R/library/lwgeom/tests/geod.R
/usr/lib64/R/library/lwgeom/tests/geod.Rout.save
/usr/lib64/R/library/lwgeom/tests/perimeter.R
/usr/lib64/R/library/lwgeom/tests/perimeter.Rout.save
/usr/lib64/R/library/lwgeom/tests/testthat.R
/usr/lib64/R/library/lwgeom/tests/testthat.Rout.save
/usr/lib64/R/library/lwgeom/tests/testthat/test-as_text.R
/usr/lib64/R/library/lwgeom/tests/testthat/test-clockwise.R
/usr/lib64/R/library/lwgeom/tests/testthat/test_lwgeom.R
/usr/lib64/R/library/lwgeom/tests/twkb.R
/usr/lib64/R/library/lwgeom/tests/twkb.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/lwgeom/libs/lwgeom.so
/usr/lib64/R/library/lwgeom/libs/lwgeom.so.avx2
/usr/lib64/R/library/lwgeom/libs/lwgeom.so.avx512
