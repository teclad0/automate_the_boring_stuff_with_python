#! /usr/bin/python3
# randomQuizGeneratorpy - Creates quizzes with questions and answers in 
#                           random order, along with the answer key

import random 

capitals = { 'Amapá' : 'Macapá',
'Amazonas'  : 'Manaus',
'Pará'  : 'Belém',
'Rondônia'  : 'Porto Velho',
'Roraima' : 'Boa Vista',
'Tocantins'  : 'Palmas',
'Alagoas'  : 'Maceió',
'Bahia' : 'Salvador',
'Ceará'  : 'Fortaleza',
'Maranhão'  : 'São Luís',
'Paraíba'  : 'João Pessoa',
'Pernambuco'  : 'Recife',
'Piauí'  : 'Teresina',
'Rio Grande do Norte'  : 'Natal',
'Sergipe'  : 'Aracaju',
'Goiás'  : 'Goiânia',
'Mato Grosso'  : 'Cuiabá',
'Mato Grosso do Sul' :'Campo Grande',
'Distrito Federal' : 'Brasília',
'Espírito Santo' : 'Vitória',
'Minas Gerais' : 'Belo Horizonte',
'São Paulo'  : 'São Paulo',
'Rio de Janeiro'  : 'Rio de Janeiro',
'Paraná'  : 'Curitiba',
'Rio Grande do Sul'  : 'Porto Alegre',
'Santa Catarina'  : 'Florianópolis'}

# Generate 27 quiz files.
for quizNum in range(10):
    # Create the quiz and answer key files
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')
    # Write out the header for the quiz
    quizFile.write(('' * 20) + f'State Capitals Quiz (Form{quizNum + 1}) - BR')
    quizFile.write('\n\n')
    # Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)
    # Loop through all 27 states, making a question for each
    for questionNum in range(25):
        # Get right and wrong answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answersOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answersOptions)
        # Write the question and the answer options to the quiz file
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"     {'ABCD'[i]}. {answersOptions[i]}\n")
            quizFile.write('\n')
            # Write the answer key to a file
        answerKeyFile.write(f"{questionNum + 1}.   {'ABCD'[answersOptions.index(correctAnswer)]}\n")
    quizFile.close()
    answerKeyFile.close()

