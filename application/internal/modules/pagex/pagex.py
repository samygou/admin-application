import typing as t

from pydantic import BaseModel


class Pagex(BaseModel):
    offset: t.Optional[int] = 0
    size: t.Optional[int] = 10
