import http_trigger
from http_trigger.imports.http_types import Request, Response, Method
from http_trigger import exports
import numpy
import json

class InboundHttp(exports.InboundHttp):
    def handle_request(self, req: Request) -> Response:
        try:
            if req.method == Method.POST and req.uri == "/multiply" and req.body is not None:
                [a, b] = json.loads(req.body)
                return Response(
                    200,
                    [("content-type", "application/json")],
                    bytes(json.dumps(numpy.matmul(a, b).tolist()), "utf-8")
                )
            else:
                return Response(400, None, None)
        except Exception as e:
            return Response(
                500,
                [("content-type", "text/plain")],
                bytes(f"{type(e).__name__}: {str(e)}", "utf-8")
            )
