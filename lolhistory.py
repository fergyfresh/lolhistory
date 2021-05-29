import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


ELO_MAP = {
    "Iron": 0,
    "Bronze": 400,
    "Silver": 800,
    "Gold": 1200,
    "Platinum": 1600,
    "Diamond": 2000,
}

def get_ranks_from_html(names, stats):
    tuples = zip(names, stats)
    rank = []
    for name, stat in tuples:
        division = name.text.replace('\n', '').strip()
        lp = stat.dd.text.split('\n')[1].strip()
        rank.append((division, lp))
    print(rank)
    return rank


def get_all_ranks(summoner_name):
    all_ranks = []
    last_ranks_len = 0
    i = 1
    while True:
        r = requests.get(f"https://lolchess.gg/profile/na/{summoner_name}/s5/lp_history/{i}")
        soup = BeautifulSoup(r.content)
        stats = soup.find_all('div', 'stats')
        names = soup.find_all('span', 'name')

        if not stats or not names or r.status_code != 200:
            break
        new_ranks = get_ranks_from_html(names, stats)
        all_ranks += new_ranks

        if last_ranks_len == len(all_ranks) or len(new_ranks) < 20:
            break
        last_ranks_len = len(all_ranks)
        i += 1
    
    return all_ranks


def get_elo_from_rank(rank, lp):
    division, tier = rank.split(' ')
    return ELO_MAP[division] - int(tier) * 100 + int(lp)


if __name__ == "__main__":
    import sys

    summoner_name = sys.argv[1]

    ranks = get_all_ranks(summoner_name)

    normalized_ranks = [get_elo_from_rank(*rank) for rank in ranks[::-1]]


    ax = plt.gca()

    yticks = []
    ytick_labels = []
    for elo in ELO_MAP:
        for i in range(4,0, -1):
            yticks.append(get_elo_from_rank(f"{elo} {i}", 0))
            ytick_labels.append(f"{elo} {i}")


    ax.set_yticks(yticks)
    ax.set_yticklabels(ytick_labels)
    ax.grid(linestyle='-')
    plt.title(f"{summoner_name} Set 5 match history")

    plt.plot(normalized_ranks)
    plt.show()