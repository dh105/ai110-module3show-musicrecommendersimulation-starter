# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: Vibe Catcher   

---

## 2. Intended Use  

This recommender suggests songs from a fixed 30-song catalog based on a user's preferred genre, mood, and energy level. It assumes the user knows exactly what they want and can express it as a single genre and mood. There's no browsing, history, or feedback loop. This is a classroom simulation built to explore how scoring logic and catalog design shape what gets recommended, not a production tool.

---

## 3. How the Model Works  

Every song gets a score based on three things: whether its genre matches what you said you like (+2 points), whether its mood matches (+1 point), and how close its energy level is to yours (up to +1 point, scaled by distance). The genre weight is doubled because genre tends to be the strongest signal for whether someone will enjoy a song. The top 5 highest-scoring songs are returned as recommendations. The mood check was temporarily removed during testing to observe how rankings shifted — it confirmed that mood acts as a tiebreaker more than a primary filter.

---

## 4. Data  


The catalog contains 30 songs across 5 genres (pop, rock, jazz, hip-hop, electronic) and 3 moods (happy, sad, chill). Energy levels range from 0.1 to 0.9 but are clustered at the extremes, with few songs in the middle. I added a few songs to ensure each genre had at least one representative but did not attempt to balance energy or mood distributions. The dataset mostly reflects mainstream tastes and lacks representation of niche genres or complex moods.
## 5. Strengths  


The system performs well for users with clear, extreme preferences (e.g., high-energy pop or low-energy jazz) because the catalog has more songs that match those profiles. The genre weighting effectively surfaces songs that fit the user's stated favorite genre, which is often the most important factor in music preference. The energy scoring also helps differentiate songs within a genre, giving users some variety while still aligning with their overall vibe.

## 6. Limitations and Bias   

The catalog has a thin middle energy range; very few songs have energy between 0.5 - 0.7. Users with this energy range will find mediocre recommendations. In cases where the user has an extreme energy preference (very low or very high), the system performs better because there are more songs that match those preferences. 
## 7. Evaluation  

I tested three standard profiles (high-energy pop, chill lofi, deep intense rock) plus eight adversarial edge cases designed to break the scoring. I noticed that the nonexistent genre profile and the uniform no-match profile returned the exact same top-5 list, which revealed that catalog load order decides rankings when nothing matches. Temporarily removing the mood check showed that mood's 1-point weight is just enough to swap two songs' positions but not enough to change who dominates the top results overall.

## 8. Future Work  

I would expand the dataset to include more songs, especially in the mid-energy range, and add more nuanced features like sub-genres or lyrical themes. I could introduce a mechanism to ensure that the top results aren't all from the same genre or energy level, even if they have similar scores. Finally, I would explore ways to handle users with more complex tastes, such as those who like multiple genres or moods simultaneously.
## 9. Personal Reflection  

It was interesting to learn how scaling works in recommender systems. I didn't understand how important it is to make calculations. I learnt that the dataset compromises a major part of the process; if the dataset is not well balanced, the recommendations will be skewed. I want to explore the bias and limitations of the dataset mroe in the future.