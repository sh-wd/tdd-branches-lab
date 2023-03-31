def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    sorted_scores = order_highest_to_lowest(scores)
    return sorted_scores[0:3]


def order_highest_to_lowest(scores):
    sorted_scores = sorted(scores, reverse=True)
    return sorted_scores