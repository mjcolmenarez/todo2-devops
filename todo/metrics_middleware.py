import time

from django.utils.deprecation import MiddlewareMixin
from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "todo_http_requests_total",
    "Total HTTP requests",
    ["method", "path", "status"],
)

REQUEST_LATENCY = Histogram(
    "todo_http_request_latency_seconds",
    "HTTP request latency in seconds",
    ["path"],
)

ERRORS_TOTAL = Counter(
    "todo_http_errors_total",
    "Total HTTP 5xx responses",
    ["path"],
)


class MetricsMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        # mark the start time
        request._metrics_start_time = time.time()

    def process_response(self, request, response):
        path = getattr(request, "path", "unknown")
        method = getattr(request, "method", "GET")
        status = getattr(response, "status_code", 500)

        start = getattr(request, "_metrics_start_time", None)
        if start is not None:
            duration = time.time() - start
            REQUEST_LATENCY.labels(path=path).observe(duration)

        REQUEST_COUNT.labels(method=method, path=path, status=status).inc()

        if status >= 500:
            ERRORS_TOTAL.labels(path=path).inc()

        return response
