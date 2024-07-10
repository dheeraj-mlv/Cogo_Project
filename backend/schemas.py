from pydantic import BaseModel
from typing import Optional

class Shipment_detailsBase(BaseModel):
    origin: str
    destination: str
<<<<<<< HEAD
    size: Optional[str]=None
    type: Optional[str]=None
    commodity: Optional[str]=None
    class Config:
        orm_mode = True


=======
    size: str
    type: str
    commodity: str
    count : int
    weight : str
>>>>>>> f7189929ae0b55d699a481d0f10008aef53014ea

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

