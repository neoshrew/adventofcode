FNAME = "input.txt"
# FNAME = "test1.txt"

def get_games():
    games = {}
    with open(FNAME) as fandle:
        for line in fandle:
            line = line.strip()
            if not line:
                break

            # Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            game_id_raw, game_raw = line.split(": ")
            game_id = int(game_id_raw.split()[1])
            this_game = games[game_id] = []

            for draw_raw in game_raw.split("; "):
                this_game.append(this_draw := {})
                for colour_raw in draw_raw.split(", "):
                    colour_count, colour = colour_raw.split(" ", 1)
                    this_draw[colour] = int(colour_count)

    return games

def game_min_counts(game):
    counts = {}
    for draw in game:
        for colour, count in draw.items():
            if (colour not in counts) or (count > counts[colour]):
                counts[colour] = count
    return counts

def solve():
    total = 0
    games = get_games()
    for game_id, game in games.items():
        game_mins = game_min_counts(game)

        total += game_mins["red"] * game_mins["blue"] * game_mins["green"]

    print(total)

if __name__ == "__main__":
    solve()