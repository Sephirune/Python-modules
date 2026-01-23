def generate_game_events(n):
    names = ["alice", "bob", "charlie", "kenny", "mickey"]
    action = ["killed monster", "found treasure", "leveled up"]
    for i in range(n):
        names = names[i % len(names)]
        level = (i % 10) + 1
        action = action[i % len(action)]
        event = f"Player {names} (level {level}) {action}"
        yield event


print("=== Game Data Stream Processor ===")
print("\nProcessing 1000 game events...\n")
events = generate_game_events(1000)
total = 0
treasure = 0
levelup = 0
high_level = 0
for event in events:
    event_text = event[0]
    level = event[1]
    action_data = event[2]
    total += 1
    if total <= 5:
        print(f"Event {total}: {event}")
    if level >= 10:
        high_level += 1
    if action_data == "found treasure":
        treasure += 1
    if action_data == "leveled up":
        levelup += 1

print("\n=== Stream Analytics ===")
print(f"Total events processed: {total}")
print(f"High-level players (10+): {high_level}")


generate_game_events(10)
