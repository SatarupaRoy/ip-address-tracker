import pygeoip
gip = pygeoip.GeoIP("GeoLiteCity.dat")
res = gip.record_by_addr('161.185.160.93')
for key,val in res.items():
    print('%s : %s' % (key,val))