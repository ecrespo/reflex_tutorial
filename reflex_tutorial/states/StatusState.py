import reflex as rx
import httpx



class WebObject(rx.Base):
    id: int
    type: str
    key: str
    value: str


class StateFather(rx.State):
    api_key: str
    project_url: str
    node: str
    method: str

    headers: list[WebObject]
    datas: list[WebObject]


class AddObject(StateFather):
    h_counter: int = 0
    d_counter: int = 0


    async def create_web_object(self, _type_: str):
        return WebObject(
            id=(
                self.h_counter if _type_ == "H" else self.d_counter
            ),
            type=_type_,
            key="",
            value=""
        )

    async def add(self, _type_: str):
        obj: WebObject = await self.create_web_object(_type_)

        self.headers.append(obj) if _type_ == "H" else self.datas.append(obj)

        self.h_counter += 1 if _type_ == "H" else self.d_counter



class Update(StateFather):

    async def type_header(self, _object, object):
        self.headers = [
            _object if header.id == object["id"] else header for header in self.headers
        ]



    async def type_data(self, _object, object):
        self.datas = [
            _object if header.id == object["id"] else header for header in self.datas
        ]


    async def update_list(self, _object, object):
        if object["type"] == "H":
            await self.type_header(_object, object)

        if object["type"] == "D":
            await self.type_data(_object, object)

    async def key(self, value, object: dict):
        _object: WebObject = WebObject(
            id=object["id"],
            type=object["type"],
            key=value,
            value=object["value"],
        )
        await self.update_list(_object, object)

    async def value(self, value, object: dict):
        _object: WebObject = WebObject(
            id=object["id"],
            type=object["type"],
            key=object["key"],
            value=value,
        )
        await self.update_list(_object, object)


class StatusState(StateFather):

    opacity: str = "0"
    status: str
    status_color: str

    async def get_status(self) -> str:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get("https://status.supabase.com")
                if response.status_code == 200:
                    self.status = "OK"
                    self.status_color = "grass"
                else:
                    self.status = "ERROR"
                    self.status_color = "orange"
                self.opacity = "1"
            except httpx.ConnectTimeout:
                self.status = "TIMEOUT"
                self.status_color = "red"
                self.opacity = "1"
            except Exception as e:
                self.status = "CONNECTION ERROR"
                self.status_color = "red"
                self.opacity = "1"



class ResetObject(StateFather):

    async def reset_list(self, _type_: str):
        self.headers = [] if _type_ == "H" else self.datas

