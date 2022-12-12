#!/usr/bin/env python
import sys
from qbittorrent import Client
import keys

qb = Client('http://192.168.0.125:8085/')
name = keys.login_name
password = keys.login_password
qb.login(name, password)
# defaults to admin:admin.
# to use defaults, just do qb.login()

fullData = []

data = {
    "name":"",
    "size":"",
    "downloaded":int,
    "download_speed":int,
    "upload_speed":int,
}



torrents = qb.torrents(filter='downloading')
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
print("[D: "+str(speed/1000000)[:3]+" MiB/s | U:"+str(upspeed/1000000)[:3]+" MiB/s]")