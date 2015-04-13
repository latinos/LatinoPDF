
#include <TMath.h>
#include <algorithm>
#include <TLorentzVector.h>
#include <iostream>

// #include "LHAPDF.h"
// #include "LHAPDF-6.1.4/include/LHAPDF/LHAPDF.h"
// #include "/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf/5.9.1-cms4/include/LHAPDF/LHAPDF.h"
#include "LHAPDF/LHAPDF.h"

// #include "DataFormats/HepMCCandidate/interface/GenParticle.h"
// #include "DataFormats/Candidate/interface/CompositeCandidate.h"
// #include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

class PDF {
public:
 //! constructor
 PDF();
 PDF(float x1, float x2, float id1, float id2, float pdf1, float pdf2, float scale);
 virtual ~PDF() {};
 
 void SetIncoming(float x1, float x2, float id1, float id2, float pdf1, float pdf2, float scale);
 
 
 //! functions
 float w1();
 
private:
 //! variables
 float _x1;
 float _id1;
 float _pdf1;
 
 float _x2;
 float _id2;
 float _pdf2;
 
 float _scale;
 
};

//! constructor
PDF::PDF() {
 const int SUBSET = 0 ;
 const std::string NAME = "cteq6ll" ; //"cteq6l1"
 
 LHAPDF::initPDFSet (NAME, LHAPDF::LHPDF, SUBSET) ;
 const int NUMBER = LHAPDF::numberPDF () ;
 std::cout << " NUMBER = " << NUMBER << std::endl;
 LHAPDF::initPDF (0) ;
}


PDF::PDF(float x1, float x2, float id1, float id2, float pdf1, float pdf2, float scale) {

 PDF();
 SetIncoming(x1, x2, id1, id2, pdf1, pdf2, scale);
  
}
 

//! functions

void PDF::SetIncoming(float x1, float x2, float id1, float id2, float pdf1, float pdf2, float scale) {
 
 _x1   = x1;
 _id1  = id1;
 _pdf1 = pdf1;
 
 _x2   = x2;
 _id2  = id2;
 _pdf2 = pdf2;
 
 _scale = scale;
 
}

float PDF::w1(){
 
 float weight = LHAPDF::xfx ((double) _x1, (double) _scale, (int) _id1) * LHAPDF::xfx ((double) _x2, (double) _scale, (int) _id2) ;
//  float weight = LHAPDF::xfx (0.2, 1.23, 1);
//  std::cout << " weight = " << weight << std::endl;
//  weight+=1;
 
 return weight;
 
}





