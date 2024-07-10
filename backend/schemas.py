from pydantic import BaseModel
from typing import Optional

class Shipment_detailsBase(BaseModel):
    origin: str
    destination: str
    size: Optional[str]=None
    type: Optional[str]=None
    commodity: Optional[str]=None
    class Config:
        orm_mode = True



class Shipment_detailsCreate(Shipment_detailsBase):
    pass
    class Config:
        orm_mode = True


class Shipment(Shipment_detailsBase):
    id: int

class Shipment_detailsUpdate(Shipment_detailsBase):
    pass


    class Config:
        orm_mode = True

