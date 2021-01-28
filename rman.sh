#!/usr/bin/bash

echo "Inside RMAN.sh"
echo "connect_string=$1"
rman target sys/Kube#2020@//rman-research:1521/ORCLCDB cmdfile=list.rman
echo "finished"
exit 0
