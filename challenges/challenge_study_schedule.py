def study_schedule(permanence_period, target_time):
    count = 0

    for index in permanence_period:
        try:
            if index[0] <= target_time <= index[1]:
                count += 1
        except TypeError:
            return None

    return count
