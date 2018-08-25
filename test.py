#!/usr/local/bin/python2

import os
import time
from subprocess import check_output

# Get sysctl data
sysctloutput = check_output(["sysctl", "dev.cpu"])
hostname = os.uname()[1]

statval = [line.split(":") for line in sysctloutput.split('\n') if "dev.cpu" and "temperature:" in line or "dev.cpu" and "tjmax:" in line]

stat = [[stat[0].split("."), stat[1].strip()] for stat in statval]

for item in stat:
    sinceepochinns = str(format (time.time() * 1000000000, '.0f'))

    print 'sensors,host=' + hostname + \
          ',feature=' + '.'.join(item[0]) + \
          ',chip=sysctl' + \
          " temp_input=" + item[1].replace("C", "") + " " + sinceepochinns

