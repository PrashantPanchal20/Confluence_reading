
import sys
sys.path.append( '/home/..../lib/python2.7/site-packages' )

import pandas as pd
import atlassian
from atlassian import Confluence
import json
import requests
from requests.auth import HTTPBasicAuth
import json

url_page = 'https://'
# url = url_page
headers = {"Accept": "application/json"}

space = '.....'
title = 'VSIM Options Master Table'
username = "....."
api_token = '.....'    #will create by profile > setting > apii_tokken > create new > copy > paste here
page_id = "...."       #Profile > page information > copy it from url

confluence = Confluence(url=url_page, token=api_token)
text = "API Testing"
page = confluence.get_page_by_title(space, title, start=None, limit=None, expand="body.storage")
body = page["body"]["storage"]["value"]

tables = pd.read_html(body)
print(tables)
# for i, table in enumerate(tables, start=1):
#     file_name = f'table_{i}.csv'
#     table.to_csv(file_name)

print("=========================================================")
defines = tables['Option'].to_string(index=False)
print(defines)
