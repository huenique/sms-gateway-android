import pydantic
import starlite


class Message(pydantic.BaseModel):
    recipient: int
    content: str


class MessageController(starlite.Controller):
    path = "/messages"

    @starlite.get()
    async def index(self) -> dict[str, str]:
        return {"status": "ok"}

    @starlite.post()
    async def store(self, message: Message) -> Message:
        return message


router = starlite.Router(path="", route_handlers=[MessageController])
