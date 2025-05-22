def acm_team(topic):
    max_topics = 0
    team_count = 0
    for i in range(len(topic)):
        for j in range(i + 1, len(topic)):
            knowledge = 0
            for k in range(len(topic[0])):
                if topic[i][k] == '1' or topic[j][k] == '1':
                    knowledge += 1
            if knowledge > max_topics:
                max_topics = knowledge
                team_count = 1
            elif knowledge == max_topics:
                team_count += 1
    return [max_topics, team_count]
print(acm_team([]))