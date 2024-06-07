import random

capitals = {
    'Alabama': 'Montgomery',    'Alaska': 'Juneau',    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New York': 'Albany', 'North Carolina': 'Raleigh',  'New Mexico': 'Santa Fe',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiz in range(5):
    quiz_file = open('./quiz/capital_quiz%s.txt' % (quiz + 1), 'w')
    quiz_answer = open('./quiz/capital_quiz_answers%s.txt' % (quiz + 1), 'w')

    quiz_file.write('Name:\n\nDate:\n\nLevel:\n\n')
    quiz_file.write((' ' * 20) + 'State Capital Quiz (Form %s)' % (quiz + 1))
    quiz_file.write('\n\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for question in range(20):
        correct_answer = capitals[states[question]]
        wrong_answer = list(capitals.values())
        del wrong_answer[wrong_answer.index(correct_answer)]
        wrong_answer = random.sample(wrong_answer, 3)
        answer_option = wrong_answer + [correct_answer]
        random.shuffle(answer_option)

        quiz_file.write('%s What is the capital of %s?\n\n' % (question + 1, states[question]))
        for i in range(4):
            quiz_file.write('   %s. %s\n' % ('ABCD'[i], answer_option[i]))
            quiz_file.write('\n')
        quiz_answer.write('%s. %s\n' % (question + 1, 'ABCD'[answer_option.index(correct_answer)]))
    quiz_file.close()
    quiz_answer.close()
