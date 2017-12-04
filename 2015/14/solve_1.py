max_distance = None
total_time = 2503


with open('input.txt') as fandle:
    all_reindeer = []
    for line in fandle:
        parts = line.split()
        speed, stamina, rest = int(parts[3]), int(parts[6]), int(parts[13])

        cycle_time = stamina+rest
        completed_cycles = total_time // cycle_time
        partial_time = total_time % cycle_time
        partial_time_moving = min(partial_time, stamina)
        partial_movement = partial_time_moving * speed
        total_distance = (completed_cycles * speed * stamina) + partial_movement
        max_distance = max(max_distance, total_distance)

print max_distance