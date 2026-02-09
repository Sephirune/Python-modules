import sys
print("=== Player Score Analytics ===")
args = sys.argv[1:]
if len(args) == 0:
    print("=== Player Score Analytics ===")
    print("No scores provided. Usage: python3 ft_score_analytics.py \
<score1> <score2> ...")
    sys.exit()

scores: list = []
try:
    for arg in args:
        scores.append(int(arg))
except ValueError:
    print("Error: Argument must be a number")

total_players: int = len(scores)
total_scores: int = sum(scores)
average_scores: float = total_scores / total_players
high_score: int = max(scores)
low_score: int = min(scores)
Score_range: int = high_score - low_score

print(f"Total players: {total_players}")
print(f"Total score: {total_scores}")
print(f"Average score: {average_scores}")
print(f"High score: {high_score}")
print(f"Low score: {low_score}")
print(f"Score range: {Score_range}")
