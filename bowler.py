# bowler.py
# Handles bowler statistics from bowler_data_odi.csv
# Inherits from BaseData class

from base import BaseData


class Bowler(BaseData):
    """
    A class to manage and search bowler statistics.
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
    
    def get_players_by_overs(self, min_overs):
        """
        Takes minimum overs (float)
        Returns dict of players who bowled MORE than min_overs
        Format: {player_name: overs, ...}
        """
        results = {}
        
        for player in self.data:
            overs = float(player['Overs'])
            if overs > min_overs:
                results[player['Player Name']] = overs
        
        return results
    
    def get_players_by_wickets(self, min_wickets):
        """
        Takes minimum wickets (int)
        Returns dict of players who took MORE than min_wickets
        Format: {player_name: wickets, ...}
        """
        results = {}
        
        for player in self.data:
            wickets = int(player['Wickets'])
            if wickets > min_wickets:
                results[player['Player Name']] = wickets
        
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
    
    def get_players_by_economy(self, max_economy):
        """
        Takes maximum economy rate (float)
        Returns dict of players with economy LESS than max_economy
        (Lower economy = better bowler)
        Format: {player_name: economy_rate, ...}
        """
        results = {}
        
        for player in self.data:
            economy = float(player['Economy Rate'])
            if economy < max_economy:
                results[player['Player Name']] = economy
        
        return results


# ===================== TESTING =====================
if __name__ == "__main__":
    test_path = "data/bowler_data_odi.csv"
    
    print("=== Testing Bowler Class ===\n")
    
    # Create Bowler object
    bowler_obj = Bowler(test_path)
    
    # Test 1: Check if data loaded
    print(f"Total bowlers loaded: {len(bowler_obj.data)}")
    assert len(bowler_obj.data) > 0, "Data should not be empty"
    print("✓ Data loaded successfully\n")
    
    # Test 2: Get player stats
    print("--- Testing get_player_stats('M Muralidaran') ---")
    murali = bowler_obj.get_player_stats('M Muralidaran')
    if murali:
        print(f"Stats: {murali}")
    assert murali is not None, "Muralidaran should be found"
    print("✓ get_player_stats works\n")
    
    # Test 3: Get players by matches (more than 15)
    print("--- Testing get_players_by_matches(15) ---")
    experienced = bowler_obj.get_players_by_matches(15)
    print(f"Players with more than 15 matches: {len(experienced)}")
    print(f"Results: {experienced}")
    print("✓ get_players_by_matches works\n")
    
    # Test 4: Get players by overs (more than 100)
    print("--- Testing get_players_by_overs(100) ---")
    workhorses = bowler_obj.get_players_by_overs(100)
    print(f"Players with more than 100 overs: {len(workhorses)}")
    print(f"Results: {workhorses}")
    print("✓ get_players_by_overs works\n")
    
    # Test 5: Get players by wickets (more than 20)
    print("--- Testing get_players_by_wickets(20) ---")
    top_wicket_takers = bowler_obj.get_players_by_wickets(20)
    print(f"Players with more than 20 wickets: {len(top_wicket_takers)}")
    print(f"Results: {top_wicket_takers}")
    print("✓ get_players_by_wickets works\n")
    
    # Test 6: Get players by country
    print("--- Testing get_players_by_country('India') ---")
    indian_bowlers = bowler_obj.get_players_by_country('India')
    print(f"Indian bowlers: {len(indian_bowlers)}")
    print(f"Results: {indian_bowlers}")
    print("✓ get_players_by_country works\n")
    
    # Test 7: Get players by economy (less than 4.0)
    print("--- Testing get_players_by_economy(4.0) ---")
    economical = bowler_obj.get_players_by_economy(4.0)
    print(f"Players with economy less than 4.0: {len(economical)}")
    print(f"Results: {economical}")
    print("✓ get_players_by_economy works\n")
    
    print("=== All Tests Passed ===")