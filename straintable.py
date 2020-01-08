#!/usr/bin/python3

# Create strain table from a downloaded summary XML
# The XML was downloaded from NCBI

import sys
from xml.dom.minidom import parse

xml = parse(sys.argv[1])
records = xml.getElementsByTagName('DocumentSummary')
outlist = dict()
for r in records:
	uid = r.getAttribute('uid')
	strain = r.getElementsByTagName('Sub_value')[0].childNodes[0].data
	submitter = r.getElementsByTagName('SubmitterOrganization')[0].childNodes[0].data
	status = r.getElementsByTagName('AssemblyStatus')[0].childNodes[0].data
	if submitter not in outlist:
		outlist[submitter] = list()
	outlist[submitter].append("%s\t%s\t%s" % (strain, submitter, status))

print("strain\tsubmitter\tassembly_status")
for submitter in outlist:
	for o in outlist[submitter]:
		print(o)
