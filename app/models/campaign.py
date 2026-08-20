from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Campaign(Base):
    __tablename__ = "campaigns"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    owner = relationship(
        "User",
        back_populates="campaigns"
    )

    members = relationship(
        "CampaignMember",
        back_populates="campaign"
    )   

    tasks = relationship(
        "CampaignTask",
        back_populates="campaign"
    )

class CampaignMember(Base):
    __tablename__ = "campaign_members"
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    role = Column(String(20), nullable=False)
    joined_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    campaign = relationship(
        "Campaign",
        back_populates="members"
    )

    user = relationship(
        "User",
        back_populates="campaign_members"
    )