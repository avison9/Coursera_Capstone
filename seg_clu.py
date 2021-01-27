import pandas as pd
import numpy as np
import requests

url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
df = pd.read_html(url)
header = ['Postal Code','Borough','Neighbourhood']
dfs = df[0][header]
df = pd.DataFrame(dfs, columns=header)
for bor in df['Borough']:
	if bor == 'Not assigned':
		