from django.http import HttpResponse


def lots_o_loops(request):
    b = 0
    for i in range(0, 10000):
        b += i

    return HttpResponse(b)
