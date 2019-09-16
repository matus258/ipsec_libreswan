#!/usr/bin/python
import subprocess
import json
import sys
import re

text_output = ''
json_output = {}
ipsec = subprocess.Popen(('sudo','ipsec','auto','status'), stdout=subprocess.PIPE)
ipsec = subprocess.check_output(('grep', '=='), stdin=ipsec.stdout)

for line in ipsec.split('\n'):
  parsed_line = re.split(r'\s+', re.sub(r'(:|=|,|{.*}|\[\d+\])', '', line))
  while('' in parsed_line):
    parsed_line.remove("")
  print(parsed_line)

  