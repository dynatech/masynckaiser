# -*- coding: utf-8 -*-
"""
Created on Mon Oct 03 17:44:15 2016

@author: PradoArturo
"""

from datetime import datetime
import threading
import os
import sys
import time
import json
import pandas as pd

#include the path of "libraries" folder for the python scripts searching
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../libraries'))
if not path in sys.path:
    sys.path.insert(1,path)
del path   

import masynckaiserWSSLib as masync
import basicDB as bdb

def main():
    host = "192.168.150.75"
    port = 5055
    schema = "senslopedb"
    batchRows = 5000
    
    while True:
      print('Start Time: %s' % time.ctime())
      masync.syncStartUp(host, port, batchRows)

      # Sleep for 10 min
      time.sleep(600)

try:
  main()
except KeyboardInterrupt:
  print('\n\nKeyboard exception received. Exiting.')
  exit()