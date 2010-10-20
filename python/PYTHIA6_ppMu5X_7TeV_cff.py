import FWCore.ParameterSet.Config as cms

configurationMetadata = cms.untracked.PSet(
        version = cms.untracked.string('$Revision: 1.3 $'),
        name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/PYTHIA6_ppMu5X_7TeV_cff.py,v $'),
        annotation = cms.untracked.string('Summer09: Pythia6-MinBias at 10TeV with Muon preselection (Loose cut), +decay-inflight, 10TeV, D6T tune')
)

from Configuration.Generator.PythiaUEZ2Settings_cfi import *

generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(7000.0),
    crossSection = cms.untracked.double(48440000000.0),
    filterEfficiency = cms.untracked.double(0.00019),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('MSEL=1           ! User defined processes', 
            'MSTJ(22)=4       ! Decay unstable particles in a cylinder', 
            'PARJ(73)=1500.   ! max. radius for MSTJ(22)=4', 
            'PARJ(74)=3000.   ! max. Z for MSTJ(22)=4', 
            'MDCY(C130,1)=1   ! decay k0-longs', 
            'MDCY(C211,1)=1   ! decay pions', 
            'MDCY(C321,1)=1   ! decay kaons'),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings',
            'processParameters')
    )
)

mugenfilter = cms.EDFilter("MCSmartSingleParticleFilter",
    Status = cms.untracked.vint32(     1,    1),
    ParticleID = cms.untracked.vint32(13,  -13),
    MinPt = cms.untracked.vdouble(    5, 5),
    MaxEta = cms.untracked.vdouble(   2.5, 2.5),
    MinEta = cms.untracked.vdouble(  -2.5, -2.5),
    MaxDecayRadius = cms.untracked.vdouble(2000.0, 2000.0),
    MaxDecayZ = cms.untracked.vdouble(4000.0, 4000.0),
    MinDecayZ = cms.untracked.vdouble(-4000.0, -4000.0)
)

ProductionFilterSequence = cms.Sequence(generator*mugenfilter)