from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = 'XXNAMEXX_step2'
config.General.workArea = 'crabProjectsStep2'

config.section_("JobType")
config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName = 'GEN-SIM-RAW_step2_cfg.py'
config.JobType.maxMemoryMB = 16000
config.JobType.numCores = 8
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.inputDBS = 'phys03'
config.Data.inputDataset = '/XXNAMEXX/XXDATASETXX/USER'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

config.Data.publication = True
config.Data.publishDBS = 'phys03'
config.Data.outLFNDirBase = '/store/group/lpcdark4muon/sD_Model_1025_step2'

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
