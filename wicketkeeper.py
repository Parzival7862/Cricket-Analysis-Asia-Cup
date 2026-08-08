# wicketkeeper.py
# Handles wicketkeeper statistics from wicketkeeper_data_odi.csv
# Inherits from BaseData class

from base import BaseData


class Wicketkeeper(BaseData):
    """
    A class to manage and search wicketkeeper statistics.
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
    
    def get_players_by_matches(self, min_matches):
        """
        Takes minimum matches (int)
        Returns dict of players who played MORE than min_matches
        Format: {player_name: matches, ...}
        """
        results = {}
        
        for player in self.data:
            matches = int(player['Matches'])
            if matches > min_matches:
                results[player['Player Name']] = matches
        
        return results
    
    def get_players_by_dismissals(self, min_dismissals):
        """
        Takes minimum dismissals (int)
        Returns dict of players with MORE than min_dismissals
        Format: {player_name: dismissals, ...}
        """
        results = {}
        
        for player in self.data:
            dismissals = int(player['Dismissals'])
            if dismissals > min_dismissals:
                results[player['Player Name']] = dismissals
        
        return results
    
    def get_players_by_country(self, country):
        """
        Takes a country name (string)
        Returns dict of players from that country
        Format: {player_name: country, ...}
        """
        results = {}
        country = country.strip().lower()
        
        for player in self.data:
            if player['Country'].strip().lower() == country:
                results[player['Player Name']] = player['Country']
        
        return results
    
    def get_players_by_max_dismissals(self, min_max_dismissals):
        """
        Takes minimum max dismissals in a match (int)
        Returns dict of players with MORE than min_max_dismissals
        Format: {player_name: max_dismissals, ...}
        """
        results = {}
        
        for player in self.data:
            # Handle trailing space in data
            max_dismissals = int(player['Maximum Dismissals'].strip())
            if max_dismissals > min_max_dismissals:
                results[player['Player Name']] = max_dismissals
        
        return results


# ===================== TESTING =====================
if __name__ == "__main__":
    test_path = "data/wicketkeeper_data_odi.csv"
    
    print("=== Testing Wicketkeeper Class ===\n")
    
    # Create Wicketkeeper object
    wk_obj = Wicketkeeper(test_path)
    
    # Test 1: Check if data loaded
    print(f"Total wicketkeepers loaded: {len(wk_obj.data)}")
    assert len(wk_obj.data) > 0, "Data should not be empty"
    print("✓ Data loaded successfully\n")
    
    # Test 2: Get player stats
    print("--- Testing get_player_stats('MS Dhoni') ---")
    dhoni = wk_obj.get_player_stats('MS Dhoni')
    if dhoni:
        print(f"Stats: {dhoni}")
    assert dhoni is not None, "Dhoni should be found"
    print("✓ get_player_stats works\n")
    
    # Test 3: Get players by matches (more than 15)
    print("--- Testing get_players_by_matches(15) ---")
    experienced = wk_obj.get_players_by_matches(15)
    print(f"Players with more than 15 matches: {len(experienced)}")
    print(f"Results: {experienced}")
    print("✓ get_players_by_matches works\n")
    
    # Test 4: Get players by dismissals (more than 20)
    print("--- Testing get_players_by_dismissals(20) ---")
    top_keepers = wk_obj.get_players_by_dismissals(20)
    print(f"Players with more than 20 dismissals: {len(top_keepers)}")
    print(f"Results: {top_keepers}")
    print("✓ get_players_by_dismissals works\n")
    
    # Test 5: Get players by country
    print("--- Testing get_players_by_country('India') ---")
    indian_keepers = wk_obj.get_players_by_country('India')
    print(f"Indian wicketkeepers: {len(indian_keepers)}")
    print(f"Results: {indian_keepers}")
    print("✓ get_players_by_country works\n")
    
    # Test 6: Get players by max dismissals (more than 4)
    print("--- Testing get_players_by_max_dismissals(4) ---")
    top_performers = wk_obj.get_players_by_max_dismissals(4)
    print(f"Players with more than 4 max dismissals in a match: {len(top_performers)}")
    print(f"Results: {top_performers}")
    print("✓ get_players_by_max_dismissals works\n")
    
    print("=== All Tests Passed ===")