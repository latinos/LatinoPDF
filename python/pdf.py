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
        #try:
            #ROOT.gROOT.LoadMacro(cmssw_base+'/src/HWWAnalysis/ShapeAnalysis/python/tree/WW2jVar.C+g')
        #except RuntimeError:
            #ROOT.gROOT.LoadMacro(cmssw_base+'/src/HWWAnalysis/ShapeAnalysis/python/tree/WW2jVar.C++g')
        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000

        for i in xrange(nentries):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed.'

            x1 = itree.x1

            #WW2j = ROOT.WW2j(pt1, pt2, eta1, eta2, phi1, phi2,    jetpt1, jetpt2, jeteta1, jeteta2, jetphi1, jetphi2)

            #w1[0]   = WW2j.Mljcloser()
            #w2[0]  = WW2j.Mljfarther()

            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
