# quiz
    import random  
    from string import ascii_lowercase
 


    print('Welcome young demigod to my quiz to see how well you know your history on Greek mythology.') 
    name = ('what is your name? ')
    print('Type in the correct answer for each question')

    NUM_QUESTIONS_PER_QUIZ = 5
    QUESTIONS = {

    '1. What was the weakness of Perseus?': [
        'hubris', 'anger', 'love', 'none',
    ],

    "2. Who was Perceus's father?": [
        'None of the above', 'Posidien', 'Ares', 'Zeus',
    ],

    '3. True or false: Is Hercules spelt correct?': [
        'True it is spelt like that',
        'Does it matter?',
        "I don't know",
        'False, it is spelt as Heracles, Hercules is Roman',
    ],

    '4. Was Heracles born a god?': [
        'Yes, he was in the movie!',
        'no he was a demigod',
        'IDK',
        'He was a demigod before becoming a god',
    ],

    "5. What was Heracles' weakness?": [
        'Hubris', 'not stated here', 'none', 'wrath',
    ],

    '6. Who was Hippolytus?': [
        'Not stated here',
        'IDK',
        "He was one of Aphrodite's children",
        'He was a hunter of Artimis',
    ],

    "7. Who was Hippolytus's parents?": [
        'Not known',
        'Theseus and Antiope',
        'Hippolyta and Zeus',
        'Theseus and Hippolyta',
    ],

    "8. Why was Theseus and Pirithous stuck in Hades?": [
        'not known',
        'Because Hades is evil',
        'because they died',
        'Pirithous wanted Persephone, wife of Hades, as his wife',
    ],

    '9. Which relationship was the most stable?': [
        'Zeus and Hera', 
        "I don't know, all of the relationships that I know of aren't the most stable.",
        "Ares and aphrodite",
        'Hades and Persephone',
    ],
    print('and finally')
    "10. Who was Zeus's least favored child ":  [
        'Hermes',
        'Athena',
        'Dionysus',
        'Ares',
    ],
    }
    num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
    questions = random.sample


    num_correct = 0
    for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f'{question}?')
    correct_answer = alternatives[3]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f" {label} {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
    print(f"Please answer one of {', '.join(labeled_alternatives)}")
    answer = labeled_alternatives[answer_label]

    answer_label = input('\nChoice? ')
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        print("correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0
