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
lightgroup=[]
for groupid in groups:
    lightgroup.append(tradfriStatus.tradfri_get_group(hubip, securityid,
                                                      str(groupid)))
def allOn(groups):
    for group in groups:
        tradfri_dim_group(hubip, securityid, group, 100)


def tradfri_dim_group(hubip, securityid, groupid, value):
    """ function for dimming tradfri lightbulb """
    tradfriHub = 'coaps://{}:5684/15004/{}'.format(hubip, groupid)
    dim = float(value) * 2.55
    payload = '{ "5851" : %s }' % int(dim)

    api = '{} -m put -u "Client_identity" -k "{}" -e \'{}\' "{}"'.format(coap, securityid,payload, tradfriHub)
    result = os.popen(api)
