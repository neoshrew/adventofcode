max_distance = None
total_time = 2503


class Reindeer(object):
    def __init__(self, speed, stamina, rest):
        self.speed = speed
        self.stamina = stamina
        self.rest = rest
        self.cycle = 'moving'
        self.cycle_left = stamina
        self.total_distance = 0
        self.points = 0

    def tick(self):
        if self.cycle == 'moving':
            self.total_distance += self.speed

        self.cycle_left -= 1

        if self.cycle_left == 0:
            if self.cycle == 'moving':
                self.cycle = 'resting'
                self.cycle_left = self.rest
            else:
                self.cycle = 'moving'
                self.cycle_left = self.stamina


with open('input.txt') as fandle:
    all_reindeer = []
    for line in fandle:
        parts = line.split()
        all_reindeer.append(Reindeer(int(parts[3]), int(parts[6]), int(parts[13])))


for i in range(total_time):
    for reindeer in all_reindeer:
        reindeer.tick()

    max_distance = max(r.total_distance for r in all_reindeer)
    for r in all_reindeer:
        if r.total_distance == max_distance:
            r.points += 1

print max(r.points for r in all_reindeer)