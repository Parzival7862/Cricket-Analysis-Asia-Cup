# match.py
# Handles Asia Cup match data from asiacup.csv
# Inherits from BaseData class

from base import BaseData


class Match(BaseData):
    """
    A class to manage and search Asia Cup match data.
    Inherits __init__ and load_data from BaseData.
    """
    
    def search_by_team(self, team_name):
        """
        Takes a team name (string)
        Returns all matches where the team is either 'Team' OR 'Opponent'
        Returns a list of match dictionaries
        """
        results = []
        team_name = team_name.strip().lower()
        
        for match in self.data:
            # Check if team is either Team or Opponent (using 'or')
            if match['Team'].lower() == team_name or match['Opponent'].lower() == team_name:
                results.append(match)
        
        return results
    
    def search_by_year(self, year):
        """
        Takes a year (int)
        Returns all matches played in that year
        Returns a list of match dictionaries
        """
        results = []
        
        for match in self.data:
            if int(match['Year']) == year:  # Convert string to int for comparison
                results.append(match)
        
        return results
    
    def search_by_player_of_match(self, player_name):
        """
        Takes a player name (string)
        Returns all matches where that player was 'Player Of The Match'
        Returns a list of match dictionaries
        """
        results = []
        player_name = player_name.strip().lower()
        
        for match in self.data:
            if match['Player Of The Match'].lower() == player_name:
                results.append(match)
        
        return results


# ===================== TESTING =====================
if __name__ == "__main__":
    test_path = "data/asiacup.csv"
    
    print("=== Testing Match Class (with Inheritance) ===\n")
    
    # Create Match object - uses inherited __init__ and load_data
    match_obj = Match("database/asiacup.csv")
    
    # Test 1: Check if data loaded (inherited functionality)
    print(f"Total matches loaded: {len(match_obj.data)}")
    assert len(match_obj.data) > 0, "Data should not be empty"
    print("✓ Data loaded successfully (inherited from BaseData)\n")
    
    # Test 2: Search by team
    print("--- Testing search_by_team('India') ---")
    india_matches = match_obj.search_by_team('India')
    print(f"Matches involving India: {len(india_matches)}")
    if len(india_matches) > 0:
        print(f"Sample match: {india_matches[0]}")
    assert len(india_matches) > 0, "India should have matches"
    print("✓ search_by_team works\n")
    
    # Test 3: Search by year
    print("--- Testing search_by_year(2018) ---")
    matches_2018 = match_obj.search_by_year(2018)
    print(f"Matches in 2018: {len(matches_2018)}")
    if len(matches_2018) > 0:
        print(f"Sample match: {matches_2018[0]}")
    print("✓ search_by_year works\n")
    
    # Test 4: Search by player of match
    print("--- Testing search_by_player_of_match('Virat Kohli') ---")
    kohli_potm = match_obj.search_by_player_of_match('Virat Kohli')
    print(f"Matches where Virat Kohli was POTM: {len(kohli_potm)}")
    if len(kohli_potm) > 0:
        print(f"Sample match: {kohli_potm}")
    print("✓ search_by_player_of_match works\n")
    
    print("=== All Tests Passed ===")