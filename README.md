# LatinoPDF
PDF uncertainty tool

    it first adds the weights for pdf variation as if it was a module of the gardener
    
    then it is used in plot/efficiency   

NB: 

    to be "git cloned" under LatinoAnalysis, to be able to use the gardener


Use cmssw LHAPDF:

    /cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/5.9.1-cms4/bin/lhapdf-config
    export LD_LIBRARY_PATH=`/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/5.9.1-cms4/bin/lhapdf-config --libdir`:$LD_LIBRARY_PATH
    export LD_LIBRARY_PATH=`/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/5.9.1/bin/lhapdf-config --libdir`:$LD_LIBRARY_PATH


    # ???
    scram tool remove lhapdf
    scram setup lhapdf6
    # ???
 
    
Install LHAPDF

    cmsenv
    wget http://www.hepforge.org/archive/lhapdf/LHAPDF-6.1.4.tar.gz -O- | tar xz
    cd LHAPDF-6.1.4
    
    export BOOST_ROOT=/afs/cern.ch/sw/lcg/external/Boost/1.55.0_python2.7/x86_64-slc6-gcc47-opt/
    export BOOST_INCLUDEDIR=/afs/cern.ch/sw/lcg/external/Boost/1.55.0_python2.7/x86_64-slc6-gcc47-opt/include/boost-1_55/
    export BOOST_LIBRARYDIR=$BOOST_ROOT/lib
    export LD_LIBRARY_PATH=$BOOST_LIBRARYDIR:$LD_LIBRARY_PATH
    export BOOSTFLAGS_ENV="-I${BOOST_ROOT}include/boost-1_55"
    export BOOSTLIBS_ENV="-L${BOOST_ROOT}lib -lboost_program_options-gcc47-mt-1_55"
<!--     ./configure  --with-boost=/afs/cern.ch/sw/lcg/external/Boost/1.50.0_python2.6/x86_64-slc5-gcc43-opt/   -->
    ./configure  --with-boost=/afs/cern.ch/sw/lcg/external/Boost/1.55.0_python2.7/x86_64-slc6-gcc47-opt/  -enable-pdfsets=mrst,cteq

    ./configure  --with-boost=/afs/cern.ch/sw/lcg/external/Boost/1.55.0_python2.7/x86_64-slc6-gcc47-opt/  -enable-pdfsets=mrst,cteq  --disable-pyext 

    
<!--     ./configure --prefix=$PWD/../local -->
    make -j 8 && make install
    cd ..

    
Example:

    sower.py pdfvarfiller    input.root   output.root
    sower.py pdfvarfiller    ../../LatinoTrees/AnalysisStep/test/latino_stepB_latinosYieldSkim_MC_ggHww_numEvent200.root   output.root


where:

    /home/amassiro/Cern/Code/Latino/LatinoPDF
    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/CMSSW_7_3_3/src/LatinoAnalysis