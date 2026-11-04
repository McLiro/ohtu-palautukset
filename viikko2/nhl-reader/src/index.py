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

def main():
    season = input("Select a season (e.g. 2024-25): ")
    nationality = input("Select a nationality (e.g. FIN): ")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    table = generate_table(players, season, nationality)
    Console().print(table)

if __name__ == "__main__":
    main()
