import pydantic
import starlite

from app import services, utils


class Message(pydantic.BaseModel):
    recipient: str
    content: str


class MessageController(starlite.Controller):
    path = "/messages"
    dependencies = {
        "message_service": starlite.Provide(services.MessageService.create),
        "termux": starlite.Provide(
            lambda: utils.Termux.create(services.TERMUX_SMS_API)
        ),
    }

    @starlite.get()
    async def index(self) -> dict[str, str]:
        return {"status": "ok"}

    @starlite.post()
    async def store(
        self,
        data: Message,
        message_service: services.MessageService,
        termux: utils.Termux,
    ) -> Message:
        message_svcs = message_service.create(termux, services.TERMUX_SMS_API)
        await message_svcs.send(data.recipient, data.content)

        return data


router = starlite.Router(path="", route_handlers=[MessageController])
