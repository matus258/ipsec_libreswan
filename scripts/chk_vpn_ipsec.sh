#!/bin/bash
# Script para monitoria de VPN IPSEC
# Necessário template Template BR Baseline IPSEC

# Verifica status da VPN

ipsec status | grep "==" | grep "$1" | egrep "#0$" | grep "$1" &> /dev/null
RETURN=$?


if [ $RETURN == "1" ]
then

  # Caso o retorno seja "1" indica que o tunel está no ok
  echo "1"

else

  if [ $RETURN == "0" ]
  then

    # Caso o retorno seja "0" indica que o tunel está fora do ar ou com algum problema
    echo "0"

  fi

fi


### FIM ###
