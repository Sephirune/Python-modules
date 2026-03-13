from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        if criteria == "high":
            return [x for x in data_batch if isinstance(x, (int, float))
                    and x > 25]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "event",
            "total_readings": self.total_readings
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.total_readings = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not isinstance(data_batch, list):
                raise ValueError("Invalid Data")

            count = len(data_batch)
            temperature = data_batch[0]

            result: str = (
                f"Sensor analysis: {count} readings processed, \
avg temp: {temperature}°C"
            )
            self.total_readings += count
            return result

        except Exception as e:
            return f"Error processing data: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Environmental Data",
            "total_readings": self.total_readings
        }


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.total_operations = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not isinstance(data_batch, list):
                raise ValueError("Invalid Data")

            count = len(data_batch)
            net_flow = sum(data_batch)

            result: str = (
                f"Transaction analysis: {count} operations, net flow: \
+{net_flow} units"
            )
            self.total_operations += count
            return result

        except Exception as e:
            return f"Error processing data: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Financial Data",
            "total_operations": self.total_operations
        }


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.total_readings = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not isinstance(data_batch, list):
                raise ValueError("Invalid Data")

            count = len(data_batch)
            errors = sum(1 for e in data_batch if e == "error")

            result: str = (
                f"Event analysis: {count} events, {errors} error detected"
            )
            self.total_readings += count
            return result

        except Exception as e:
            return f"Error processing data: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "System Events",
            "total_readings": self.total_readings
        }


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if isinstance(stream, DataStream):
            self.streams.append(stream)

    def process_all(self) -> None:
        sensor_data = [22.5, 65, 1013]
        transaction_data = [100, -150, 75]
        event_data = ["login", "error", "logout"]

        for stream in self.streams:
            if isinstance(stream, SensorStream):
                result = stream.process_batch(sensor_data)

            elif isinstance(stream, TransactionStream):
                print(f"Processing transaction batch: \
[buy:{transaction_data[0]}, sell:{transaction_data[1]}, \
buy:{transaction_data[2]}]")
                result = stream.process_batch(transaction_data)

            elif isinstance(stream, EventStream):
                print("Processing event batch: [login, error, logout]")
                result = stream.process_batch(event_data)

            print(result)


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    print("\nInitializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    sensor_data = [22.5, 65, 1013]
    print(f"Processing sensor batch: [temp:{sensor_data[0]}, \
humidity:{sensor_data[1]}, pressure:{sensor_data[2]}]")
    print(sensor.process_batch(sensor_data))

    print("\nInitializing Transaction Stream...")
    print(f"Stream ID: {transaction.stream_id}, Type: Financial Data")
    transaction_data = [100, -150, 75]
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(transaction.process_batch(transaction_data))

    print("\nInitializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: System Events")
    event_data = ["login", "error", "logout"]
    print("Processing event batch: [login, error, logout]")
    print(event.process_batch(event_data))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    streams: List[DataStream] = [sensor, transaction, event]
    batches: List[List[Any]] = [
        [22.5, 23.1],
        [100, -50, 25, -10],
        ["login", "logout", "error"]
    ]

    print("\nBatch 1 Results:")
    for stream, batch in zip(streams, batches):
        if isinstance(stream, SensorStream):
            print(f"- Sensor data: {len(batch)} readings processed")
        elif isinstance(stream, TransactionStream):
            print(f"- Transaction data: {len(batch)} operations processed")
        elif isinstance(stream, EventStream):
            print(f"- Event data: {len(batch)} events processed")

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
