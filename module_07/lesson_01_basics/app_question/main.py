from Classes.ClassQuestion import Question

if __name__ == '__main__':
    questions = [
        {'question': 'My name __ Vova', 'answer': 'is'},
        {'question': 'I live __ Moscow', 'answer': 'in'},
    ]
    all_questions_obj = []

    for question in questions:
        all_questions_obj.append(Question(question['question'], question['answer']))

    for question in all_questions_obj:
        print(question.question)
        user_answer = input('Введите ваш ответ: ').strip().lower()
        if question.is_correct(user_answer):
            print(f'{user_answer} - это верно!')
        else:
            print(f'{user_answer} это неверно, правильный ответ {question.correct_answer}')
