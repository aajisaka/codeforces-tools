#!/usr/bin/env python3

import urllib.request
import json
import sys

args = sys.argv
if len(args) != 2:
  print('Usage: ./tool.py <comma-separated username>')
  sys.exit(1)

api = "https://codeforces.com/api/user.status?handle={username}"
submittedset = set()
names = sys.argv[1].split(',')

for name in names:
  url = api.format(username=name)
  print("Fetching: " + url)
  req = urllib.request.Request(url)
  r = urllib.request.urlopen(req)
  data = json.load(r)
  for result in data['result']:
    contestId = result['contestId']
    submittedset.add(contestId)

url = "https://codeforces.com/api/contest.list"
req = urllib.request.Request(url)
r = urllib.request.urlopen(req)
contests = json.load(r)
for contest in contests['result']:
  contestId = contest['id']
  if contestId not in submittedset and contest['phase'] == "FINISHED":
    print(str(contestId) + ": " + contest['name'])

