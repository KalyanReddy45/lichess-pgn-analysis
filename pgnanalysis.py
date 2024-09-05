import chess.pgn

# Initialize counters
tournament_games = 0
non_tournament_games = 0

# Open the PGN file
with open("lichess_db_standard_rated_2013-03.pgn") as pgn_file:  # Replace "lichess_data.pgn" with your PGN file name
    while True:
        # Parse the next game in the PGN file
        game = chess.pgn.read_game(pgn_file)
        if game is None:
            break  # Stop when all games are read

        # Extract the "Event" header and check if it's a tournament game
        event = game.headers.get("Event", "").lower()  # Get the event field in lowercase
        if "tournament" in event:
            tournament_games += 1
        else:
            non_tournament_games += 1

# Output the results
print(f"Tournament games: {tournament_games}")
print(f"Non-tournament games: {non_tournament_games}")
