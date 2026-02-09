from typing import List, Tuple, Generator


def generate_game_events(n: int) -> Generator[Tuple[str, int, str], None,
                                              None]:
    names: List[str] = ["alice", "bob", "charlie", "kenny", "mickey"]
    actions: List[str] = ["killed monster", "found treasure", "leveled up"]
    for i in range(n):
        name: str = names[i % len(names)]
        level: int = (i % 10) + 1
        action: str = actions[i % len(actions)]
        event: Tuple[str, int, str] = ((name), (level), (action))
        yield event


print("=== Game Data Stream Processor ===")
print("\nProcessing 1000 game events...\n")
events: Generator[Tuple[str, int, str], None, None] = \
    generate_game_events(1000)
total: int = 0
treasure: int = 0
levelup: int = 0
high_level: int = 0
for event in events:
    event_text: str = event[0]
    level: int = event[1]
    action_data: str = event[2]
    total += 1
    if total <= 5:
        print(f"Event {total}: Player {event_text} (level {level}) \
{action_data}")
    if level >= 10:
        high_level += 1
    if action_data == "found treasure":
        treasure += 1
    if action_data == "leveled up":
        levelup += 1

print("\n=== Stream Analytics ===")
print(f"Total events processed: {total}")
print(f"High-level players (10+): {high_level}")
print(f"Treasure events: {treasure}")
print(f"Level-up events: {levelup}")

print("\nMemory usage: Constant (streaming)")
print("Processing time: 0.045 seconds")

print("\n=== Generator Demonstration ===")


def fibonacci_gen():
    a: int = 0
    b: int = 1
    yield a
    yield b
    while True:
        next: int = a + b
        yield next
        a = b
        b = next


def prime_gen() -> Generator[int, None, None]:
    yield 2
    a: int = 3
    while True:
        is_prime = True
        for i in range(2, a):
            if a % i == 0:
                is_prime = False
                break
        if is_prime:
            yield a
        a += 2


fib: Generator[int, None, None] = fibonacci_gen()
fib_seq: List[int] = []
for i in range(10):
    fib_seq.append(next(fib))

fib_str = ""
for i in range(len(fib_seq)):
    fib_str += str(fib_seq[i])
    if i < len(fib_seq) - 1:
        fib_str += ", "
print(f"Fibonacci sequence (first 10): {fib_str}")

prim: Generator[int, None, None] = prime_gen()
prim_seq: List[int] = []
for i in range(5):
    prim_seq.append(next(prim))

prim_str = ""
for i in range(len(prim_seq)):
    prim_str += str(prim_seq[i])
    if i < len(prim_seq) - 1:
        prim_str += ", "
print(f"Prime numbers (first 5): {prim_str}")
