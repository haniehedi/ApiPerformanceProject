# listings/middleware.py
import time
import logging

# Set up logging
logger = logging.getLogger(__name__)

class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()  # Start timing

        # Process the request
        response = self.get_response(request)

        # Calculate duration
        duration = time.time() - start_time
        logger.info(f"{request.method} {request.path} took {duration:.2f} seconds")  # Log time taken

        return response

