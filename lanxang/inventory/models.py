from pydantic import BaseModel


class Inventory(BaseModel):
    created: str
    hostname: str
    data: dict
