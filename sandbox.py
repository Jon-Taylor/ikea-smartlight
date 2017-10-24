from __future__ import print_function
from __future__ import unicode_literals

import os
import sys
import time
import ConfigParser

from tradfri import tradfriStatus
from tqdm import tqdm

conf = ConfigParser.ConfigParser()
script_dir = os.path.dirname(os.path.realpath(__file__))
conf.read(script_dir + '/tradfri.cfg')

hubip = conf.get('tradfri', 'hubip')
securityid = conf.get('tradfri', 'securityid')

lightbulb = []
lightgroup = []

print('[ ] Tradfri: acquiring all Tradfri devices, please wait ...')
devices = tradfriStatus.tradfri_get_devices(hubip, securityid)
groups = tradfriStatus.tradfri_get_groups(hubip, securityid)

print(groups)

print(devices)

print(devices)

