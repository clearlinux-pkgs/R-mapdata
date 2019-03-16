#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mapdata
Version  : 2.3.0
Release  : 6
URL      : https://cran.r-project.org/src/contrib/mapdata_2.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mapdata_2.3.0.tar.gz
Summary  : Extra Map Databases
Group    : Development/Tools
License  : GPL-2.0
Requires: R-maps
BuildRequires : R-maps
BuildRequires : clr-R-helpers

%description
higher-resolution databases.

%prep
%setup -q -c -n mapdata

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530341274

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530341274
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mapdata
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mapdata
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mapdata
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library mapdata|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mapdata/DESCRIPTION
/usr/lib64/R/library/mapdata/INDEX
/usr/lib64/R/library/mapdata/Meta/Rd.rds
/usr/lib64/R/library/mapdata/Meta/data.rds
/usr/lib64/R/library/mapdata/Meta/features.rds
/usr/lib64/R/library/mapdata/Meta/hsearch.rds
/usr/lib64/R/library/mapdata/Meta/links.rds
/usr/lib64/R/library/mapdata/Meta/nsInfo.rds
/usr/lib64/R/library/mapdata/Meta/package.rds
/usr/lib64/R/library/mapdata/NAMESPACE
/usr/lib64/R/library/mapdata/R/mapdata
/usr/lib64/R/library/mapdata/R/mapdata.rdb
/usr/lib64/R/library/mapdata/R/mapdata.rdx
/usr/lib64/R/library/mapdata/data/Rdata.rdb
/usr/lib64/R/library/mapdata/data/Rdata.rds
/usr/lib64/R/library/mapdata/data/Rdata.rdx
/usr/lib64/R/library/mapdata/help/AnIndex
/usr/lib64/R/library/mapdata/help/aliases.rds
/usr/lib64/R/library/mapdata/help/mapdata.rdb
/usr/lib64/R/library/mapdata/help/mapdata.rdx
/usr/lib64/R/library/mapdata/help/paths.rds
/usr/lib64/R/library/mapdata/html/00Index.html
/usr/lib64/R/library/mapdata/html/R.css
/usr/lib64/R/library/mapdata/mapdata/china.G
/usr/lib64/R/library/mapdata/mapdata/china.L
/usr/lib64/R/library/mapdata/mapdata/china.N
/usr/lib64/R/library/mapdata/mapdata/japan.G
/usr/lib64/R/library/mapdata/mapdata/japan.L
/usr/lib64/R/library/mapdata/mapdata/japan.N
/usr/lib64/R/library/mapdata/mapdata/nzHires.G
/usr/lib64/R/library/mapdata/mapdata/nzHires.L
/usr/lib64/R/library/mapdata/mapdata/nzHires.N
/usr/lib64/R/library/mapdata/mapdata/rivers.G
/usr/lib64/R/library/mapdata/mapdata/rivers.L
/usr/lib64/R/library/mapdata/mapdata/rivers.N
/usr/lib64/R/library/mapdata/mapdata/world2Hires.G
/usr/lib64/R/library/mapdata/mapdata/world2Hires.L
/usr/lib64/R/library/mapdata/mapdata/world2Hires.N
/usr/lib64/R/library/mapdata/mapdata/world2Lores.G
/usr/lib64/R/library/mapdata/mapdata/world2Lores.L
/usr/lib64/R/library/mapdata/mapdata/world2Lores.N
/usr/lib64/R/library/mapdata/mapdata/worldHires.G
/usr/lib64/R/library/mapdata/mapdata/worldHires.L
/usr/lib64/R/library/mapdata/mapdata/worldHires.N
/usr/lib64/R/library/mapdata/mapdata/worldLores.G
/usr/lib64/R/library/mapdata/mapdata/worldLores.L
/usr/lib64/R/library/mapdata/mapdata/worldLores.N
