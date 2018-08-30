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
    
    masync.syncStartUp(host, port)
#    masync.syncRealTime(host, port)
#    masync.testSendRecv(host, port, schema, table)
#    masync.threadedSendRecv(host, port, schema, table)

main()