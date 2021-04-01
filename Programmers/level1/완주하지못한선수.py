def solution(participant, completion):
    for person in participant:
        if person in completion:
            completion.remove(person)
        else:
            answer = person
    return answer
