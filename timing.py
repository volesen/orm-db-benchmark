'''
Testing script measuring time for processing and serialization to client for a server
Several metrics are measured using cURL inspired by
- http://blog.cloudflare.com/a-question-of-timing/
- http://stackoverflow.com/questions/17638026/calculating-server-processing-time-with-curl
'''
import pycurl

from io import BytesIO
from statistics import mean, stdev

buffer = BytesIO()


URL = 'http://localhost:8000/paginate/2'


request_process_time = []

for i in range(1, 5):
    c = pycurl.Curl()
    c.setopt(c.URL, URL)
    c.setopt(c.WRITEDATA, buffer)

    c.perform()
    request_process_time.append( c.getinfo(pycurl.STARTTRANSFER_TIME) - c.getinfo(pycurl.PRETRANSFER_TIME) )
    print( c.getinfo(pycurl.STARTTRANSFER_TIME) - c.getinfo(pycurl.PRETRANSFER_TIME)  )
    c.close()


print(f'Mean: {mean(request_process_time)}')
print(f'Std: {stdev(request_process_time)}')