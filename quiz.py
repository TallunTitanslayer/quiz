#           while True:
  #  d1a = input("Do you want to: \n A) House. B) Stable. [A/B]? : ")
  #  if d1a == "A":
   #     print("You approach the cottage.")
  #  elif d1a == "B":
   #     print("You approach the stables.")
 #   elif d1a == "Q":
  #      print("Done!")
  #      break
  #print('Question 1: what was the weakness of Perseus?')

#while True:
#        question_1 = input('was is: \n a) hubris. b) anger. c) love. d) none.[a/b/c/d]? :')
#if question_1 == 'd':
#    print('correct!')
#
#else:
#    print('wrong!')




#print('Welcome young demigod to my quiz to see how well you know your history on Greek mythology.') 
#name = ('what is your name? ')
#print('Type in the correct answer for each question')

#NUM_QUESTIONS_PER_QUIZ = 5
#QUESTIONS = {
 #   '1. What was the weakness of Perseus?': [
 #       'hubris', 'anger', 'love', 'none',
 #   ],

   # "2. Who was Perceus's father?": [
    #    'None of the above', 'Posidien', 'Ares', 'Zeus',
  #  ],

  #  '3. True or false: Is Hercules spelt correct?': [
  #      'True it is spelt like that',
 #       'False, it is spelt as Heracles, Hercules is Roman',
  #  ],
#
   # '4. Was Heracles born a god?': [
  #      'Yes, he was in the movie!',
   #     'no he was a demigod',
   #     'He was a demigod before becoming a god',
    #    'IDK',
    #],

   # "5. What was Heracles' weakness?": [
  #      'Hubris', 'Wrath', 'none', 'none of the above',
  #  ],
#
  #  '6. Who was Hippolytus?': [
  #      'He was a hunter of Artimis',
  #      'IDK',
  #      "He was one of Aphrodite's children",
   #     'none of the above',
   # ],

   # "7. Who was Hippolytus's parents?": [
   #     'Theseus and Hippolyta',
   ##     'Theseus and Antiope',
   #     'Hippolyta and Zeus',
    ##    'none of the above',
    #],

    #"8. Why was Theseus and Pirithous stuck in Hades?": [
    #    'Pirithous want Persephone, wife of Hades, as his wife',
    #    'Because Hades is evil',
    #    'because they died',
    #   'None of the above',
  #  ],

   #'9. Which relationship was the most stable?': [
     #   'Zeus and Hera', 
   #     'Hades and Persephone',
     #   "Ares and aphrodite",
       # 'other'
  #  ],
#
    #'10.what did you learn': [
    #    'Most gods/goddesses suck',
    #    'Hercules the movie was a lie',
    #    'a lot of things',
   #     'nothing',
   # ],
#}

#num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
#questions = random.sample

#for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
#    print(f"\nQuestion {num}:")
#   print(f'{question}?')
#    correct_answer = alternatives[3]
#    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
#    for label, alternative in labeled_alternatives.items():
#        print(f" {label} {alternative}")

 #   answer_label = input('\nChoice? ')
 #   answer = labeled_alternatives.get(answer_label)
 #   if answer == correct_answer:
    #    print("correct!")
   # else:
    #    print(f"The answer is {correct_answer!r}, not {answer!r}")
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

    "2. Who was Perceus's father ": [
       'None of the above', 'Posidien', 'Ares', 'Zeus',
],

    '3. True or false: Is Hercules spelt correct ': [
      'True it is spelt like that',
      'Does it matter?',
      "I don't know",
      'False, it is spelt as Heracles, Hercules is Roman',
],

    '4. Was Heracles born a god ': [
        'Yes, he was in the movie!',
        'no he was a demigod',
        'IDK',
        'He was a demigod before becoming a god',
],

    "5. What was Heracles' weakness ": [
        'Hubris', 'not stated here', 'none', 'wrath',
],

    '6. Who was Hippolytus ': [
       'Not stated here',
       'IDK',
       "He was one of Aphrodite's children",
       'He was a hunter of Artimis',
],

    "7. Who was Hippolytus's parents ": [
        'Not known',
        'Theseus and Antiope',
        'Hippolyta and Zeus',
        'Theseus and Hippolyta',
],

    "8. Why was Theseus and Pirithous stuck in Hades ": [
        'not known',
        'Because Hades is evil',
        'because they died',
        'Pirithous wanted Persephone, wife of Hades, as his wife',
 ],

    "9. Which relationship was the most stable ": [
        'Zeus and Hera',
        "I don't know, all of the relationships that I know of aren't the most stable.",
        "Ares and aphrodite",
        'Hades and Persephone',
 ],

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
   

