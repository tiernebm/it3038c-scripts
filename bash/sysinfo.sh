#!/bin/bash
#EMAIL our info
emailaddress=tiernebm@mail.uc.edu
today=$(date)
ip=$(ip a | grep 'dynamic ens192'| awk '{print$2}')
content="User: \t $USER \n HOSTNAME: $HOSTNAME IP: $ip DATE: $today"
mail -s "192.168.33.12" $emailaddress <<< $(echo -e $content)
