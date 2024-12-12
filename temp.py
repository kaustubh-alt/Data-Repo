import pandas as pd

def load_ipl_data(file_path):
    """Load IPL data from a CSV file."""
    try:
        ipl_data = pd.read_csv(file_path)
        return ipl_data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def team_performance_with_toss_and_opposition(ipl_data, team_name, opposition_team=None):
    """Analyze the team's performance based on batting/bowling first, toss decisions, and opposition team."""
    if ipl_data is None:
        print("No data available to analyze.")
        return

    # Filter data for the selected team
    team_matches = ipl_data[(ipl_data['team1'] == team_name) | (ipl_data['team2'] == team_name)]

    if opposition_team:
        team_matches = team_matches[(team_matches['team1'] == opposition_team) | (team_matches['team2'] == opposition_team)]

    # Batting first
    batting_first = team_matches[(team_matches['toss_winner'] == team_name) & (team_matches['toss_decision'] == 'bat')]
    batting_first_wins = batting_first[batting_first['winner'] == team_name]
    batting_first_win_rate = len(batting_first_wins) / len(batting_first) * 100 if len(batting_first) > 0 else 0

    # Bowling first
    bowling_first = team_matches[(team_matches['toss_winner'] == team_name) & (team_matches['toss_decision'] == 'field')]
    bowling_first_wins = bowling_first[bowling_first['winner'] == team_name]
    bowling_first_win_rate = len(bowling_first_wins) / len(bowling_first) * 100 if len(bowling_first) > 0 else 0

    # Overall toss impact
    toss_wins = team_matches[team_matches['toss_winner'] == team_name]
    toss_wins_won_match = toss_wins[toss_wins['winner'] == team_name]
    toss_win_rate = len(toss_wins_won_match) / len(toss_wins) * 100 if len(toss_wins) > 0 else 0

    print(f"Performance of {team_name}:")
    if opposition_team:
        print(f"Against {opposition_team}:")
    print(f"- Batting first: {len(batting_first_wins)} wins out of {len(batting_first)} matches ({batting_first_win_rate:.2f}% win rate)")
    print(f"- Bowling first: {len(bowling_first_wins)} wins out of {len(bowling_first)} matches ({bowling_first_win_rate:.2f}% win rate)")
    print(f"- Toss impact: {len(toss_wins_won_match)} wins out of {len(toss_wins)} tosses ({toss_win_rate:.2f}% win rate)")

    # Make a decision
    if batting_first_win_rate > bowling_first_win_rate:
        print(f"Decision: {team_name} should prefer batting first.")
    elif bowling_first_win_rate > batting_first_win_rate:
        print(f"Decision: {team_name} should prefer bowling first.")
    else:
        print(f"Decision: {team_name} has equal performance in batting and bowling first.")

# Load the data
file_path = "C:/Programs/mini_project/matches.csv"  # Replace with the actual file path
ipl_data = load_ipl_data(file_path)

# Analyze a team's performance
team_name = "Mumbai Indians"  # Replace with the desired team name
opposition_team = "Chennai Super Kings"  # Replace with the desired opposition team, or None
team_performance_with_toss_and_opposition(ipl_data, team_name, opposition_team)
