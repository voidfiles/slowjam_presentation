from django.conf.urls import url

from .views import lots_o_loops
from .slowjam_views import demo_view

urlpatterns = [
    url(r'^loops', lots_o_loops),
    url(r'^demo', demo_view)
]
