import os
from ROOT import *

rndm = TRandom()

cfg_file = open('MinBias_13TeV_config_test.py','r')

for i in xrange(3):
   cfg_file.seek(0)
   tmp_file = open('MinBias_13TeV_config.py','w+')
   genseed = "process.RandomNumberGeneratorService.generator.initialSeed = "+str(rndm.Integer(1000)+1)
   for line in cfg_file:
      line = line.strip('\n\r')
      if not 'set random seed' in line: tmp_file.write(line)
      else: tmp_file.write(genseed)
      tmp_file.write('\n')
   tmp_file.close()
   print(genseed)
   cmd = "cat MinBias_13TeV_config.py "
   cmd = "sbatch run_jobs.sh \/cms\/data\/store\/user\/t2\/users\/bm163\/Test2\/minbias_2M_output"+str(i+1)+".root"
   os.system(cmd)

cfg_file.close()
