#!/bin/bash
# "Script para validacao de
#  conexao VPN atraves de ping
#  para o PEER do cliente"


IPCLIENTE="$1"

PING=`ping -q -c10 -W1 -i 0.3 $IPCLIENTE | grep received | awk '{print $4}'`

echo $PING 

### FIM ###
