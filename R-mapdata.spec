#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mapdata
Version  : 2.3.1
Release  : 44
URL      : https://cran.r-project.org/src/contrib/mapdata_2.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mapdata_2.3.1.tar.gz
Summary  : Extra Map Databases
Group    : Development/Tools
License  : GPL-2.0
Requires: R-maps
BuildRequires : R-maps
BuildRequires : buildreq-R

%description
Notes on creating new map databases.
1) See the references:
Richard A. Becker, and Allan R. Wilks,
"Maps in S",
emph{AT\&T Bell Laboratories Statistics Research Report [93.2], 1993.}

%prep
%setup -q -n mapdata
cd %{_builddir}/mapdata

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1667333572

%install
export SOURCE_DATE_EPOCH=1667333572
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
