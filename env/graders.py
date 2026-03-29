def grade_task_1(env):
    return sum(1 for t in env.tickets if t.category) / len(env.tickets)

def grade_task_2(env):
    return sum(1 for t in env.tickets if t.resolved) / len(env.tickets)

def grade_task_3(env):
    score = 0
    for t in env.tickets:
        if t.resolved:
            score += 0.5
        if t.priority == "high" and t.resolved:
            score += 0.5
    return min(score / len(env.tickets), 1.0)