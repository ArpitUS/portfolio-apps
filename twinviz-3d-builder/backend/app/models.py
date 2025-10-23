from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class ProjectCreate(BaseModel):
    name: str

class ProjectOut(BaseModel):
    id: int
    name: str
    filename: str
    content_type: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
