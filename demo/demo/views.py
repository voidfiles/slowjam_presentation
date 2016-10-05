from django.http import HttpResponse
import random
import requests
from slowjam.trace import span, annotate

def demo_view(request):
    delay = random.choice([.1, .2, .3, .4, .5, .6, .7, .8, .9, 1])
    error = random.choice([200, 200, 200, 200, 200, 200, 200, 200, 404, 500])

    with span('demo_view.request', extras={'delay': delay}):
        resp = requests.get('https://httpbin.org/delay/{}'.format(delay))

    annotate('demo_view.requests', extras={'total_time': delay * 3})

    return HttpResponse('This is a nice view <br><pre>{}</pre>'.format(resp.content),
                        status=error)


def lots_o_loops(request):
    b = 0
    for i in range(0, 10000):
        b += i

    return HttpResponse(b)
