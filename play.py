from xbmcjson import XBMC, PLAYER_VIDEO

xbmc = XBMC("http://192.168.0.218:8080/jsonrpc")

print xbmc.JSONRPC.Ping()

# print xbmc.Player.Open('code/bbc-radio-alarm/today_22_05_2015_b05vfdzj.m4a')
print xbmc.Player.Open({'item': {'file': 'code/bbc-radio-alarm/today_22_05_2015_b05vfdzj.m4a'}})