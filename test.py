#!/usr/local/bin/python2

import os
import time
from subprocess import check_output

#sysctloutput = 'dev.cpu.1.temperature: 30.0C\ndev.cpu.1.coretemp.throttle_log: 0\ndev.cpu.1.coretemp.tjmax: 85.0C\ndev.cpu.1.coretemp.resolution: 1\ndev.cpu.1.coretemp.delta: 55\ndev.cpu.1.cx_method: C1/hlt\ndev.cpu.1.cx_usage_counters: 375099011\ndev.cpu.1.cx_usage: 100.00% last 11692us\ndev.cpu.1.cx_lowest: C1\ndev.cpu.1.cx_supported: C1/1/0\ndev.cpu.1.%parent: acpi0\ndev.cpu.1.%pnpinfo: _HID=none _UID=0\ndev.cpu.1.%location: handle=\PR_.CPU1\ndev.cpu.1.%driver: cpu\ndev.cpu.1.%desc: ACPI CPU\ndev.cpu.0.temperature: 27.0C\ndev.cpu.0.coretemp.throttle_log: 0\ndev.cpu.0.coretemp.tjmax: 85.0C\ndev.cpu.0.coretemp.resolution: 1\ndev.cpu.0.coretemp.delta: 58\ndev.cpu.0.cx_method: C1'
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

