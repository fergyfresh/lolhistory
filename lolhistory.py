import requests
from bs4 import BeautifulSoup


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
    while True and last_ranks_len <= 313:
        r = requests.get(f"https://lolchess.gg/profile/na/iprefertacos/s5/lp_history/{i}")
        soup = BeautifulSoup(r.content)
        stats = soup.find_all('div', 'stats')
        names = soup.find_all('span', 'name')

        if not stats or not names or r.status_code != 200:
            break
        print(i)
        new_ranks = get_ranks_from_html(names, stats)
        all_ranks += new_ranks
        if last_ranks_len == len(all_ranks) or len(new_ranks) < 20:
            break
        last_ranks_len = len(all_ranks)
        print(last_ranks_len)
        i += 1
    
    return all_ranks




summoner_name = 'iprefertacos'
#ranks = get_all_ranks(summoner_name)

ranks = [('Platinum 1', '4'), ('Platinum 2', '87'), ('Platinum 2', '70'), ('Platinum 2', '43'), ('Platinum 2', '16'), ('Platinum 2', '0'), ('Platinum 2', '41'), ('Platinum 2', '31'), ('Platinum 2', '21'), ('Platinum 3', '94'), ('Platinum 3', '55'), ('Platinum 3', '39'), ('Platinum 3', '0'), ('Platinum 3', '3'), ('Platinum 3', '28'), ('Platinum 3', '0'), ('Platinum 3', '38'), ('Platinum 3', '28'), ('Platinum 3', '0'), ('Platinum 3', '38'), ('Platinum 3', '10'), ('Platinum 3', '0'), ('Platinum 3', '11'), ('Platinum 3', '37'), ('Platinum 3', '18'), ('Platinum 3', '0'), ('Platinum 3', '28'), ('Platinum 3', '10'), ('Platinum 3', '0'), ('Platinum 3', '1'), ('Platinum 3', '54'), ('Platinum 3', '75'), ('Platinum 2', '0'), ('Platinum 2', '13'), ('Platinum 2', '52'), ('Platinum 2', '76'), ('Platinum 2', '66'), ('Platinum 2', '92'), ('Platinum 2', '72'), ('Platinum 2', '95'), ('Platinum 2', '85'), ('Platinum 2', '75'), ('Platinum 1', '0'), ('Platinum 1', '1'), ('Platinum 1', '11'), ('Platinum 1', '21'), ('Platinum 1', '31'), ('Platinum 1', '0'), ('Platinum 1', '17'), ('Platinum 1', '27'), ('Platinum 1', '10'), ('Platinum 1', '0'), ('Platinum 1', '36'), ('Platinum 1', '75'), ('Diamond 4', '0'), ('Diamond 4', '0'), ('Diamond 4', '19'), ('Diamond 4', '60'), ('Diamond 4', '23'), ('Diamond 4', '47'), ('Diamond 4', '73'), ('Diamond 4', '42'), ('Diamond 4', '0'), ('Diamond 4', '26'), ('Diamond 4', '8'), ('Diamond 4', '49'), ('Diamond 4', '74'), ('Diamond 4', '99'), ('Diamond 4', '56'), ('Diamond 4', '84'), ('Diamond 4', '66'), ('Diamond 4', '56'), ('Diamond 4', '14'), ('Diamond 4', '58'), ('Diamond 4', '48'), ('Diamond 4', '31'), ('Diamond 4', '0'), ('Diamond 4', '2'), ('Platinum 1', '84'), ('Platinum 1', '65'), ('Platinum 1', '75'), ('Diamond 4', '0'), ('Diamond 4', '40'), ('Diamond 4', '30'), ('Diamond 4', '0'), ('Diamond 4', '6'), ('Diamond 4', '16'), ('Diamond 4', '26'), ('Diamond 4', '72'), ('Diamond 4', '29'), ('Diamond 4', '10'), ('Diamond 4', '75'), ('Diamond 3', '0'), ('Diamond 3', '9'), ('Diamond 3', '19'), ('Diamond 3', '0'), ('Diamond 3', '35'), ('Diamond 3', '17'), ('Diamond 3', '0'), ('Diamond 3', '49'), ('Diamond 3', '32'), ('Diamond 3', '22'), ('Diamond 3', '3'), ('Diamond 3', '13'), ('Diamond 4', '96'), ('Diamond 4', '86'), ('Diamond 4', '46'), ('Diamond 4', '19'), ('Diamond 4', '0'), ('Diamond 4', '17'), ('Diamond 4', '27'), ('Diamond 4', '10'), ('Diamond 4', '0'), ('Diamond 4', '20'), ('Diamond 4', '0'), ('Diamond 4', '22'), ('Platinum 1', '81'), ('Platinum 1', '91'), ('Platinum 1', '62'), ('Platinum 1', '19'), ('Platinum 1', '0'), ('Platinum 1', '51'), ('Platinum 1', '41'), ('Platinum 1', '65'), ('Platinum 1', '75'), ('Platinum 1', '65'), ('Platinum 1', '55'), ('Platinum 1', '98'), ('Platinum 1', '69'), ('Platinum 1', '79'), ('Platinum 1', '62'), ('Platinum 1', '43'), ('Platinum 1', '0'), ('Platinum 1', '10'), ('Platinum 1', '0'), ('Platinum 1', '7'), ('Platinum 1', '67'), ('Platinum 1', '39'), ('Platinum 1', '10'), ('Platinum 1', '0'), ('Platinum 1', '8'), ('Platinum 1', '32'), ('Platinum 1', '42'), ('Platinum 1', '32'), ('Platinum 1', '14'), ('Platinum 2', '85'), ('Platinum 2', '69'), ('Platinum 2', '52'), ('Platinum 2', '8'), ('Platinum 3', '75'), ('Platinum 2', '0'), ('Platinum 2', '19'), ('Platinum 3', '75'), ('Platinum 2', '0'), ('Platinum 2', '7'), ('Platinum 3', '75'), ('Platinum 2', '0'), ('Platinum 2', '25'), ('Platinum 2', '48'), ('Platinum 2', '30'), ('Platinum 2', '67'), ('Platinum 2', '89'), ('Platinum 2', '44'), ('Platinum 2', '0'), ('Platinum 2', '16'), ('Platinum 2', '6'), ('Platinum 3', '75'), ('Platinum 3', '31'), ('Platinum 3', '41'), ('Platinum 4', '95'), ('Platinum 4', '47'), ('Platinum 4', '10'), ('Platinum 4', '46'), ('Platinum 4', '17'), ('Platinum 4', '27'), ('Platinum 4', '75'), ('Platinum 3', '0'), ('Platinum 3', '4'), ('Platinum 3', '25'), ('Platinum 3', '75'), ('Platinum 2', '0'), ('Platinum 2', '3'), ('Platinum 2', '54'), ('Platinum 2', '44'), ('Platinum 2', '0'), ('Platinum 2', '10'), ('Platinum 2', '20'), ('Platinum 2', '43'), ('Platinum 2', '24'), ('Platinum 2', '59'), ('Platinum 2', '49'), ('Platinum 2', '5'), ('Platinum 2', '25'), ('Platinum 2', '73'), ('Platinum 2', '63'), ('Platinum 2', '44'), ('Platinum 2', '24'), ('Platinum 2', '74'), ('Platinum 2', '43'), ('Platinum 2', '26'), ('Platinum 2', '36'), ('Platinum 2', '26'), ('Platinum 2', '16'), ('Platinum 3', '85'), ('Platinum 3', '75'), ('Platinum 2', '0'), ('Platinum 2', '3'), ('Platinum 2', '47'), ('Platinum 2', '79'), ('Platinum 2', '89'), ('Platinum 2', '71'), ('Platinum 2', '39'), ('Platinum 2', '20'), ('Platinum 2', '0'), ('Platinum 2', '7'), ('Platinum 2', '17'), ('Platinum 2', '27'), ('Platinum 2', '8'), ('Platinum 3', '75'), ('Platinum 2', '0'), ('Platinum 2', '5'), ('Platinum 3', '58'), ('Platinum 3', '41'), ('Platinum 3', '9'), ('Platinum 3', '30'), ('Platinum 4', '84'), ('Platinum 4', '52'), ('Platinum 4', '34'), ('Platinum 4', '44'), ('Platinum 4', '34'), ('Platinum 4', '2'), ('Gold 1', '70'), ('Gold 1', '33'), ('Gold 1', '10'), ('Gold 1', '0'), ('Gold 1', '24'), ('Gold 1', '34'), ('Gold 1', '10'), ('Gold 1', '0'), ('Gold 1', '2'), ('Gold 1', '12'), ('Gold 2', '79'), ('Gold 2', '99'), ('Gold 2', '79'), ('Gold 2', '69'), ('Gold 2', '34'), ('Gold 2', '67'), ('Gold 2', '98'), ('Gold 2', '75'), ('Gold 1', '0'), ('Gold 1', '10'), ('Gold 1', '0'), ('Gold 1', '1'), ('Gold 1', '32'), ('Gold 1', '63'), ('Gold 1', '53'), ('Gold 1', '43'), ('Gold 1', '86'), ('Gold 1', '43'), ('Gold 1', '0'), ('Gold 1', '8'), ('Gold 1', '39'), ('Gold 1', '49'), ('Gold 1', '8'), ('Gold 2', '50'), ('Gold 2', '26'), ('Gold 2', '44'), ('Gold 2', '54'), ('Gold 2', '44'), ('Gold 2', '0'), ('Gold 2', '4'), ('Gold 2', '22'), ('Gold 3', '76'), ('Gold 3', '31'), ('Gold 3', '41'), ('Gold 3', '14'), ('Gold 3', '4'), ('Gold 3', '22'), ('Gold 3', '64'), ('Gold 3', '54'), ('Gold 3', '6'), ('Gold 3', '23'), ('Gold 4', '95'), ('Gold 4', '85'), ('Gold 4', '95'), ('Gold 4', '66'), ('Gold 4', '0'), ('Gold 4', '5'), ('Gold 4', '33'), ('Gold 4', '49'), ('Gold 4', '19'), ('Gold 4', '36'), ('Gold 4', '4'), ('Gold 4', '21'), ('Silver 1', '67'), ('Silver 1', '56'), ('Silver 1', '0'), ('Silver 1', '21'), ('Silver 1', '55'), ('Silver 1', '90'), ('Silver 1', '25'), ('Silver 2', '56'), ('Silver 2', '66'), ('Silver 2', '76'), ('Silver 3', '65'), ('Silver 3', '75'), ('Silver 2', '0'), ('Silver 2', '3'), ('Silver 2', '13')]


ELO_MAP = {
    "Silver": 400,
    "Gold": 800,
    "Platinum": 1200,
    "Diamond": 1600,
}

def get_elo_from_rank(rank, lp):
    division, tier = rank.split(' ')
    return ELO_MAP[division] - int(tier) * 100 + int(lp)

normalized_ranks = [get_elo_from_rank(*rank) for rank in ranks[::-1]]

import matplotlib.pyplot as plt

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