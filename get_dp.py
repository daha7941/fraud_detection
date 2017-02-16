#
# Python program to get a data point from a web site
# if it is a new data point then send it to the web site
#

import requests
import socket
import time 

# Data store for new points
DATA = []


if __name__ == '__main__':
  # Register for pinging service
  delay = 2
  #ip_address = socket.gethostbyname(socket.gethostname())
  #print "attempting to register %s:%d" % (ip_address, PORT)
  #register_for_ping(ip_address, str(PORT))
  while(1):
    time.sleep(delay)
    r = requests.get('http://galvanize-case-study-on-fraud.herokuapp.com/data_point')
    dp = r.json()
    if dp in DATA:
        #print "duplicate discard!"
        pass
    else:
        if len(DATA) > 100:
          DATA = DATA[50:]
        DATA.append(dp)
        print dp['name']
        requests.post("http://0.0.0.0:8080/score", json=dp)
