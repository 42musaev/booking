from pydantic import BaseModel as base_model


class BaseModel(base_model):
    class Config:
        orm_mode = True
