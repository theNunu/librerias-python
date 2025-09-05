from pydantic import BaseModel
from datetime import datetime
class Champion(BaseModel):
    name: str
    carril: str
    # created_at =  datetime.now()
