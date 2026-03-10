from enum import Enum
from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime


class RankEnum(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: RankEnum
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def custom_validation(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Invalid ID! Must start with 'M'")
        ranks: list[RankEnum] = [m.rank for m in self.crew]
        if RankEnum.captain not in ranks and RankEnum.commander not in ranks:
            raise ValueError("Mission must have a captain or commander!")
        if self.duration_days > 365:
            for member in self.crew:
                if member.years_experience < 5:
                    raise ValueError(
                        f"{member.name} lacks experience for a long mission "
                        f"(needs 5+ years, has {member.years_experience})"
                    )
        for member in self.crew:
            if not member.is_active:
                raise ValueError(f"Crew member {member.name} is not active!")
        return self


def main() -> None:
    print("=========================================")
    print("Valid mission created:")

    commander: CrewMember = CrewMember(
        member_id="CM001",
        name="Sarah Connor",
        rank=RankEnum.commander,
        age=40,
        specialization="Mission Command",
        years_experience=15,
        is_active=True
    )

    mission: SpaceMission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2026-03-06",
        duration_days=900,
        budget_millions=2500.0,
        crew=[commander]
    )

    print(
        f"Mission: {mission.mission_name}",
        f"\nID: {mission.mission_id}",
        f"\nDestination: {mission.destination}",
        f"\nBudget: {mission.budget_millions}",
        f"\nCrew count: {len(mission.crew)}"
    )

    print("Crew members:")
    for member in mission.crew:
        print(f"{member.name} ({member.rank.value}) - {member.specialization}")

    print("\n=========================================")

    try:
        SpaceMission(
            mission_id="M2024_MARSDSDSAFASFAD",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2026-03-06",
            duration_days=900,
            budget_millions=2500.0,
            crew=[commander]
        )
    except ValidationError as e:
        print("Expected validation error")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
