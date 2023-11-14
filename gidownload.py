#!/usr/bin/python3

"""
This script downloads the prediction results
from IslandView4 webserver
"""

import requests, sys
from requests_toolbelt.multipart.encoder import MultipartEncoder
import glob
import time
import sys

server = "http://www.pathogenomics.sfu.ca/islandviewer"
ext = "/rest/job/"

tokenfile = open(sys.argv[1])
tokens = list()
for t in tokenfile:
	line = t.rstrip().split()[5][:-1].replace("'", "")
	tokens.append(line)
tokenfile.close()

headers={'x-authtoken': 'dbe367ad-1792-fee2-feaa-d95a54426a6c'}

for t in tokens:
	r = requests.get(server + ext + t, headers = headers)
	if not r.ok:
		r.raise_for_status()
	decoded = r.json()
	print(repr(decoded))
	time.sleep(10)
