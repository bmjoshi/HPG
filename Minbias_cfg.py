# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: MinBias_13TeV_cfi --conditions auto:startup -s GEN,SIM --datatier GEN-SIM -n 10
# --relval 9000,300 --eventcontent RAWSIM --io MinBias.io --python MinBias.py --no_exec --fileout minbias.root
# Changes made to the main configuration file (source:https://twiki.cern.ch/twiki/bin/view/CMS/Tau3MuBari)

import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from Configuration.StandardSequences.Eras import eras

process = cms.Process('SIM',eras.Run2_2017)
options = VarParsing('analysis')

# Import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2017Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

options.parseArguments()

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2000000)
)

process.outputEvery = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

# Random event generation

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(
    outputEvery = cms.untracked.int32(10),
    numberOfThreads=cms.untracked.uint32(8)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('MinBias_13TeV_pythia8_cfi nevts:50'),
    name = cms.untracked.string('Applications')
)

# Output definition
process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string(options.outputFile),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step'),
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2017_realistic', '')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    crossSection = cms.untracked.double(71.39e+09),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'SoftQCD:nonDiffractive = on',
            'SoftQCD:singleDiffractive = on',
            'SoftQCD:doubleDiffractive = on'),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
        )
	 )

# Add Muon Filter

process.MuFilter = cms.EDFilter("MCSingleParticleFilter",
    MinPt = cms.untracked.vdouble(5.0), #using 2.7 I got 5 over 10000 events
    MaxEta = cms.untracked.vdouble(2.45),
    MinEta = cms.untracked.vdouble(-2.45),
    ParticleID = cms.untracked.vint32(13),
)

process.ProductionFilterSequence = cms.Sequence(process.generator * process.MuFilter)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(
    process.generation_step,
    process.genfiltersummary_step,
    process.simulation_step,
    process.endjob_step,
    process.RAWSIMoutput_step
)

# Set different random numbers seeds every time one runs cmsRun
#from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
#randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
#randSvc.populate()
RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    generator = cms.PSet(
        initialSeed = cms.untracked.uint32(1234),
        engineName = cms.untracked.string('HepJamesRandom')
    )
)

process.RandomNumberGeneratorService.generator.initialSeed = 791

# Filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
