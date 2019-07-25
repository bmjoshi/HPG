!/bin/bash
#SBATCH --job-name=test    	# Name for job
#SBATCH -o job_%j.out       # 
#SBATCH --mail-type=ALL
#SBATCH --mail-user=<rosedj1@ufl.edu>
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=100mb	or #SBATCH --mem=1gb
#SBATCH --time=2:00:00 (hh:mm:ss)	or	#SBATCH -t=00:01:00

<SCRIPT STUFF BELOW, e.g.>
hostname
module load python
python -V

#SLURM sbatch directives
#multi-letter directives are double dashes
--nodes=1	# processors
--ntasks
--ntasks-per-node
--ntasks-per-socket
--cpus-per-task (cores per task)
#Memory usage:
--mem=1gb
--mem-per-cpu=1gb
--distribution
Long option	short option	description
--nodes=1	-N	request num of servers
--ntasks=1	-n	num tasks that job will use (useful for MPI applications)
--cpus-per-task=8	-c

#If you invest in 10 cores, burst qos can use up to 90 cores!
#SBATCH --nodes=1

#Task Arrays
#SBATCH --array=1-200%10	<== run on 10 jobs at a time to be nice
$SLURM_ARRAY_TASK_ID 
%A: job id
%a: task id
