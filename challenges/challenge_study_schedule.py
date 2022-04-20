def study_schedule(permanence_period, target_time):
    try:
        count = 0.
        for permanence in permanence_period:
            if permanence[0] <= target_time <= permanence[1]:
                count += 1
        return count
    except Exception:
        return None
