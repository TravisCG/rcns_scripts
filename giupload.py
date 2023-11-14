#!/usr/bin/python3

"""
This script uploads the GBK formatted files
to IslandView4 webserver and find potential
genomic islands.
The script does not check if the job is done.
"""

import requests, sys
from requests_toolbelt.multipart.encoder import MultipartEncoder
import glob
import time

server = "http://www.pathogenomics.sfu.ca/islandviewer"
ext = "/rest/submit/"

filenames = glob.glob("../genomicisland/*.gbk")

for f in filenames:

  multipart_data = MultipartEncoder(
    fields={ "format_type": "GENBANK",
             'email_addr': 'buldozer88@hotmail.com',
             'ref_accnum': 'LN649235.1',
             'genome_file': ('filename', open(f, 'rb'), 'text/plain')}
  )

  headers={'Content-Type': multipart_data.content_type, 'x-authtoken': 'dbe367ad-1792-fee2-feaa-d95a54426a6c'}

  r = requests.post(server+ext, headers=headers, data=multipart_data)

  if not r.ok:
    r.raise_for_status()
  decoded = r.json()
  print(repr(decoded))
  time.sleep(10)
