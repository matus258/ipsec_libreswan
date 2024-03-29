#!/usr/bin/python
import subprocess
import json
import sys
import re
discovery={}
data = []
text_output = ''
json_output = {}
ipsec = subprocess.Popen(('sudo','ipsec','auto','status'), stdout=subprocess.PIPE)
ipsec = subprocess.check_output(('grep', '=='), stdin=ipsec.stdout)

for line in ipsec.split('\n'):
  parsed_line = re.split(r'\s+', re.sub(r'(:|=|,|{.*}|\[\d+\])', '', line))
  while('' in parsed_line):
    parsed_line.remove("")
  if parsed_line:
    tunnel_name=parsed_line[1]
    print(tunnel_name)
    tunnel_id_status = parsed_line[len(parsed_line)-1]
    if tunnel_id_status == '#0':
      tunnel_status = 'Down'
    else:
      tunnel_status = 'UP'
    data.append({'#TUNNEL':tunnel_name,'#STATUS':tunnel_status})

discovery = {'data':data}
print(json.dumps(discovery, indent=2))
  