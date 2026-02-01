from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria:
                    Optional[str] = None):
        if criteria is None:
            return data_batch
        if criteria == "high":
            return [x for x in data_batch if isinstance(x, (int, float)) and x
                    > 25]
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
            total = sum(data_batch)
            avg = total / count
            result: str = f"Sensor analysis: {count} readings processed, avg \
temp: {avg}"
            self.total_readings += count
            return result
        except Exception as e:
            return f"Error processing data: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "Stream_id": self.stream_id,
            "type": "Enviromental Data",
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
            total = sum(data_batch)
            result: str = f"Transaction analysis: {count} operations, \
net flow: +{total} units"
            self.total_operations += count
            return result
        except Exception as e:
            return f"Error processing data: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "Stream_id": self.stream_id,
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
            result: str = f"Event analysis: {count} events processed"
            self.total_readings += count
            return result
        except Exception as e:
            return f"Error processing data: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "Stream_id": self.stream_id,
            "type": "System Events",
            "total_readings": self.total_readings
        }


class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if isinstance(stream, DataStream):
            self.streams.append(stream)

    def process_all(self) -> None:
        sensor_data = [22.5, 65, 1013]
        transaction_data = [100, -50, 75]
        event_data = ["login", "error", "logout"]
        for stream in self.streams:
            if isinstance(stream, SensorStream):
                result = stream.process_batch(sensor_data)
            elif isinstance(stream, TransactionStream):
                result = stream.process_batch(transaction_data)
            elif isinstance(stream, EventStream):
                result = stream.process_batch(event_data)
            print(result)


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    processor = StreamProcessor()

    sensor = SensorStream("SENSOR_001")
    print("\nInitializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    print(f"Processing sensor batch: [temp:22.5, humidity:65, preassure:1013]")
    processor.add_stream(sensor)
    transaction = TransactionStream("TRANS_001")
    print("\nInitializing Transaction Stream...")
    print(f"Stream ID: {transaction.stream_id}, Type: Financial Data")
    processor.add_stream(transaction)
    event = EventStream("EVENT_001")
    print("\nInitializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: System Events")
    processor.add_stream(event)

    processor.process_all()