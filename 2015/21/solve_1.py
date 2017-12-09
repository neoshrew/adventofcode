from itertools import combinations
from math import ceil

with open('input.txt') as fandle:
    boss_stats = {
        k.lower().replace(' ', '_'): int(v)
        for k, v in (
            line.strip().split(': ')
            for line in fandle
        )
    }

def will_win(A, B):
    # Steps to kill is ceil(hit_points/net_damage)
    # net_damage is max(damage-opponent_armour, 1)
    # A goes first so a wins a tie
    def steps(_a, _b):
        net_damage = max(_a['damage']-_b['armor'], 1)
        n_steps = ceil(float(_b['hit_points'])/float(net_damage))
        return n_steps

    return steps(A, B) <= steps(B, A)


def _dmg(n):
    def _(x): x['damage'] += n
    return _
def _rmr(n):
    def _(x): x['armor'] += n
    return _
_nun = lambda x: x

weapons = (
    ('Dagger',     8,  _dmg(4)),
    ('Shortsword', 10, _dmg(5)),
    ('Warhammer',  25, _dmg(6)),
    ('Longsword',  40, _dmg(7)),
    ('Greataxe',   74, _dmg(8))
)
armors = (
    ('<none>',     0,   _nun),
    ('Leather',    13,  _rmr(1)),
    ('Chainmail',  31,  _rmr(2)),
    ('Splintmail', 53,  _rmr(3)),
    ('Bandedmail', 75,  _rmr(4)),
    ('Platemail',  102, _rmr(5)),
)
ring_pairs = tuple(combinations((
    ('<L None>',   0,   _nun),
    ('<R None>',   0,   _nun),
    ('Damage +1',  25,  _dmg(1)),
    ('Damage +2',  50,  _dmg(2)),
    ('Damage +3',  100, _dmg(3)),
    ('Defense +1', 20,  _rmr(1)),
    ('Defense +2', 40,  _rmr(2)),
    ('Defense +3', 80,  _rmr(3)),
), 2))


player_base = {'hit_points': 100, 'damage': 0, 'armor': 0}

possibilities = []
for weapon in weapons:
    for armor in armors:
        for ring_1, ring_2 in ring_pairs:
            x = player_base.copy()
            weapon[2](x)
            armor[2](x)
            ring_1[2](x)
            ring_2[2](x)

            if will_win(x, boss_stats):
                cost = weapon[1] + armor[1] + ring_1[1] + ring_2[1]
                possibilities.append(cost)

print min(possibilities)

