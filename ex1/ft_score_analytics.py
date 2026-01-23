import sys
print("=== Player Score Analytics ===")
args = sys.argv[1:]
if len(args) == 0:
    print("=== Player Score Analytics ===")
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")

scores = []
try:
    for arg in args:
        scores.append(int(arg))
except:
    print("Error: Argument must be a number")

total_players = len(scores)
total_scores = sum(scores)
average_scores = total_scores / total_players
high_score = max(scores)
low_score = min(scores)
Score_range = high_score - low_score

print("=== Player Score Analytics ===")
print(f"Total players: {total_players}")
print(f"Total score: {total_scores}")
print(f"Average score: {average_scores}")
print(f"High score: {high_score}")
print(f"Low score: {low_score}")
print(f"Score range: {Score_range}")