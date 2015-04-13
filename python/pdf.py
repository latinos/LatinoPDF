#
#
#      _ \   __ \   ____| 
#     |   |  |   |  |     
#     ___/   |   |  __|   
#    _|     ____/  _|     
#                         
#   
#   


from LatinoAnalysis.Gardener.gardening import TreeCloner
import numpy
import ROOT
import sys
import optparse
import re
import warnings
import os.path
from array import array;

class PDFVarFiller(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Add PDF weights'''

    def addOptions(self,parser):
        pass

    def checkOptions(self,opts):
        pass

    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)
        newbranches = ['w1', 'w2']
        self.clone(output,newbranches)

        w1    = numpy.ones(1, dtype=numpy.float32)
        w2    = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('w1'  , w1 , 'w1/F')
        self.otree.Branch('w2'  , w2 , 'w2/F')

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        #what is self.itree? what is self.otree?
        itree     = self.itree
        otree     = self.otree

        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            #ROOT.gSystem.Load('/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/5.9.1-cms4/lib/libLHAPDF.a')
            #import ctypes
            #la = ctypes.CDLL("/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/5.9.1-cms4/lib/python2.7/site-packages/_lhapdf.so", 0x100 | 0x2)
            #ROOT.gSystem.Load('/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/5.9.1-cms4/lib/python2.7/site-packages/_lhapdf.so')
            #ROOT.gInterpreter.AddIncludePath('/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/5.9.1-cms4/include')

            #ROOT.gSystem.Load('/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/6.1.5/lib/libLHAPDF.so')
            #ROOT.gInterpreter.AddIncludePath('/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/6.1.5/include')

            #ROOT.gSystem.Load('/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/5.9.1/lib/python2.7/site-packages/_lhapdf.so')
            #ROOT.gSystem.Load('/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/5.9.1/lib/python2.7/site-packages/_lhapdf')
            #ln -s /cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/5.9.1/lib/libLHAPDF.a 
            ROOT.gSystem.Load('libLHAPDF.so')
            ROOT.gInterpreter.AddIncludePath('/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/5.9.1/include')
                
            
            #ROOT.gSystem.Load('/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/6.1.5-odfocd/lib/libLHAPDF.so')
            #ROOT.gInterpreter.AddIncludePath('/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/6.1.5-odfocd/include')
            
            #ROOT.gSystem.Load('/cvmfs/cms.cern.ch/slc6_amd64_gcc491/external/lhapdf6/6.1.5-cms/lib/libLHAPDF.so')
            #ROOT.gInterpreter.AddIncludePath('/cvmfs/cms.cern.ch/slc6_amd64_gcc491/external/lhapdf6/6.1.5-cms/include')
            
            #ROOT.gSystem.Load('/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf6/6.1.5-cms/lib/libLHAPDF.so')
            #ROOT.gInterpreter.AddIncludePath('/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf6/6.1.5-cms/include')
            
            #ROOT.gSystem.Load('/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf6/6.1.5/lib/libLHAPDF.so')
            #ROOT.gInterpreter.AddIncludePath('/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf6/6.1.5/include')
            
            #ROOT.gSystem.Load('/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/6.1.5/lib/python2.7/site-packages/lhapdf.so')
            #ROOT.gInterpreter.AddIncludePath('/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/6.1.5/include')
            
            
            
            
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/LatinoPDF/python/pdf.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/LatinoPDF/python/pdf.C++g')
        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000

        PDF = ROOT.PDF()

        for i in xrange(nentries):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed.'

            x1   = itree.pdfx1
            id1  = itree.pdfid1
            pdf1 = itree.pdfx1PDF
            x2   = itree.pdfx2
            id2  = itree.pdfid2
            pdf2 = itree.pdfx2PDF
            scale = itree.pdfscalePDF

            PDF.SetIncoming(x1, x2, id1, id2, pdf1, pdf2, scale)

            w1[0]   = PDF.w1()
            
            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
