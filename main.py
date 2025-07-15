
import requests
# This script fetches the latest chess games from a user's archive on Chess.com
username = "chibob1000"


def fetch_latest_games(username):
    # 1) Get your archive URLs
    archives_url = f"https://api.chess.com/pub/player/{username}/games/archives"
    res = requests.get(archives_url)
    if res.status_code != 200:
        print("Error fetching archives:", res.status_code)
        return

    archives = res.json().get('archives', [])
    if not archives:
        print("No archives found for", username)
        return

    latest_url = archives[-1]  # the most recent month

    # 2) Fetch the games in that archive
    games_res = requests.get(latest_url)
    if games_res.status_code != 200:
        print("Error fetching games:", games_res.status_code)
        return

    games = games_res.json().get('games', [])
    print(f"Found {len(games)} games for '{username}' in the latest archive.")

    # 3) Print basic info for each game
    for game in games:
        white = game['white']['username']
        black = game['black']['username']
        result_white = game['white']['result']
        result_black = game['black']['result']
        pgn_preview = game['pgn'][:200].replace("\n", " ") + "..."

        print("\n=== Game ===")
        print(f"{white} vs {black}")
        print(f"Result: {result_white} – {result_black}")
        print("PGN Preview:", pgn_preview)


if __name__ == "__main__":
    fetch_latest_games(username)
