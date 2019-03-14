'''
Testing script measuring time (an estimate) for processing and serialization of DB content for a server
Several metrics are measured using cURL through pycURL inspired by
- http://blog.cloudflare.com/a-question-of-timing/
- http://stackoverflow.com/questions/17638026/calculating-server-processing-time-with-curl
'''
import pycurl

from io import BytesIO
from statistics import mean, stdev

buffer = BytesIO()


def get_mean_time(url, n):
    '''
    Measures mean and standard deviation of request process time

    Args:
        url: endpoint for test
        n: number of requests
    Returns:
        Tuple of mean and std of request process time
    '''

    req_times = []

    for _ in range(1, n+1):
        # Setup cURL binding
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()

        # Measure server processing time
        req_time = c.getinfo(pycurl.STARTTRANSFER_TIME) - \
            c.getinfo(pycurl.PRETRANSFER_TIME)

        req_times.append(req_time)

        c.close()

    return (mean(req_times), stdev(req_times))


urls = [
    'http://localhost:1000/paginate/1',
    'http://localhost:1001/paginate/1',
    'http://localhost:1002/paginate/1',
    'http://localhost:1003/authors/',
    'http://localhost:1004/authors/'
]


# Measure server request process time for given endpoints
for url in urls:
    print(get_mean_time(url, 3))
