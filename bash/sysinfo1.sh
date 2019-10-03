echo "User: $USER"
echo "Hostname: $HOSTNAME"
a=$(ip a | grep 'dynamic ens192'| awk '{print$2}')
echo "IP: $a"
now=$(date)
echo "Date: $now"
