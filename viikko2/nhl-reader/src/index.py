from rich.console import Console
from rich.table import Table
from player import PlayerReader, PlayerStats

def generate_table(players, season, nationality):
    table = Table(title=f"Player statistics for {season}, {nationality}")
    table.add_column("Name")
    table.add_column("Team")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.goals + player.assists),
        )

    return table

def select_players(stats, selection):
    if selection == "n":
        nationality = input("Select a nationality (e.g. FIN): ")
        return stats.top_scorers_by_nationality(nationality), nationality
    if selection == "t":
        team = input("Select a team (e.g. DAL): ")
        return stats.top_scorers_by_team(team), team
    raise ValueError("Select either n for nationality or t for team")

def main():
    season = input("Select a season (e.g. 2024-25): ")
    selection = input("Search by nationality or team (n/t): ")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players, filter_value = select_players(stats, selection)
    table = generate_table(players, season, filter_value)
    Console().print(table)

if __name__ == "__main__":
    main()
