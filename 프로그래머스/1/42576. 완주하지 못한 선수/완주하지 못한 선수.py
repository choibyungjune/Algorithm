from collections import defaultdict

def solution(participant, completion):
    counts = defaultdict(int)
    for name in participant:
        counts[name] = counts[name] + 1

    for name in completion:
        counts[name] -= 1

    for name, cnt in counts.items():
        if cnt > 0:
            return name

