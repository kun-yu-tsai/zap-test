import time
from pprint import pprint
from zapv2 import ZAPv2

target = 'https://public-firing-range.appspot.com/'
apiKey = '8scvgn8em58k3avcad9cua1p41'
zap = ZAPv2(apikey=apiKey)

print('Spidering target {}'.format(target))

scanID = zap.spider.scan(target)

while int(zap.spider.status(scanID)) < 5:
    print('Spider progress %: {}'.format(zap.spider.status(scanID)))
    time.sleep(1)

print('Spider has completed!')
# Prints the URLs the spider has crawled
print('\n'.join(map(str, zap.spider.results(scanID))))


while int(zap.pscan.records_to_scan) > 0:
    # Loop until the passive scan has finished
    print('Records to passive scan : ' + zap.pscan.records_to_scan)
    time.sleep(2)

print('Passive Scan completed')

# Print Passive scan results/alerts
print('Hosts: {}'.format(', '.join(zap.core.hosts)))
print('Alerts: ')
pprint(zap.core.alerts())

with open('out.txt', 'w') as f:
    print('Hosts: {}'.format(', '.join(zap.core.hosts)), file=f)
    print('Alerts: ', file=f)
    pprint(zap.core.alerts(), f)