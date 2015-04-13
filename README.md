# LatinoPDF
PDF uncertainty tool

    it first adds the weights for pdf variation as if it was a module of the gardener
    
    then it is used in plot/efficiency   

NB: 

    to be "git cloned" under LatinoAnalysis, to be able to use the gardener


Use cmssw LHAPDF:

    /cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/5.9.1/lib/libLHAPDF.a
    check where this library is
    the code automatically creates a symbolic link, but it has to be consistent!
     
     
Example:

    sower.py pdfvarfiller    input.root   output.root
    sower.py pdfvarfiller    ../../LatinoTrees/AnalysisStep/test/latino_stepB_latinosYieldSkim_MC_ggHww_numEvent200.root   output.root


where:

    /home/amassiro/Cern/Code/Latino/LatinoPDF
    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/CMSSW_7_3_3/src/LatinoAnalysis

    