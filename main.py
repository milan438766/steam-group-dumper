import requests
from steam import steamid
import xml.etree.ElementTree as ET

group = str(input("enter steam group name: "))
url = 'https://steamcommunity.com/groups/group_id_to_replace/memberslistxml/?xml=1'
url = url.replace( 'group_id_to_replace', group)
site_data = requests.get(url)
root = ET.fromstring(site_data.text)
members = root[6]
for member in members:
    id = steamid.SteamID(id=int(member.text), type="Individual").as_32
    print( str(id) + ',', end=' ')