from enum import Enum, IntEnum
from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime
from typing import Optional


class ContactType(str, Enum):
    radio = "radio",
    visual = "visual",
    physical = "physical",
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(le=0.0, ge=10.0)
    duration_minutes: int = Field(le=1, ge=1440)
    witness__count: int = Field(le=1, ge=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def customvalidation(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Invalid contact. Contacts must start with AC")
        if self.contact_type == ContactType.physical:
            raise ValueError("Physical contacts must be verified!")
        if self.contact_type == ContactType.telepathic:
            if self.witness__count < 3:
                raise ValueError("Telepathic contact requires at least 3 \
witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals should be reported!")
        return self
