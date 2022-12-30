# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import pb_kit_sms_pb2 as pb__kit__sms__pb2


class APIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendSM = channel.unary_unary(
                '/pb_kit_sm.API/SendSM',
                request_serializer=pb__kit__sms__pb2.SendSMReq.SerializeToString,
                response_deserializer=pb__kit__sms__pb2.SendSMResp.FromString,
                )
        self.CheckCode = channel.unary_unary(
                '/pb_kit_sm.API/CheckCode',
                request_serializer=pb__kit__sms__pb2.CheckCodeReq.SerializeToString,
                response_deserializer=pb__kit__sms__pb2.CheckCodeResp.FromString,
                )
        self.SendTemplateSM = channel.unary_unary(
                '/pb_kit_sm.API/SendTemplateSM',
                request_serializer=pb__kit__sms__pb2.SendTemplateSMReq.SerializeToString,
                response_deserializer=pb__kit__sms__pb2.SendTemplateSMResp.FromString,
                )


class APIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendSM(self, request, context):
        """发送验证码短信
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckCode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendTemplateSM(self, request, context):
        """发送模板短信
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_APIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendSM': grpc.unary_unary_rpc_method_handler(
                    servicer.SendSM,
                    request_deserializer=pb__kit__sms__pb2.SendSMReq.FromString,
                    response_serializer=pb__kit__sms__pb2.SendSMResp.SerializeToString,
            ),
            'CheckCode': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckCode,
                    request_deserializer=pb__kit__sms__pb2.CheckCodeReq.FromString,
                    response_serializer=pb__kit__sms__pb2.CheckCodeResp.SerializeToString,
            ),
            'SendTemplateSM': grpc.unary_unary_rpc_method_handler(
                    servicer.SendTemplateSM,
                    request_deserializer=pb__kit__sms__pb2.SendTemplateSMReq.FromString,
                    response_serializer=pb__kit__sms__pb2.SendTemplateSMResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb_kit_sm.API', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class API(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendSM(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb_kit_sm.API/SendSM',
            pb__kit__sms__pb2.SendSMReq.SerializeToString,
            pb__kit__sms__pb2.SendSMResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckCode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb_kit_sm.API/CheckCode',
            pb__kit__sms__pb2.CheckCodeReq.SerializeToString,
            pb__kit__sms__pb2.CheckCodeResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendTemplateSM(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb_kit_sm.API/SendTemplateSM',
            pb__kit__sms__pb2.SendTemplateSMReq.SerializeToString,
            pb__kit__sms__pb2.SendTemplateSMResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
