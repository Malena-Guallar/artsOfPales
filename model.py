from pydantic import BaseModel, Field
from typing import Optional, Union

class Artist(BaseModel):
    _id: Optional[Union[str, int, float]]
    firstname: str
    lastname: str
    field: str

