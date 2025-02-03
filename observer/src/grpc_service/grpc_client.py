import grpc

from generated.observe_pb2_grpc import TelegramBotStub
from schemas.grpc_schemas import SendMessageRequest, Empty


class TelegrambotClient:
    def __init__(self, address="localhost:5001"):
        self.address = address
        self.channel = None
        self._stub = None

    async def connect(self):
        self.channel = grpc.aio.insecure_channel(self.address)
        self._stub = TelegramBotStub(self.channel)

    async def close(self):
        if self.channel:
            self.channel.close()

    async def send_message(self, request: SendMessageRequest) -> Empty:
        self._stub.SendMessage(request)


telegram_bot_client = TelegrambotClient()
