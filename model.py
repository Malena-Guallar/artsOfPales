from pydantic import BaseModel, Field
from typing import List, Optional, Union
from datetime import datetime

class Artist(BaseModel):
    _id: Optional[Union[str, int, float]]
    firstname: str
    lastname: str
    field: str

