import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def _score_with_reasons(self, user: UserProfile, song: Song) -> Tuple[float, List[str]]:
        """Return a (score, reasons) tuple for a song against a user profile."""
        score = 0.0
        reasons = []

        if song.genre == user.favorite_genre:
            score += 2.0
            reasons.append(f"genre match ({song.genre}, +2.0)")

        # if song.mood == user.favorite_mood:
        #     score += 1.0
        #     reasons.append(f"mood match ({song.mood}, +1.0)")

        energy_sim = 1.0 - abs(song.energy - user.target_energy)
        score += energy_sim
        reasons.append(f"energy similarity {energy_sim:.2f}")

        return score, reasons

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k songs ranked by score for the given user."""
        scored = sorted(self.songs, key=lambda s: self._score_with_reasons(user, s)[0], reverse=True)
        return scored[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a human-readable string explaining why a song was recommended."""
        _, reasons = self._score_with_reasons(user, song)
        return "Matched on: " + ", ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    return songs


def _score_song_with_reasons(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song dict against user preference dict and return (score, reasons)."""
    score = 0.0
    reasons = []

    if song.get("genre") == user_prefs.get("genre"):
        score += 2.0
        reasons.append(f"genre match ({song['genre']}, +2.0)")

    # if song.get("mood") == user_prefs.get("mood"):
    #     score += 1.0
    #     reasons.append(f"mood match ({song['mood']}, +1.0)")

    energy_sim = 1.0 - abs(song["energy"] - user_prefs.get("energy", 0.5))
    score += energy_sim
    reasons.append(f"energy similarity {energy_sim:.2f}")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score, reasons = _score_song_with_reasons(user_prefs, song)
        scored.append((song, score, "Matched on: " + ", ".join(reasons)))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
