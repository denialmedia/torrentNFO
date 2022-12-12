#!/usr/bin/env python
import sys
from qbittorrent import Client
import keys

qb = Client('http://192.168.0.125:8085/')
# Grabs keys from keys.py
name = keys.login_name
password = keys.login_password

qb.login(name, password)
# defaults to admin:admin.
# to use defaults, just do qb.login()

fullData = []

# build data object
data = {
    "name":"",
    "size":"",
    "downloaded":int,
    "download_speed":int,
    "upload_speed":int,
}



# filter torrent to get just currently downloading torrents
torrents = qb.torrents(filter='downloading')

# build data entry for each torrent being downloaded. Add entry to fullData array.
for torrent in torrents:
    data = {}
    data['name'] = torrent['name']
    data['size'] = torrent['size']
    data['downloaded'] = torrent['completed']
    data['download_speed'] = torrent['dlspeed']
    data['upload_speed'] = torrent['upspeed']
    fullData.append(data)

speed = 0
upspeed = 0

for i in fullData:
    speed += i['download_speed']
    upspeed += i['upload_speed']
# divide by 1000000 to convert from kbps to mbps convert to string and truncate. Then print.
print("[D: "+str(speed/1000000)[:3]+" MiB/s | U:"+str(upspeed/1000000)[:3]+" MiB/s]")