"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


USERS = {
    "High-Energy Pop": {"genre": "pop",      "mood": "happy",   "energy": 0.9},
    "Chill Lofi":      {"genre": "lofi",     "mood": "chill",   "energy": 0.35},
    "Deep Intense Rock": {"genre": "rock",   "mood": "intense", "energy": 0.92},
}

EDGE_CASES = {
    # Genre and mood never match any song, so all 30 songs score identically on those components and ranking collapses to energy proximity alone.
    "Nonexistent Genre+Mood": {"genre": "vaporwave", "mood": "melancholic", "energy": 0.5},

    # energy=-1.0 is below the valid [0,1] range, making every energy similarity score negative and inverting the energy preference signal.
    "Negative Energy": {"genre": "pop", "mood": "happy", "energy": -1.0},

    # energy=5.0 is far above the valid [0,1] range, driving all energy similarity scores below -3.0 so every recommendation returns a negative total score.
    "Energy Way Above Max": {"genre": "rock", "mood": "intense", "energy": 5.0},

    # The "energy" key is omitted entirely; the algorithm silently defaults to 0.5 with no warning, hiding the missing preference from the user.
    "Missing Energy Key": {"genre": "jazz", "mood": "chill"},

    # Empty strings never match any song's genre or mood, so the profile behaves identically to having no preferences at all.
    "Empty String Genre/Mood": {"genre": "", "mood": "", "energy": 0.7},

    # No song matches either category, so the top-3 results are determined purely by which songs happen to have energy closest to 0.5 in catalog order.
    "Uniform No-Match": {"genre": "nonexistent", "mood": "nonexistent", "energy": 0.5},

    # energy=0.0 is the valid minimum; tests that the algorithm correctly rewards the lowest-energy songs without wrapping or clamping.
    "Energy Boundary Min": {"genre": "ambient", "mood": "chill", "energy": 0.0},

    # energy=1.0 is the valid maximum; confirms the distance formula reaches its floor of 0.0 similarity for songs at the opposite extreme.
    "Energy Boundary Max": {"genre": "metal", "mood": "intense", "energy": 1.0},
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

    # for label, user_prefs in USERS.items():
    #     recommendations = recommend_songs(user_prefs, songs, k=5)
    #     print_recommendations(label, recommendations)

    for label, user_prefs in EDGE_CASES.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_recommendations(label, recommendations)


if __name__ == "__main__":
    main()
