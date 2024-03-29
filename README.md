HiPerGator (HPG)

HiPerGator lectures given by Matt Gitzendanner

Find notes on HiPerGator (Find Matt Gitzendanner's presentations):
training.it.ufl.edu
Find SLURM commands at:
help.rc.ufl.edu
Interactive Jupyter Notebook session that uses HiPerGator!:
jhub.rc.ufl.edu

Location of SLURM example scripts:
/ufrc/data/training/SLURM/*.sh
- for single jobs, grab: single_job.sh
- for parallel jobs, grab: parallel_job.sh

You have a couple main directories:
/	<== where HPG first drops you off
/home/<gatorlink>/	<== CANNOT handle big files (only has 20 GB of storage)
/ufrc/<group>/<gatorlink>	<== can handle 51000 cores!

/ufrc/phz5155/$USER
- parallel file system
- CAN handle 51000 cores, reading and writing to it
- 2 TB limit per group
after ssh’ing into HPG, it will take you to:
/home/$USER
- for me this is: /home/rosedj1
- Get 20GB of space
- Has one server (node) hosting

My groups:
/ufrc/korytov/rosedj1/	<== for particle physics research
/ufrc/phz5155/	<== for computing course
- so I'm part of two different groups

To use class resources, instead of Korytov’s resources:
module load class/phz5155
- each time you want to submit a job, do this command

Development Sessions
When to use a dev session?
- When a job requires multiple cores and maybe a few days to run
- There are 6 dev nodes!

module load ufrc
srundev -h	<== help!
srundev --time=04:00:00	<== begin a 4 hr dev session, with the default 1 processor core and 2 GB of memory
srundev --time=60 --ntasks=1 --cpus-per-task=4 --mem=4gb	<== additional flags
srundev -t 3-0 <== session lasts 3 days
srundev -t 60	<== session lasts 60 min
- default time is 00:10:00 (10 min) and max time is 12:00:00
These are all wrappers for:
srun --partition=hpg2-dev --pty bash -i

Getting CMSSW on HPG!!!
1. Start a dev session
2. source /cvmfs/cms.cern.ch/cmsset_default.sh    <== this makes cmsrel and cmsenv two new aliases for you!
3. Now cmsrel your favorite CMSSW_X_Y_Z

HPG COMMANDS:
id	<== see your user id, your group id, etc.
sbatch <script.sh>	<== submit script.sh to scheduler
sbatch --qos=phz5155-b <script.sh>	<== 
squeue	<== see ALL jobs running
squeue -u rosedj1	<== just see your jobs
squeue -j <job_id>
scancel <job_id>	<== kill a job
sacct	<== 
sstat	<== 
slurmInfo	<== see info about resource utilization; must do: module load ufrc
slurmInfo -p	<== partition, a better summary
slurmInfo -g <group_name>	<== 
srun --mpi=pmix_v2 myApp


In the job summary email, the memory usage is talking about RAM efficiency

Time: 
-t
time limit is 31 days
- It is to our benefit to be accurate with job time
- infinite loops will just waste resources and make you think your job is actually working
- the scheduler might postpone your job if it sees it will delay other people's jobs

Module system organizes file paths
If you want to use common modules on HPG, you must load them first:
module load <module>
module load python
module load python3
module load = ml <== already aliased automagically into HPG
module list	<== list modules
module spider	<== list everything?
module spider cl	<== list everything with cl in name
module purge	<== unloads all modules
ml intel	<== allows you to do "make" commands
module load intel/2018 openmpi/3.1.0	<== compiling
                                                 
Command to make DIGI files:
cmsDriver.py -s DIGI,L1,DIGI2RAW,HLT --datatier GEN-SIM-DIGI-RAW --conditions 100X_upgrade2018_realistic_v10 --eventcontent RAWSIM --era Run2_2018 --filein file:DsTau3Mu_13TeV_MC2018_SIM.root --fileout file:DsTau3Mu_13TeV_MC2018_DIGI.root --python_filename DsTau3Mu_13TeV_MC2018_DIGI.py -n 10 --no_exec --pileup 2018_25ns_ProjectedPileup_PoissonOOTPU --pileup_input dbs:/MinBias_TuneCP5_13TeV-pythia8/RunIISpring18GS-100X_upgrade2018_realistic_v9-v1/GEN-SIM
