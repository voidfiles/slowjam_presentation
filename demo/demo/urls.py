from django.conf.urls import url

from .views import demo_view, lots_o_loops
urlpatterns = [
    url(r'^loops', lots_o_loops),
    url(r'^demo', demo_view)
]
