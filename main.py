# main.py
# ============================================================
# ASIA CUP CRICKET STATISTICS LOOKUP SYSTEM
# ============================================================
# Main file that imports all classes and provides user interface
# for searching and displaying Asia Cup cricket statistics.
# ============================================================

from match import Match
from batsman import Batsman
from bowler import Bowler
from wicketkeeper import Wicketkeeper
from champions import Tournament

# ==================== FILE PATHS ====================
MATCH_FILE = "database/asiacup.csv"
BATSMAN_FILE = "database/batsman_data_odi.csv"
BOWLER_FILE = "database/bowler_data_odi.csv"
WICKETKEEPER_FILE = "database/wicketkeeper_data_odi.csv"
TOURNAMENT_FILE = "database/champion.csv"


# ==================== DISPLAY FUNCTIONS ====================

def print_banner():
    """Display the welcome banner"""
    print("\n" + "=" * 60)
    print("    ASIA CUP CRICKET STATISTICS LOOKUP SYSTEM")
    print("=" * 60)
    print("      Your one-stop shop for Asia Cup ODI stats!")
    print("=" * 60 + "\n")


def display_dict_results(results, value_label="Value"):
    """
    Display dictionary results in a formatted table
    Format: {name: value, ...}
    """
    if not results or len(results) == 0:
        print("\n[X] No results found.\n")
        return
    
    print("\n" + "-" * 50)
    print(f"{'Player/Team':<30} | {value_label}")
    print("-" * 50)
    
    for name, value in results.items():
        print(f"{name:<30} | {value}")
    
    print("-" * 50)
    print(f"Total results: {len(results)}")
    print()


def display_list_results(results):
    """
    Display list of dictionaries in a formatted way
    For match results and tournament results
    """
    if not results or len(results) == 0:
        print("\n[X] No results found.\n")
        return
    
    print("\n" + "=" * 60)
    count = 1
    for item in results:
        print(f"\n--- Result #{count} ---")
        for key, value in item.items():
            print(f"  {key}: {value}")
        count += 1
    
    print("\n" + "=" * 60)
    print(f"Total results: {len(results)}")
    print()


def display_single_result(result):
    """Display a single dictionary result (player stats, tournament info)"""
    if result is None:
        print("\n[X] No results found.\n")
        return
    
    print("\n" + "-" * 40)
    for key, value in result.items():
        print(f"  {key}: {value}")
    print("-" * 40 + "\n")


# ==================== MENU FUNCTIONS ====================

def main_menu():
    """Display main menu and return user choice"""
    print("\n" + "=" * 40)
    print("            MAIN MENU")
    print("=" * 40)
    print("  1. Match Statistics")
    print("  2. Batsman Statistics")
    print("  3. Bowler Statistics")
    print("  4. Wicketkeeper Statistics")
    print("  5. Tournament History")
    print("  6. Export Search to File")
    print("  0. Exit")
    print("=" * 40)
    
    choice = input("Enter your choice (0-6): ").strip()
    return choice


def match_menu(match_obj):
    """Handle match search options"""
    while True:
        print("\n" + "-" * 40)
        print("         MATCH STATISTICS")
        print("-" * 40)
        print("  1. Search by Team")
        print("  2. Search by Year")
        print("  3. Search by Player of the Match")
        print("  0. Back to Main Menu")
        print("-" * 40)
        
        choice = input("Enter your choice (0-3): ").strip()
        
        if choice == "1":
            team = input("Enter team name (e.g., India, Pakistan, Sri Lanka): ").strip()
            if team:
                results = match_obj.search_by_team(team)
                display_list_results(results)
            else:
                print("[X] Please enter a valid team name.")
                
        elif choice == "2":
            try:
                year = int(input("Enter year (e.g., 2018): ").strip())
                results = match_obj.search_by_year(year)
                display_list_results(results)
            except ValueError:
                print("[X] Please enter a valid year (number).")
                
        elif choice == "3":
            player = input("Enter player name (e.g., Virat Kohli): ").strip()
            if player:
                results = match_obj.search_by_player_of_match(player)
                display_list_results(results)
            else:
                print("[X] Please enter a valid player name.")
                
        elif choice == "0":
            break
        else:
            print("[X] Invalid choice. Please try again.")


def batsman_menu(batsman_obj):
    """Handle batsman search options"""
    while True:
        print("\n" + "-" * 40)
        print("         BATSMAN STATISTICS")
        print("-" * 40)
        print("  1. Get Player Stats")
        print("  2. Search by Minimum Runs")
        print("  3. Search by Minimum Matches")
        print("  4. Search by Minimum Centuries")
        print("  0. Back to Main Menu")
        print("-" * 40)
        
        choice = input("Enter your choice (0-4): ").strip()
        
        if choice == "1":
            player = input("Enter player name (e.g., SR Tendulkar): ").strip()
            if player:
                result = batsman_obj.get_player_stats(player)
                display_single_result(result)
            else:
                print("[X] Please enter a valid player name.")
                
        elif choice == "2":
            try:
                min_runs = int(input("Enter minimum runs: ").strip())
                results = batsman_obj.get_players_by_runs(min_runs)
                display_dict_results(results, "Runs")
            except ValueError:
                print("[X] Please enter a valid number.")
                
        elif choice == "3":
            try:
                min_matches = int(input("Enter minimum matches: ").strip())
                results = batsman_obj.get_players_by_matches(min_matches)
                display_dict_results(results, "Matches")
            except ValueError:
                print("[X] Please enter a valid number.")
                
        elif choice == "4":
            try:
                min_centuries = int(input("Enter minimum centuries: ").strip())
                results = batsman_obj.get_players_by_centuries(min_centuries)
                display_dict_results(results, "Centuries")
            except ValueError:
                print("[X] Please enter a valid number.")
                
        elif choice == "0":
            break
        else:
            print("[X] Invalid choice. Please try again.")


def bowler_menu(bowler_obj):
    """Handle bowler search options"""
    while True:
        print("\n" + "-" * 40)
        print("         BOWLER STATISTICS")
        print("-" * 40)
        print("  1. Get Player Stats")
        print("  2. Search by Minimum Matches")
        print("  3. Search by Minimum Overs")
        print("  4. Search by Minimum Wickets")
        print("  5. Search by Country")
        print("  6. Search by Maximum Economy Rate")
        print("  0. Back to Main Menu")
        print("-" * 40)
        
        choice = input("Enter your choice (0-6): ").strip()
        
        if choice == "1":
            player = input("Enter player name (e.g., M Muralidaran): ").strip()
            if player:
                result = bowler_obj.get_player_stats(player)
                display_single_result(result)
            else:
                print("[X] Please enter a valid player name.")
                
        elif choice == "2":
            try:
                min_matches = int(input("Enter minimum matches: ").strip())
                results = bowler_obj.get_players_by_matches(min_matches)
                display_dict_results(results, "Matches")
            except ValueError:
                print("[X] Please enter a valid number.")
                
        elif choice == "3":
            try:
                min_overs = float(input("Enter minimum overs: ").strip())
                results = bowler_obj.get_players_by_overs(min_overs)
                display_dict_results(results, "Overs")
            except ValueError:
                print("[X] Please enter a valid number.")
                
        elif choice == "4":
            try:
                min_wickets = int(input("Enter minimum wickets: ").strip())
                results = bowler_obj.get_players_by_wickets(min_wickets)
                display_dict_results(results, "Wickets")
            except ValueError:
                print("[X] Please enter a valid number.")
                
        elif choice == "5":
            country = input("Enter country name (e.g., India): ").strip()
            if country:
                results = bowler_obj.get_players_by_country(country)
                display_dict_results(results, "Country")
            else:
                print("[X] Please enter a valid country name.")
                
        elif choice == "6":
            try:
                max_economy = float(input("Enter maximum economy rate: ").strip())
                results = bowler_obj.get_players_by_economy(max_economy)
                display_dict_results(results, "Economy Rate")
            except ValueError:
                print("[X] Please enter a valid number.")
                
        elif choice == "0":
            break
        else:
            print("[X] Invalid choice. Please try again.")


def wicketkeeper_menu(wk_obj):
    """Handle wicketkeeper search options"""
    while True:
        print("\n" + "-" * 40)
        print("       WICKETKEEPER STATISTICS")
        print("-" * 40)
        print("  1. Get Player Stats")
        print("  2. Search by Minimum Matches")
        print("  3. Search by Minimum Dismissals")
        print("  4. Search by Country")
        print("  5. Search by Max Dismissals in a Match")
        print("  0. Back to Main Menu")
        print("-" * 40)
        
        choice = input("Enter your choice (0-5): ").strip()
        
        if choice == "1":
            player = input("Enter player name (e.g., MS Dhoni): ").strip()
            if player:
                result = wk_obj.get_player_stats(player)
                display_single_result(result)
            else:
                print("[X] Please enter a valid player name.")
                
        elif choice == "2":
            try:
                min_matches = int(input("Enter minimum matches: ").strip())
                results = wk_obj.get_players_by_matches(min_matches)
                display_dict_results(results, "Matches")
            except ValueError:
                print("[X] Please enter a valid number.")
                
        elif choice == "3":
            try:
                min_dismissals = int(input("Enter minimum dismissals: ").strip())
                results = wk_obj.get_players_by_dismissals(min_dismissals)
                display_dict_results(results, "Dismissals")
            except ValueError:
                print("[X] Please enter a valid number.")
                
        elif choice == "4":
            country = input("Enter country name (e.g., India): ").strip()
            if country:
                results = wk_obj.get_players_by_country(country)
                display_dict_results(results, "Country")
            else:
                print("[X] Please enter a valid country name.")
                
        elif choice == "5":
            try:
                min_max = int(input("Enter minimum max dismissals in a match: ").strip())
                results = wk_obj.get_players_by_max_dismissals(min_max)
                display_dict_results(results, "Max Dismissals")
            except ValueError:
                print("[X] Please enter a valid number.")
                
        elif choice == "0":
            break
        else:
            print("[X] Invalid choice. Please try again.")


def tournament_menu(tournament_obj):
    """Handle tournament search options"""
    while True:
        print("\n" + "-" * 40)
        print("        TOURNAMENT HISTORY")
        print("-" * 40)
        print("  1. Get Tournament by Year")
        print("  2. Search by Champion Country")
        print("  3. Search by Player of the Series")
        print("  4. Search by Highest Wicket Taker")
        print("  0. Back to Main Menu")
        print("-" * 40)
        
        choice = input("Enter your choice (0-4): ").strip()
        
        if choice == "1":
            try:
                year = int(input("Enter year (e.g., 2018): ").strip())
                result = tournament_obj.get_tournament_by_year(year)
                display_single_result(result)
            except ValueError:
                print("[X] Please enter a valid year.")
                
        elif choice == "2":
            country = input("Enter champion country (e.g., India): ").strip()
            if country:
                results = tournament_obj.get_tournaments_by_champion(country)
                display_list_results(results)
            else:
                print("[X] Please enter a valid country name.")
                
        elif choice == "3":
            player = input("Enter player name (e.g., Sanath Jayasuriya): ").strip()
            if player:
                results = tournament_obj.get_tournament_by_player_of_series(player)
                display_list_results(results)
            else:
                print("[X] Please enter a valid player name.")
                
        elif choice == "4":
            player = input("Enter player name (e.g., Lasith Malinga): ").strip()
            if player:
                results = tournament_obj.get_tournament_by_highest_wicket_taker(player)
                display_list_results(results)
            else:
                print("[X] Please enter a valid player name.")
                
        elif choice == "0":
            break
        else:
            print("[X] Invalid choice. Please try again.")


def export_menu(match_obj, batsman_obj, bowler_obj, wk_obj, tournament_obj):
    """Export search results to a file"""
    print("\n" + "-" * 40)
    print("         EXPORT TO FILE")
    print("-" * 40)
    print("  1. Export all India matches")
    print("  2. Export top batsmen (500+ runs)")
    print("  3. Export top bowlers (15+ wickets)")
    print("  4. Export all tournament winners")
    print("  0. Back to Main Menu")
    print("-" * 40)
    
    choice = input("Enter your choice (0-4): ").strip()
    
    if choice == "1":
        results = match_obj.search_by_team("India")
        filename = "india_matches_export.txt"
        
    elif choice == "2":
        results = batsman_obj.get_players_by_runs(500)
        filename = "top_batsmen_export.txt"
        
    elif choice == "3":
        results = bowler_obj.get_players_by_wickets(15)
        filename = "top_bowlers_export.txt"
        
    elif choice == "4":
        results = tournament_obj.data  # All tournaments
        filename = "tournament_winners_export.txt"
        
    elif choice == "0":
        return
    else:
        print("[X] Invalid choice.")
        return
    
    # Write to file
    try:
        file = open(filename, 'w')
        file.write("=" * 50 + "\n")
        file.write("ASIA CUP STATISTICS EXPORT\n")
        file.write("=" * 50 + "\n\n")
        
        if isinstance(results, dict):
            for name, value in results.items():
                file.write(f"{name}: {value}\n")
        elif isinstance(results, list):
            for item in results:
                for key, value in item.items():
                    file.write(f"{key}: {value}\n")
                file.write("-" * 30 + "\n")
        
        file.write(f"\nTotal records: {len(results)}\n")
        file.close()
        
        print(f"\n[OK] Successfully exported to '{filename}'!")
        
    except Exception as e:
        print(f"[X] Error exporting: {e}")


# ==================== MAIN FUNCTION ====================

def main():
    """
    Main function - Entry point of the program
    Loads all data and runs the interactive menu system
    """
    # Print welcome banner
    print_banner()
    
    # Load all data files
    print("Loading data files...")
    
    try:
        match_obj = Match(MATCH_FILE)
        print(f"  [OK] Loaded {len(match_obj.data)} matches")
        
        batsman_obj = Batsman(BATSMAN_FILE)
        print(f"  [OK] Loaded {len(batsman_obj.data)} batsmen")
        
        bowler_obj = Bowler(BOWLER_FILE)
        print(f"  [OK] Loaded {len(bowler_obj.data)} bowlers")
        
        wk_obj = Wicketkeeper(WICKETKEEPER_FILE)
        print(f"  [OK] Loaded {len(wk_obj.data)} wicketkeepers")
        
        tournament_obj = Tournament(TOURNAMENT_FILE)
        print(f"  [OK] Loaded {len(tournament_obj.data)} tournaments")
        
        print("\nAll data loaded successfully!\n")
        
    except Exception as e:
        print(f"\n[X] Error loading data: {e}")
        print("Please make sure all CSV files are in the 'database' folder.")
        return
    
    # Main menu loop
    running = True
    while running:
        choice = main_menu()
        
        if choice == "1":
            match_menu(match_obj)
            
        elif choice == "2":
            batsman_menu(batsman_obj)
            
        elif choice == "3":
            bowler_menu(bowler_obj)
            
        elif choice == "4":
            wicketkeeper_menu(wk_obj)
            
        elif choice == "5":
            tournament_menu(tournament_obj)
            
        elif choice == "6":
            export_menu(match_obj, batsman_obj, bowler_obj, wk_obj, tournament_obj)
            
        elif choice == "0":
            print("\n" + "=" * 50)
            print("  Thanks for using Asia Cup Stats System!")
            print("       Made for CICS 110 Final Project")
            print("=" * 50 + "\n")
            running = False
            
        else:
            print("\n[X] Invalid choice. Please enter a number between 0-6.")
    

# ==================== RUN PROGRAM ====================

if __name__ == "__main__":
    main()