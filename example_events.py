# Example Events for Gaming

This file contains detailed example events that can be used in a gaming context. Each event includes a description of the event, its significance, and any relevant parameters.

1. **Player Joined**  
   - **Description:** A player joins the game.  
   - **Significance:** Indicates that a new player has entered the game environment.  
   - **Parameters:**  
     - `player_id`: Unique identifier for the player.  
     - `join_time`: Timestamp of when the player joined.  

2. **Player Scored**  
   - **Description:** A player scores points.  
   - **Significance:** Tracks player performance and game progression.  
   - **Parameters:**  
     - `player_id`: Unique identifier for the player.  
     - `score`: Number of points scored.  
     - `timestamp`: Time when the score was achieved.  

3. **Item Collected**  
   - **Description:** A player collects an item.  
   - **Significance:** Informs gameplay about inventory changes.  
   - **Parameters:**  
     - `player_id`: Unique identifier for the player.  
     - `item_id`: Identifier for the collected item.  
     - `collection_time`: Timestamp of when the item was collected.  

4. **Level Up**  
   - **Description:** A player levels up in the game.  
   - **Significance:** Indicates progression of the player through the game.  
   - **Parameters:**  
     - `player_id`: Unique identifier for the player.  
     - `new_level`: The level the player has reached.  
     - `level_up_time`: Timestamp of when the level was achieved.  

5. **Player Died**  
   - **Description:** A player dies in the game.  
   - **Significance:** Affects the player's ability to continue and might trigger penalties.  
   - **Parameters:**  
     - `player_id`: Unique identifier for the player.  
     - `death_time`: Timestamp of when the player died.  
     - `cause_of_death`: Description of how the player died (e.g., enemy attack, fall).  

6. **Game Started**  
   - **Description:** The game session starts.  
   - **Significance:** Marks the beginning of a new gaming session.  
   - **Parameters:**  
     - `session_id`: Unique identifier for the game session.  
     - `start_time`: Timestamp when the game started.  

7. **Game Ended**  
   - **Description:** The game session ends.  
   - **Significance:** Indicates the completion of a gaming session.  
   - **Parameters:**  
     - `session_id`: Unique identifier for the game session.  
     - `end_time`: Timestamp when the game ended.  
     - `winner_id`: Player ID of the winning player (if applicable).  

8. **Achievement Unlocked**  
   - **Description:** A player unlocks an achievement.  
   - **Significance:** Rewards players for reaching certain milestones.  
   - **Parameters:**  
     - `player_id`: Unique identifier for the player.  
     - `achievement_id`: Unique identifier for the achievement.  
     - `unlock_time`: Timestamp of when the achievement was unlocked.  

9. **Player Chatted**  
   - **Description:** A player sends a chat message.  
   - **Significance:** Facilitates communication between players.  
   - **Parameters:**  
     - `player_id`: Unique identifier for the player.  
     - `message`: The content of the chat message.  
     - `chat_time`: Timestamp when the message was sent.  

10. **Matchmaking Attempt**  
    - **Description:** A player attempts to join a match.  
    - **Significance:** Tracks attempts to find opponents or teammates.  
    - **Parameters:**  
      - `player_id`: Unique identifier for the player.  
      - `attempt_time`: Timestamp when the matchmaking attempt was made.  
      - `queue_position`: Player's position in the matchmaking queue.

This file serves as a reference for developers to implement event tracking in gaming applications.