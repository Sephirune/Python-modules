from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        for i in data:
            if not isinstance(i, (int, float)):
                return False
        return True

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid Data")
            count = len(data)
            total = sum(data)
            average = total / count
            result: str = f"Processed {count} numeric values, sum={total}, \
avg={average}"
            return super().format_output(result)
        except Exception as e:
            return f"Error processing data: {e}"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid Data")
            count = len(data)
            words = data.split()
            lenwords = len(words)
            result: str = f"Processed {count} characters, {lenwords} words"
            return super().format_output(result)
        except Exception as e:
            return f"Error processing data: {e}"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid Data")
            if "ERROR" in data:
                type = "ERROR"
                warning = "[ALERT]"
            elif "INFO" in data:
                type = "INFO"
                warning = "[INFO]"
            else:
                type = "UNKNOWN"
                warning = "[LOG]"
            result: str = f"{warning} {type} level detected: \
{data.split(': ')[1]}"
            return super().format_output(result)
        except Exception as e:
            return f"Error processing data: {e}"


""" if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    numeric = NumericProcessor()
    data1 = [1, 2, 3, 4, 5]
    print(f"Processing data: {data1}")
    print(f"Validation: {'Numeric data verified' if numeric.validate(data1) else 'Invalid'}")
    print(numeric.process(data1))

    print("\nInitializing Text Processor...")
    text = TextProcessor()
    data2 = "Hello Nexus World"
    print(f'Processing data: "{data2}"')
    print(f"Validation: {'Text data verified' if text.validate(data2) else 'Invalid'}")
    print(text.process(data2))

    print("\nInitializing Log Processor...")
    log = LogProcessor()
    data3 = "ERROR: Connection timeout"
    print(f'Processing data: "{data3}"')
    print(f"Validation: {'Log entry verified' if log.validate(data3) else 'Invalid'}")
    print(log.process(data3))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processors = [numeric, text, log]
    test_data = [[1, 2, 3], "Hello World!", "INFO: System ready"]
    #enumerate() convierte una tupla en un objeto enumerable
    for i, processor in enumerate(processors):
        result = processor.process(test_data[i])
        print(f"Result {i+1}: {result}")

    print("\nFoundation systems online. Nexus ready for advanced streams.") """
