from starlette.middleware.base import BaseHTTPMiddleware

class SampleMiddleware(BaseHTTPMiddleware):
    # def __init__(self, app, header_value='Example'):
    #     super().__init__(app)
    #     self.header_value = header_value

    async def dispatch(self, request, call_next):
        print('--- before ---')
        response = await call_next(request)
        # response.headers['Custom'] = 'Example'
        print('--- after ---')
        return response
