from datetime import datetime
from pydantic import BaseModel, ConfigDict

class CampaignBase(BaseModel):
    name: str
    description: str | None = None


class CampaignCreate(CampaignBase):
    pass


class CampaignUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


class CampaignResponse(CampaignBase):
    id: int
    owner_id: int
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


class CampaignMemberCreate(BaseModel):
    user_id: int
    role: str = "MEMBER"


class CampaignMemberResponse(BaseModel):
    campaign_id: int
    user_id: int
    role: str
    joined_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )