
#/bin/bash
#this script outputs the ip address and hostname of a machine
greeting="this is a script. Hello!"
echo $greeting, thanksfor joining us!
echo '$greeting,thanks fr joiing us! You owe me $20'
echo "$greeting,thanks for joining us!"
echo "$greeting, you owe me \$20"
echo Machine Type: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working Dir: $PWD
echo Session Length: $SECONDS
echo Home Dir: $HOME
=$(ip a | grep 'dynamic ens192'| awk '{print$2}')
echo My IP is $a
