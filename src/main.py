"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


USERS = {
    "High-Energy Pop": {"genre": "pop",      "mood": "happy",   "energy": 0.9},
    "Chill Lofi":      {"genre": "lofi",     "mood": "chill",   "energy": 0.35},
    "Deep Intense Rock": {"genre": "rock",   "mood": "intense", "energy": 0.92},
}


def print_recommendations(label: str, recommendations: list) -> None:
    print("\n" + "=" * 44)
    print(f"  {label.upper()}")
    print("=" * 44)
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n  #{rank}  {song['title']} by {song['artist']}")
        print(f"       Score : {score:.2f} / 4.00")
        print(f"       Why   : {explanation}")
    print("\n" + "=" * 44)


def main() -> None:
    songs = load_songs("data/songs.csv")

    for label, user_prefs in USERS.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_recommendations(label, recommendations)


if __name__ == "__main__":
    main()
