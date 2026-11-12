from pydantic import BaseModel, Field, ConfigDict


class IncidentCreate(BaseModel):
    title: str = Field(max_length=200)
    description: str = Field(max_length=500)
    severity: int = Field(ge=1, le=5)
    status: str = Field(default="OPEN", max_length=50)


class IncidentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id : int
    title: str
    description: str
    severity: int
    status: str