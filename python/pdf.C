
#include <TMath.h>
#include <algorithm>
#include <TLorentzVector.h>
#include <iostream>

// #include "LHAPDF.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Candidate/interface/CompositeCandidate.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"

class PDF {
public:
 //! constructor
 PDF(float x1, float x2, float id1, float id2, float pdf1, float pdf2, float scale);
 virtual ~PDF() {};
 
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
PDF::PDF(float x1, float x2, float id1, float id2, float pdf1, float pdf2, float scale) {

 _x1   = x1;
 _id1  = id1;
 _pdf1 = pdf1;
 
 _x2   = x2;
 _id2  = id2;
 _pdf2 = pdf2;

 _scale = scale;
 
}

//! functions

float PDF::w1(){
 
 float weight = LHAPDF::xfx (_x1, _scale, _id1) * LHAPDF::xfx (_x2, _scale, _id2) ;
 
 return -1;
 
}





