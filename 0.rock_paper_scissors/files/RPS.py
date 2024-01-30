import random
from collections import defaultdict

available_plays = ['R', 'P', 'S']

win_response = {
    'R': 'P',
    'P': 'S',
    'S': 'R'
}

# Instantiate a dictionary to register `played_history` combinations
# and fetch `next_play_hist` combinations
repeats = defaultdict(int)

# Length of both `played_history` and `next_play_hist` combinations
memory_len = 7

def player(prev_play, opponent_history = []):

    # No empty strings as registered plays in `opponent_history`
    if prev_play != "":
        opponent_history.append(prev_play)

    # Return arbitrary plays until `opponent_history` = `memory_len`
    if (len(opponent_history) < memory_len):
        return random.choice(available_plays)

    # Concatenate the last `memory_len` plays the opponent played
    played_history = "".join(opponent_history[-memory_len:])

    # Register in `repeats` how many times each `played_history` combination is played 
    repeats[played_history] += 1

    # Create three new `next_play_hist` combinations of plays by
    # dropping the oldest play from `played_history` and concatenating them 
    # with the three `available_plays`
    next_play_hist = [
        played_history[1:] + next_play for next_play in available_plays
    ]

    # Mode or most repeated combination of previous plays
    most_played_hist = 0

    # Position of the play, ranges from 0 to 2
    play = 0
 
    for p, nph in enumerate(next_play_hist):

        # Compute how many times the opponent played each `next_play_hist` combination,
        # and compare it with the most repeated combination of plays `most_played_hist`
        if repeats[nph] > most_played_hist:

            # If True, update both the new record of the mode for `most_played_hist`..
            most_played_hist = repeats[nph]

            # ..and the position of the play for this new mode record
            play = p

    # According to the `win_response` dictionary, 
    # return the best response with the optimized `play`
    return win_response[available_plays[play]]