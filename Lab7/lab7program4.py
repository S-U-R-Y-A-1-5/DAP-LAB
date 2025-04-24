def count_good_feedback(feedback):
    return feedback.count("was")
string = "The service was Good. Food was GOOD. Overall, a good experience."
print("Count of 'was':", count_good_feedback(string))
