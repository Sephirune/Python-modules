from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class Validate(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    station = Validate(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        is_operational=True,
        last_maintenance="2026-03-05T12:00:00"
        )

    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size}")
    print(f"Power: {station.power_level}")
    print(f"Oxygen: {station.oxygen_level}")
    if station.is_operational:
        print("Status: Operational")
    else:
        print("Status: Offline")

    print("\n========================================")
    try:
        Validate(
            station_id="BAD",
            name="Bad International Space Station",
            crew_size=100,
            power_level=815.6,
            oxygen_level=9150.2,
            is_operational=False,
            last_maintenance="2026-03-05T12:00:00"
            )
    except ValidationError as e:
        print("Expected validation error")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
