'''
JavaScript Object Notation
'''

import json

with open('sxsw_bitrate_master.json') as f:
    data = json.load(f)

for quality in data['qualities']:
    #print('bitrate: ', quality['bitrate'], "   ", 'num_viewports: ', quality['num_viewports'])

    del quality['smoothstep']

with open('new_sxsw_bitrate_master.json', 'w') as f:
    json.dump(data, f, indent=2)