#!/usr/bin/bash

echo "Inside RMAN.sh"
# echo "connect_string=$1"
connect_string="sys/Kube#2020@//rman-research:1521/ORCLCDB"
connect_string=$1
command=$2
dbid=$3
return_code=0
if [ $command = "list" ]; then
rman target $connect_string cmdfile=list.rman
return_code=$?
elif [ $command = "backupcontrolfile" ]; then
rman target $connect_string cmdfile=backupcontrolfile.rman
return_code=$?
elif [ $command = "fullbackup" ]; then
rman target $connect_string cmdfile=fullbackup.rman
return_code=$?
elif [ $command = "restore" ]; then
rman target $connect_string cmdfile=fullrestore.rman using "$dbid"
return_code=$?
elif [ $command = "dropdb" ]; then
rman target $connect_string cmdfile=dropdb.rman
return_code=$?
else
echo "command is not yet implemented"
fi

echo "finished"
exit $return_code
