'''
Testing script measuring time (an estimate) for processing and serialization of DB content for a server
The time spent is measured using cURL through pycURL inspired by
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


endpoints = {
    'flask_mongoengine_embedding': 'http://localhost:1000/paginate/1',
    'flask_mongoengine_reference': 'http://localhost:1001/paginate/1',
    'flask_postgresql': 'http://localhost:1002/paginate/1',
    'flask_sqlite': 'http://localhost:1003/paginate/1',
    'django_postgresql': 'http://localhost:1004/authors/',
    'django_sqlite': 'http://localhost:1005/authors/',
    'flask_peewee_postgresql': 'http://localhost:1006/paginate/1'
}


# Measure server request process time for given endpoints
N = 3
for kv in endpoints.items():
    service, endpoint = kv

    time, std = get_mean_time(endpoint, N)

    print(f'Service: {service}, time {time}, std {std} (average of {N})')
