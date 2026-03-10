from enum import Enum
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
    signal_strength: float = Field(le=10.0, ge=0.0)
    duration_minutes: int = Field(le=1440, ge=1)
    witness__count: int = Field(le=100, ge=1)
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


def main():
    print(
        'Alien Contact Log Validation',
        '\n======================================',
        '\nValid contact report:'
    )
    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2026-03-06",
        location="Area 51, Nevada",
        contact_type="radio",
        signal_strength=8.5,
        duration_minutes=45,
        witness__count=5,
        message_received="'Greetings from Zeta Reticuli"
    )
    print(f"ID: {contact.contact_id}",
          f"\nType: {contact.contact_type}",
          f"\nLocation: {contact.location}",
          f"\nSignal: {contact.signal_strength}/10",
          f"\nDuration: {contact.duration_minutes}",
          f"\nWitnesses: {contact.witness__count}",
          f"\nMessage: {contact.message_received}"
          )
    print("\n======================================")
    try:
        contact = AlienContact(
            contact_id="AC_2024_0014523141",
            timestamp="2026-03-06",
            location="Area 51, Nevada",
            contact_type="radio",
            signal_strength=8.5,
            duration_minutes=45,
            witness__count=5,
            message_received="'Greetings from Zeta Reticuli"
            )
    except ValidationError as e:
        print("Expected validation error")
        print(e.errors()[0]["msg"])


main()
