from django.http import HttpResponse
import random
import requests
from slowjam.trace import span

DELAYS = [.1, .2, .3, .4, .5, .6, .7, .8, .9, 1]
RESPONSES = [200, 200, 200, 200, 200, 200, 200, 200, 404, 500]


def demo_view(request):
    delay = random.choice(DELAYS)
    status = random.choice(RESPONSES)

    with span('demo_view.request', extras={'delay': delay}):
        resp = requests.get('https://httpbin.org/delay/{}'.format(delay))

    return HttpResponse('This is a nice view <br><pre>{}</pre>'.format(resp.content),
                        status=status)
