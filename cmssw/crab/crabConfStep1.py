from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.workArea = 'crabProjectsStep1'
config.General.requestName = 'XXNAMEXX'
config.section_('JobType')
config.JobType.psetName = 'XXCFGXX'
config.JobType.pluginName = 'PrivateMC'
config.JobType.inputFiles = ['XXFILEXX']
config.JobType.allowUndistributedCMSSW = True
config.section_('Data')
config.Data.outputDatasetTag = 'MC_generation_LHE'
config.Data.publishDBS = 'phys03'
config.Data.publication = True
config.Data.unitsPerJob = 1000
config.Data.splitting = 'EventBased'
config.Data.outLFNDirBase = '/store/group/lpcdark4muon/sD_Model_1025'
config.Data.outputPrimaryDataset = 'XXNAMEXX'
config.Data.totalUnits = 10000
config.section_('Site')
config.Site.storageSite = 'T3_US_FNALLPC'
