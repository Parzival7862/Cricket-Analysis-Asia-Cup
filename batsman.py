# batsman.py
# Handles batsman statistics from batsman_data_odi.csv
# Inherits from BaseData class

from base import BaseData


class Batsman(BaseData):
    """
    A class to manage and search batsman statistics.
    Inherits __init__ and load_data from BaseData.
    """
    
    def get_player_stats(self, player_name):
        """
        Takes a player name (string)
        Returns the full stats dictionary for that player
        Returns None if player not found
        """
        player_name = player_name.strip().lower()
        
        for player in self.data:
            if player['Player Name'].strip().lower() == player_name:
                return player
        
        return None
    
    def get_players_by_runs(self, min_runs):
        """
        Takes minimum runs (int)
        Returns dict of players who scored MORE than min_runs
        Format: {player_name: runs, player_name: runs, ...}
        """
        results = {}
        
        for player in self.data:
            runs = int(player['Runs'])
            if runs > min_runs:
                results[player['Player Name']] = runs
        
        return results
    
    def get_players_by_matches(self, min_matches):
        """
        Takes minimum matches (int)
        Returns dict of players who played MORE than min_matches
        Format: {player_name: matches, player_name: matches, ...}
        """
        results = {}
        
        for player in self.data:
            matches = int(player['Matches'])
            if matches > min_matches:
                results[player['Player Name']] = matches
        
        return results
    
    def get_players_by_centuries(self, min_centuries):
        """
        Takes minimum centuries (int)
        Returns dict of players who scored MORE than min_centuries
        Format: {player_name: centuries, player_name: centuries, ...}
        """
        results = {}
        
        for player in self.data:
            centuries = int(player['Centuries'])
            if centuries > min_centuries:
                results[player['Player Name']] = centuries
        
        return results


# ===================== TESTING =====================
if __name__ == "__main__":
    test_path = "data/batsman_data_odi.csv"
    
    print("=== Testing Batsman Class ===\n")
    
    # Create Batsman object
    batsman_obj = Batsman("database/batsman_data_odi.csv")
    
    # Test 1: Check if data loaded
    print(f"Total batsmen loaded: {len(batsman_obj.data)}")
    assert len(batsman_obj.data) > 0, "Data should not be empty"
    print("✓ Data loaded successfully\n")
    
    # Test 2: Get player stats
    print("--- Testing get_player_stats('SR Tendulkar') ---")
    tendulkar = batsman_obj.get_player_stats('SR Tendulkar')
    if tendulkar:
        print(f"Stats: {tendulkar}")
    assert tendulkar is not None, "Tendulkar should be found"
    print("✓ get_player_stats works\n")
    
    # Test 3: Get players by runs (more than 500)
    print("--- Testing get_players_by_runs(500) ---")
    high_scorers = batsman_obj.get_players_by_runs(500)
    print(f"Players with more than 500 runs: {len(high_scorers)}")
    print(f"Results: {high_scorers}")
    print("✓ get_players_by_runs works\n")
    
    # Test 4: Get players by matches (more than 20)
    print("--- Testing get_players_by_matches(20) ---")
    experienced = batsman_obj.get_players_by_matches(20)
    print(f"Players with more than 20 matches: {len(experienced)}")
    print(f"Results: {experienced}")
    print("✓ get_players_by_matches works\n")
    
    # Test 5: Get players by centuries (more than 3)
    print("--- Testing get_players_by_centuries(3) ---")
    centurions = batsman_obj.get_players_by_centuries(3)
    print(f"Players with more than 3 centuries: {len(centurions)}")
    print(f"Results: {centurions}")
    print("✓ get_players_by_centuries works\n")
    
    print("=== All Tests Passed ===")