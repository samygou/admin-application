import logging
import typing as t
from concurrent import futures

import grpc

from application.api.v1.app import admin_pb2_grpc
from application.internal.service import service


class GRPCServer:
    """gRPC server"""

    def __init__(
            self,
            port: int,
            api_svc: service.AdminService,
            options: t.List[t.Tuple] = None
    ):
        self._port = port
        self._options = options if options else [('grpc.max_receive_message_length', 30 * 1024 * 1024)]
        self.api_svc = api_svc
        self.server = None

    def serve(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=self._options)
        admin_pb2_grpc.add_AdminServicer_to_server(self.api_svc, server)

        server.add_insecure_port(f'0.0.0.0:{self._port}')
        server.start()

        self.server = server
        logging.info('run grpc server success')


def new_grpc_server(port: int, api_svc: service.AdminService, options: t.List[t.Tuple] = None) -> GRPCServer:
    # 运行服务, 并把服务句柄保存到类属性
    grpc_server = GRPCServer(port, api_svc, options)
    grpc_server.serve()

    return grpc_server
