def acm_team(topic):
    max_topics = 0
    team_count = 0
    
    for i in range(len(topic)):
        for j in range(i+1, len(topic)):
           
            combined = bin(int(topic[i], 2) | int(topic[j], 2))
            topics = combined.count('1')  
            
            if topics > max_topics:
                max_topics = topics
                team_count = 1
            elif topics == max_topics:
                team_count += 1
                
    return [max_topics, team_count]