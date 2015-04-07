#!/usr/bin/env python

from LatinoAnalysis.Gardener.gardening         import gardener_cli
from LatinoAnalysis.Gardener.gardening         import ModuleManager
#from LatinoAnalysis.Gardener.gardening         import ModuleManager,Pruner,Grafter,AliasGrafter,RootWeighter

# pdf weights
from LatinoAnalysis.LatinoPDF.pdf              import PDFVarFiller


if __name__ == '__main__':

    print "sower"
    
    modules = ModuleManager()

    # new variables
    modules['pdfvarfiller']    = PDFVarFiller()

    gardener_cli( modules )