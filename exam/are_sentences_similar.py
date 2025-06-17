def are_sentences_similar(sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]) -> bool:
    if len(sentence1) != len(sentence2):
        return False

    similar = set()
    for pair in similarPairs:
        similar.add((pair[0], pair[1]))
        similar.add((pair[1], pair[0]))  
 
    for word1, word2 in zip(sentence1, sentence2):
        if word1 == word2:  
            continue
        if (word1, word2) not in similar: 
            return False
    
    return True