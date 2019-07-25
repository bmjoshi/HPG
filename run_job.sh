#!/bin/bash
#SBATCH --job-name=jobrun    # Job name
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -o test_output.out
#SBATCH --mail-user=bm163@ufl.edu   # Where to send mail
#SBATCH --cpus-per-task=8            # Number of CPU cores per task
#SBATCH --time=72:00:00               # Time limit hrs:min:sec
#SBATCH --output=/cms/data/store/user/t2/users/bm163/Test/serial_test_%j.out   # Standard output and error log

pwd; hostname; date

echo "Generating MinBias events..."

filename=$1
echo $filename
cmsRun MinBias_13TeV_config.py outputFile=$filename
date
