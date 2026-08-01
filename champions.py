# tournament.py
# Handles tournament/champion data from champion.csv
# Inherits from BaseData class

from base import BaseData


class Tournament(BaseData):
    """
    A class to manage and search Asia Cup tournament data.
    Inherits __init__ and load_data from BaseData.
    """
    
    def get_tournament_by_year(self, year):
        """
        Takes a year (int)
        Returns the tournament dictionary for that year
        Returns None if year not found
        """
        for tournament in self.data:
            if int(tournament['Year']) == year:
                return tournament
        
        return None
    
    def get_tournaments_by_champion(self, champion):
        """
        Takes a country name (string)
        Returns list of tournaments won by that country
        Format: list of tournament dictionaries
        """
        results = []
        champion = champion.strip().lower()
        
        for tournament in self.data:
            if tournament['Champion'].strip().lower() == champion:
                results.append(tournament)
        
        return results
    
    def get_tournament_by_player_of_series(self, player_name):
        """
        Takes a player name (string)
        Returns list of tournaments where that player was Player Of The Series
        Format: list of tournament dictionaries
        """
        results = []
        player_name = player_name.strip().lower()
        
        for tournament in self.data:
            if tournament['Player Of The Series'].strip().lower() == player_name:
                results.append(tournament)
        
        return results
    
    def get_tournament_by_highest_wicket_taker(self, player_name):
        """
        Takes a player name (string)
        Returns list of tournaments where that player was Highest Wicket Taker
        Format: list of tournament dictionaries
        """
        results = []
        player_name = player_name.strip().lower()
        
        for tournament in self.data:
            if tournament['Highest Wicket Taker'].strip().lower() == player_name:
                results.append(tournament)
        
        return results


# ===================== TESTING =====================
if __name__ == "__main__":
    test_path = "data/champion.csv"
    
    print("=== Testing Tournament Class ===\n")
    
    # Create Tournament object
    tournament_obj = Tournament(test_path)
    
    # Test 1: Check if data loaded
    print(f"Total tournaments loaded: {len(tournament_obj.data)}")
    assert len(tournament_obj.data) > 0, "Data should not be empty"
    print("✓ Data loaded successfully\n")
    
    # Test 2: Get tournament by year
    print("--- Testing get_tournament_by_year(2018) ---")
    tournament_2018 = tournament_obj.get_tournament_by_year(2018)
    if tournament_2018:
        print(f"Tournament: {tournament_2018}")
    assert tournament_2018 is not None, "2018 tournament should be found"
    print("✓ get_tournament_by_year works\n")
    
    # Test 3: Get tournaments by champion
    print("--- Testing get_tournaments_by_champion('India') ---")
    india_wins = tournament_obj.get_tournaments_by_champion('India')
    print(f"Tournaments won by India: {len(india_wins)}")
    for t in india_wins:
        print(f"  {t['Year']}: {t['Champion']}")
    print("✓ get_tournaments_by_champion works\n")
    
    # Test 4: Get tournament by player of series
    print("--- Testing get_tournament_by_player_of_series('Sanath Jayasuriya') ---")
    jayasuriya_pos = tournament_obj.get_tournament_by_player_of_series('Sanath Jayasuriya')
    print(f"Tournaments where Jayasuriya was POS: {len(jayasuriya_pos)}")
    for t in jayasuriya_pos:
        print(f"  {t['Year']}: {t['Player Of The Series']}")
    print("✓ get_tournament_by_player_of_series works\n")
    
    # Test 5: Get tournament by highest wicket taker
    print("--- Testing get_tournament_by_highest_wicket_taker('Lasith Malinga') ---")
    malinga_hwt = tournament_obj.get_tournament_by_highest_wicket_taker('Lasith Malinga')
    print(f"Tournaments where Malinga was HWT: {len(malinga_hwt)}")
    for t in malinga_hwt:
        print(f"  {t['Year']}: {t['Highest Wicket Taker']}")
    print("✓ get_tournament_by_highest_wicket_taker works\n")
    
    print("=== All Tests Passed ===")