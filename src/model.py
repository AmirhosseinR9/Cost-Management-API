from pydantic import BaseModel, Field
from typing import Annotated


_OnlyLetters = Annotated[str, Field(pattern=r'^[A-Za-z\u0600-\u06FF\s]+$', max_length=500, min_length=1)]

class _CostBase(BaseModel):
    description: _OnlyLetters
    amount: int


class ResponsCost(_CostBase):
    id: int

class CreatCost(_CostBase):
    pass

class EditCost(_CostBase):
    pass