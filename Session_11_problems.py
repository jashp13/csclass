from typing import List, Tuple

# 1
last_names: List[str] = [
    "Smith", "Johnson", "Williams", "Jones", "Brown",
    "Davis", "Miller", "Wilson", "Taylor", "Anderson"
]

def display_names(names: List[str]) -> None:
    for name in names:
        print(name)

def display_names_reverse(names: List[str]) -> None:
    for name in reversed(names):
        print(name)


# 2
scores: List[int] = [88, 73, 95, 67, 82, 91, 78, 85, 90, 69]

def display_names_and_scores(names: List[str], scores: List[int]) -> None:
    for name, score in zip(names, scores):
        print(f"{name:10s} : {score}")

def display_names_and_scores_reverse(names: List[str], scores: List[int]) -> None:
    for name, score in zip(reversed(names), reversed(scores)):
        print(f"{name:10s} : {score}")


# 3
def load_from_file(fname: str) -> Tuple[List[str], List[int]]:
    names, vals = [], []
    with open(fname) as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 2: continue
            names.append(parts[0])
            vals.append(int(parts[1]))
    return names, vals

def find_high_low(names: List[str], vals: List[int]) -> None:
    high_val = 0
    high_idx = -1
    low_val = 999
    low_idx = -1
    for i, v in enumerate(vals):
        if v > high_val:
            high_val, high_idx = v, i
        if v < low_val:
            low_val, low_idx = v, i
    print("Highest :", names[high_idx], high_val)
    print("Lowest  :", names[low_idx], low_val)


# 4 & 5
def load_players(fname: str) -> Tuple[List[str], List[float]]:
    names, avgs = [], []
    with open(fname) as f:
        for line in f:
            nm, avg = line.strip().split()
            names.append(nm)
            avgs.append(float(avg))
    return names, avgs

def search_and_report(names: List[str], avgs: List[float]) -> None:
    while True:
        query = input("\nEnter last name (or blank to quit): ").strip()
        if not query:
            break
        try:
            idx = names.index(query)
            print(f"{names[idx]} -> {avgs[idx]:.3f}")
        except ValueError:
            print("Name not found.")


if __name__ == "__main__":
    print("── Task 1: display names ──")
    display_names(last_names)
    print("\n── Task 1: display names in reverse ──")
    display_names_reverse(last_names)

    print("\n── Task 2: names with scores ──")
    display_names_and_scores(last_names, scores)
    print("\n── Task 2: names with scores in reverse ──")
    display_names_and_scores_reverse(last_names, scores)

    print("\n── Task 3: load scores.txt & find high/low ──")
    fnames, fvals = load_from_file("scores.txt")
    display_names_and_scores(fnames, fvals)
    find_high_low(fnames, fvals)

    print("\n── Task 4 & 5: load players.txt & interactive search ──")
    pnames, pavg = load_players("players.txt")
    display_names_and_scores(pnames, [int(a*1000) for a in pavg])
    search_and_report(pnames, pavg)
