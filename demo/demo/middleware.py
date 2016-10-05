from django_cprofile_middleware.middleware import ProfilerMiddleware

import line_profiler


class MyProfilerMiddleware(ProfilerMiddleware):
    def can(self, request):
        return 'prof' in request.GET


class MyLineProfilerMiddleware(object):

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.GET.get('line_profile') == '1':
            prof = line_profiler.LineProfiler()
            prof.add_function(view_func)
            prof.enable_by_count()
            request._line_profile_context = prof

    def process_response(self, request, response):
        prof = getattr(request, '_line_profile_context', None)
        if prof:
            prof.disable_by_count()
            prof.print_stats()

        return response
