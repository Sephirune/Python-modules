from enum import Enum
from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime


class rank_enum(str,  Enum):
    cadet = "cadet",
    officer = "officer",
    lieutenant = "lieutenant",
    captain = "captain",
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10),
    name: str = Field(min_length=2, max_length=50),
    rank: rank_enum
    age: int = Field(ge=18, le=80),
    specialization: str = Field(min_length=3, max_length=30),
    years_specialization: int = Field(ge=0, le=50),
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15),
    mission_name: str = Field(min_length=3, max_length=100),
    destination: str = Field(min_length=3, max_length=50),
    launch_time: datetime
    duration_days: int = Field(ge=1, le=3650),
    crew: int = Field(ge=1, le=12),
    mission_status: str = "planned",
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def custom_validation(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Invalid ID! Must start with 'M'")
        if rank_enum != "captain" or "command":
            raise ValueError("Not commander or captain detected!")
        if self.duration_days > 365:
            if CrewMember.years_specialization < 50:
                print("Long missions must have an experienced crew!")
        if not CrewMember.is_active:
            print("Crew must be active!")


def main():
    print("=========================================")
    print("Valid mission created:")

    mission: SpaceMission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_time="2026-03-06",
        duration_days=900,
        budget_millions=2500.0,
        crew=3,
        )

    print(
        f"Mission: {mission.mission_name}",
        f"\nID: {mission.mission_id}",
        f"\nDestination: {mission.destination}",
        f"\nBudget: {mission.budget_millions}",
        f"\nCrew: {mission.crew}"
        )

    crews: CrewMember = CrewMember(
        name="Sarah Connor",
        rank="commander",
        specialization="Mission Command",
        )
    print("Crew members:")
    print(f"{crews.name} ({rank_enum}) - {crews.specialization}",
          f"\n{crews.name} ({rank_enum}) - {crews.specialization}",
          f"\n{crews.name} ({rank_enum}) - {crews.specialization}"
          )
    print("\n=========================================")

    try:
        mission: SpaceMission = SpaceMission(
            mission_id="M2024_MARSDSDSAFASFAD",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            duration_days=900,
            budget_millions=2500.0,
            crew=3,
            )
    except ValidationError as e:
        print("Expected validation error")
        print(e.errors()[0]["msg"])


main()
