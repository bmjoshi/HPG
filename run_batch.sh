#srundev -t 60
for i in {1..10}; do
   ofile="\/cms\/data\/store\/user\/t2\/users\/bm163\/minbias2_test$i.root"
   echo sbatch run_job.sh $ofile
done
