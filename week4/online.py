import random

#this is allowing us to define the target phrase and all possible characters that may be used
def main():
    goal = "methinks it is like a weasel"
    characters = "abcdefghijklmnopqrstuvwxyz "
    generations = 0
    current_sequence = generate_random_string(goal, characters)
    print("Generation:",generations)
    print(current_sequence)
    while current_sequence != goal:
        current_sequence = get_mutatated_sequence(current_sequence,goal,characters)
        generations += 1
        print("Generation: ",generations)
        print(current_sequence)


#we need to create a random string of characters that will act as our base generations
def generate_random_string(goal,characters):
    sequence = ""
    for i in range(len(goal)):
        sequence += characters[random.randint(0, len(characters)-1)]
    return sequence

def get_mutatated_sequence(sequence, goal, characters):
    sequence_list = get_sequence_mutations(sequence,characters)
    best_seq = sequence_list[0]
    best_similarity_factor = get_score(best_seq,goal)
    for seq in sequence_list:
        similarity_factor = get_score(seq,goal)
        if similarity_factor > best_similarity_factor:
            best_similarity_factor = similarity_factor
            best_seq = seq
    return best_seq

def get_sequence_mutations(sequence,characters):
    sequence_list = []
    for i in range(100):
        sequence_list.append(mutate_sequence(sequence,characters))
    return sequence_list

def mutate_sequence(sequence, characters):
    result = ""
    for i in range(len(sequence)):
        if random.randint(0,100) <= 5:
            result += characters[random.randint(0,len(characters)-1)]
        else:
            result += sequence[i]
    return result

def get_score(sequence,goal):
    score = 0
    for i in range(len(goal)):
        if goal[i] == sequence[i]:
            score += 1
    return score

main()
