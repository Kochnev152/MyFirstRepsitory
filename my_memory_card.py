#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *
from random import shuffle
from random import choice

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions = [
    Question('Какой национальности не существует?','Энцы','Чулымцы','Смурфы','Алеуты'),
    Question('Государственный язык Аргентины?','Испанский','Аргентинский','Английский','Бразильский'),
    Question('Что будет, если ты станешь программистом?','Всё вместе','Лень','Прогресс','Опыт'),
    Question('Какого цвета крайнее правое кольцо в олимпийской символике?','Красное','Синее','Желтое','Зеленое'),
    Question('Какую страну не пересекает экватор?','Панама','Бразилия','Индонезия','Кения'),
    Question('Под каким названием известна единица с последующими ста нулями?','Гугол','Мегатрон','Гигабит','Наномоль'),
    Question('Какой химический элемент составляет более половины массы тела человека?','Кислород','Углерод','Кальций','Железо'),
    Question('Какую часть тела также называют «атлант»?','Шейный позвонок','Головной мозг','Шестая пара ребер','Часть плеча'),
    Question('Сколько кубиков в кубике Рубика?','26','22','24','28')
]

def cur_question():
    global question_number
    if question_number == 0:
        question_number = randint(1,8)
    elif question_number == 1:
        question_number = (choice([i for i in range(0,8) if i not in [1]]))
    elif question_number == 2:
        question_number = (choice([i for i in range(0,8) if i not in [2]]))
    elif question_number == 3:
        question_number = (choice([i for i in range(0,8) if i not in [3]]))
    elif question_number == 4:
        question_number = (choice([i for i in range(0,8) if i not in [4]]))
    elif question_number == 5:
        question_number = (choice([i for i in range(0,8) if i not in [5]]))
    elif question_number == 6:
        question_number = (choice([i for i in range(0,8) if i not in [6]]))
    elif question_number == 7:
        question_number = (choice([i for i in range(0,8) if i not in [7]]))
    elif question_number == 8:
        question_number = randint(0,7)


def next_question():
    global question_number
    cur_question()
    if question_number == 1:
        question.setText(questions[question_number].question)
        btn_answer1.setText(questions[question_number].wrong1)
        btn_answer2.setText(questions[question_number].wrong2)
        btn_answer3.setText(questions[question_number].right_answer)
        btn_answer4.setText(questions[question_number].wrong3)
    elif question_number == 2:
        question.setText(questions[question_number].question)
        btn_answer1.setText(questions[question_number].wrong1)
        btn_answer2.setText(questions[question_number].wrong2)
        btn_answer3.setText(questions[question_number].wrong3)
        btn_answer4.setText(questions[question_number].right_answer)
    elif question_number == 3:
        question.setText(questions[question_number].question)
        btn_answer1.setText(questions[question_number].wrong1)
        btn_answer2.setText(questions[question_number].right_answer)
        btn_answer3.setText(questions[question_number].wrong2)
        btn_answer4.setText(questions[question_number].wrong3)
    elif question_number == 4:
        question.setText(questions[question_number].question)
        btn_answer1.setText(questions[question_number].right_answer)
        btn_answer2.setText(questions[question_number].wrong1)
        btn_answer3.setText(questions[question_number].wrong2)
        btn_answer4.setText(questions[question_number].wrong3)
    elif question_number == 5:
        question.setText(questions[question_number].question)
        btn_answer1.setText(questions[question_number].wrong1)
        btn_answer2.setText(questions[question_number].right_answer)
        btn_answer3.setText(questions[question_number].wrong2)
        btn_answer4.setText(questions[question_number].wrong3)
    elif question_number == 6:
        question.setText(questions[question_number].question)
        btn_answer1.setText(questions[question_number].wrong1)
        btn_answer2.setText(questions[question_number].wrong2)
        btn_answer3.setText(questions[question_number].right_answer)
        btn_answer4.setText(questions[question_number].wrong3)
    elif question_number == 7:
        question.setText(questions[question_number].question)
        btn_answer1.setText(questions[question_number].wrong1)
        btn_answer2.setText(questions[question_number].wrong2)
        btn_answer3.setText(questions[question_number].wrong3)
        btn_answer4.setText(questions[question_number].right_answer)
    elif question_number == 8:
        question.setText(questions[question_number].question)
        btn_answer1.setText(questions[question_number].wrong1)
        btn_answer2.setText(questions[question_number].right_answer)
        btn_answer3.setText(questions[question_number].wrong2)
        btn_answer4.setText(questions[question_number].wrong3)
    elif question_number == 0:
        question.setText(questions[question_number].question)
        btn_answer1.setText(questions[question_number].right_answer)
        btn_answer2.setText(questions[question_number].wrong1)
        btn_answer3.setText(questions[question_number].wrong2)
        btn_answer4.setText(questions[question_number].wrong3)
        print('Ты прошёл все вопросы!')

    lb_Correct1.setText(questions[question_number].right_answer)



def show_answer():
    global totalq
    global totalrightans
    if button_answer.text() == 'Ответить':
        button_answer.setText('Следующий вопрос')
        RadioGroupBox.hide()
        AnsGroupBox.show()
        if question.text() == 'Какой национальности не существует?':
            if btn_answer1.isChecked():
                lb_Question.setText('Вы ответили правильно!')
                totalrightans += 1
            else:
                lb_Question.setText('Вы ответили неправильно!')
        elif question.text() == 'Государственный язык Аргентины?':
            if btn_answer3.isChecked():
                lb_Question.setText('Вы ответили правильно!')
                totalrightans += 1
            else:
                lb_Question.setText('Вы ответили неправильно!')
        elif question.text() == 'Что будет, если ты станешь программистом?':
            if btn_answer4.isChecked():
                lb_Question.setText('Вы ответили правильно!')
                totalrightans += 1
            else:
                lb_Question.setText('Вы ответили неправильно!')
        elif question.text() == 'Какое число я загадал?':
            if btn_answer2.isChecked():
                lb_Question.setText('Вы ответили правильно!')
                totalrightans += 1
            else:
                lb_Question.setText('Вы ответили неправильно!')
        elif question.text() == 'Какой напиток самый лучший?':
            if btn_answer1.isChecked():
                lb_Question.setText('Вы ответили правильно!')
                totalrightans += 1
            else:
                lb_Question.setText('Вы ответили неправильно!')  
        elif question.text() == 'Под каким названием известна единица с последующими ста нулями?': 
            if btn_answer2.isChecked():
                lb_Question.setText('Вы ответили правильно!')
                totalrightans += 1
            else:
                lb_Question.setText('Вы ответили неправильно!') 
        elif question.text() == 'Какой химический элемент составляет более половины массы тела человека?': 
            if btn_answer3.isChecked():
                lb_Question.setText('Вы ответили правильно!')
                totalrightans += 1
            else:
                lb_Question.setText('Вы ответили неправильно!')
        elif question.text() == 'Какую часть тела также называют «атлант»?': 
            if btn_answer4.isChecked():
                lb_Question.setText('Вы ответили правильно!')
                totalrightans += 1
            else:
                lb_Question.setText('Вы ответили неправильно!')
        elif question.text() == 'Сколько кубиков в кубике Рубика?': 
            if btn_answer2.isChecked():
                lb_Question.setText('Вы ответили правильно!')
                totalrightans += 1
            else:
                lb_Question.setText('Вы ответили неправильно!')
        
    else:
        button_answer.setText('Ответить')
        totalq += 1
        print('Всего вопросов:', totalq)
        print('правильных ответов:', totalrightans)
        print('Статистика:', totalrightans/totalq *100,'%')
        RadioGroupBox.show()
        AnsGroupBox.hide()
        RadioGroup.setExclusive(False)
        btn_answer1.setChecked(False)
        btn_answer2.setChecked(False)
        btn_answer3.setChecked(False)
        btn_answer4.setChecked(False)
        next_question()
        
  
def start_test():
    if button_answer.text == 'Ответить':
        show_result()
    else:
        show_question()
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.setLayout(layout_res)


#создание приложения и главного окна
question_number = 0
totalq = 0
totalrightans = 0
app = QApplication([])
main_win = QWidget()
main_win.resize(400,200)
main_win.setWindowTitle('Memory Card')
question = QLabel(questions[question_number].question)


RadioGroupBox = QGroupBox("Варианты ответов")
btn_answer1 = QRadioButton(questions[question_number].right_answer)
btn_answer2 = QRadioButton(questions[question_number].wrong1)
btn_answer3 = QRadioButton(questions[question_number].wrong2)
btn_answer4 = QRadioButton(questions[question_number].wrong3)
button_answer = QPushButton('Ответить')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(btn_answer1) # два ответа в первый столбец
layout_ans2.addWidget(btn_answer2)
layout_ans3.addWidget(btn_answer3) # два ответа во второй столбец
layout_ans3.addWidget(btn_answer4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox("Результат теста")
lb_Question = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('Правильный ответ:') 
lb_Correct1 = QLabel(questions[question_number].right_answer) # здесь будет написан текст правильного ответа
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Question, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
layout_res.addWidget(lb_Correct1, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()
layout_ans1.addWidget(question, alignment = Qt.AlignCenter)


layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"

layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:

# Размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
layout_line3.addStretch(1)
layout_line3.addWidget(button_answer, stretch=5) # кнопка должна быть большой
layout_line3.addStretch(1)

button_answer.clicked.connect(show_answer)

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

# Теперь созданные строки разместим друг под другой:

layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addLayout(layout_line3)

layout_card.setSpacing(5) # пробелы между содержимым
main_win.setLayout(layout_card)
main_win.show()
app.exec_()