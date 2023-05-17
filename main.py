from tkinter import *

questions1 = ['五_______照片 （5 фотографий）', '那_______电视机 （тот телевизор)', '三十七_______词典 （37 словарей）',
                   '十三_______猫 （13 котов）', '那_______商店 （этот магазин）']

options1 = [['本', '张', '台', '张'], ['块', '本', '台', '台'], ['条', '张', '本', '本'], ['条', '只', '把', '只'],
            ['家', '台', ' 块', '家']]

questions2 = ['一_______山（1 гора）', '这_______家具（эта мебель）', '那_______电影（тот фильм）',
              '一_______铅笔（один карандаш）', '两_______先生（два господина）']

options2 = [['座', '个', '些', '座'], ['支', '双', '件', '件'], ['个', '部', '位', '部'],
            ['个', '支', '座', '支'], ['个', '双', '位', '位']]

questions3 = [['她拥有两家商店。 里面有四只猫、两条狗和一只乌龟。', '她拥有两家商店。 里面有四只猫、两条狗和一只乌龟。'],
              ['我在图书馆拿了四本书、两张杂志和五张名人照片。', '我在图书馆拿了四本书、两本杂志和五张名人照片。'],
              ['礼堂里有七张桌子、十四把椅子和1块黑板。', '礼堂里有七张桌子、十四把椅子和1块黑板。'],
              ['这条街上有三座楼和一座大桥，前面有两条河流。', '这条街上有三座楼和一座大桥，前面有两条河流。'],
              [' 五个学生在一把电视上观看了那个电影，并吃了几块蛋糕。', '五个学生在一台电视上观看了那部电影，并吃了几块蛋糕。']]


def main_window():
    window = Toplevel()
    window.geometry("500x350")
    window.configure(background='#FFE4C4')

    for c1 in range(2): window.columnconfigure(index=c1, weight=1)
    for r1 in range(3): window.rowconfigure(index=r1, weight=1)

    btn1 = Button(window, text="规则 一", font='Times 36', bg='#87CEFA', command=rule_one)
    btn1.grid(row=0, column=0)

    btn2 = Button(window, text="规则 二", font='Times 36', bg='#87CEFA', command=rule_two)
    btn2.grid(row=0, column=1)

    btn3 = Button(window, text="练习 一", font='Times 30', bg='#DA70D6', command=ex1)
    btn3.grid(row=1, column=0)

    btn4 = Button(window, text="练习 二", font='Times 30', bg='#DA70D6', command=ex2)
    btn4.grid(row=1, column=1)

    btn5 = Button(window, text="练习 三", font='Times 35', width=20, height=1, bg='#CD5C5C', command=ex3)
    # columnspan=2 - растягиваем на два столбца
    btn5.grid(row=2, column=0, columnspan=2)


def rule_one():
    window = Toplevel()
    window.geometry("712x400")
    window.image = PhotoImage(file='rule1.png')
    img = PhotoImage(file='rule1.png')
    label = Label(window)
    label.image = img
    label['image'] = label.image
    label.place(x=0, y=0)


def rule_two():
    window = Toplevel()
    window.geometry("455x390")
    window.image = PhotoImage(file='rule2.png')
    img = PhotoImage(file='rule2.png')
    label = Label(window)
    label.image = img
    label['image'] = label.image
    label.place(x=0, y=0)


def rule_three():
    window = Toplevel()
    window.geometry("1250x700")
    window.image = PhotoImage(file='rule3.png')
    img = PhotoImage(file='rule3.png')
    label = Label(window)
    label.image = img
    label['image'] = label.image
    label.place(x=0, y=0)



index1 = 0
correct1 = 0

index2 = 0
correct2 = 0

index3 = 0
correct3 = 0


def ex1():
    window = Toplevel()
    window.geometry("505x375")
    window.configure(background='#DDA0DD')
    frame = Frame(window, padx=10, pady=10, bg='#DDA0DD')
    ques_label = Label(frame, height=8, width=30, bg='grey', fg='#fff', font=('Veranda', 20), wraplength=500)
    ques_label['text'] = '请选择正确的答案'
    button_start = Button(frame, text='Начать', bg='#BA55D3', font=('Veranda', 20), command=ex_one, border='10')
    ques_label.grid(row=0, column=0)
    button_start.grid(row=1, column=0, pady=22)
    frame.pack(fill='both')


def ex2():
    window = Toplevel()
    window.geometry("505x375")
    window.configure(background='#DDA0DD')
    frame = Frame(window, padx=10, pady=10, bg='#DDA0DD')
    ques_label = Label(frame, height=8, width=30, bg='grey', fg='#fff', font=('Veranda', 20), wraplength=500)
    ques_label['text'] = '请选择正确的答案'
    button_start = Button(frame, text='Начать', bg='#BA55D3', font=('Veranda', 20), command=ex_two, border='10')
    ques_label.grid(row=0, column=0)
    button_start.grid(row=1, column=0, pady=22)
    frame.pack(fill='both')


def ex3():
    window = Toplevel()
    window.geometry("505x375")
    window.configure(background='#FA8072')
    frame = Frame(window, padx=10, pady=10, bg='#FA8072')
    ques_label = Label(frame, height=8, width=30, bg='#B22222', fg='#fff', font=('Veranda', 20), wraplength=500)
    ques_label['text'] = '对/不对'
    button_start = Button(frame, text='Начать', bg='#BA55D3', font=('Veranda', 20), command=ex_three, border='10')
    ques_label.grid(row=0, column=0)
    button_start.grid(row=1, column=0, pady=22)
    frame.pack(fill='both')


def ex_one():
    window = Toplevel()
    window.geometry("505x375")
    frame = Frame(window, padx=10, pady=10, bg='#DDA0DD')
    ques_label = Label(frame, height=5, width=30, bg='grey', fg='#fff', font=('Veranda', 20), wraplength=500)

    v1 = StringVar(frame)
    v2 = StringVar(frame)
    v3 = StringVar(frame)

    option1 = Radiobutton(frame, bg='#DDA0DD', variable=v1, font=('Veranda', 20), command=lambda: check_answer(option1))
    option2 = Radiobutton(frame, bg='#DDA0DD', variable=v2, font=('Veranda', 20), command=lambda: check_answer(option2))
    option3 = Radiobutton(frame, bg='#DDA0DD', variable=v3, font=('Veranda', 20), command=lambda: check_answer(option3))

    button_next = Button(frame, text='Далее', bg='#BA55D3', font=('Veranda', 20), command=lambda: next_quest())
    button_rule = Button(frame, text='Правило', bg='#BA55D3', font=('Veranda', 20), command=lambda: rule_one())

    frame.pack(fill='both')
    ques_label.grid(row=0, column=0, columnspan=2)

    option1.grid(sticky='W', row=1, column=0)
    option2.grid(sticky='W', row=2, column=0)
    option3.grid(sticky='W', row=3, column=0)

    button_next.grid(row=6, column=0)
    button_rule.grid(row=6, column=1)

    def disable_buttons(state):
        option1['state'] = state
        option2['state'] = state
        option3['state'] = state

    def check_answer(radio):
        global correct1, index1

        if radio['text'] == options1[index1][3]:
            correct1 +=1
            ques_label['bg'] = 'green'
            ques_label['text'] = 'Верно!'
        else:
            ques_label['bg'] = 'red'
            ques_label['text'] = f'Ошибка. Верный вариант: {options1[index1][3]}'
        index1 +=1
        disable_buttons('disable')

    def next_quest():
        button_rule.configure(state=DISABLED)
        global index1, correct1

        if button_next['text'] == 'Начать заново':
            correct1 = 0
            index1 = 0
            ques_label['bg'] = 'grey'
            button_next['text'] = 'Далее'

        if index1 == len(options1):
            button_rule.configure(state='normal')
            button_next['text'] = 'Начать заново'
            if correct1 > 3:
                ques_label['text'] = str(correct1) + '/' + str(len(options1)) + '\n' + 'Вы молодец!'
                ques_label['bg'] = 'green'
            else:
                ques_label['text'] = str(correct1) + '/' + str(len(options1)) + '\n' + 'Мы только учимся, вернитесь к правилу и попробуйте еще!'
                ques_label['bg'] = 'red'
        else:
            ques_label['text'] = questions1[index1]
            ques_label['bg'] = 'grey'

            disable_buttons('normal')
            opts = options1[index1]
            option1['text'] = opts[0]
            option2['text'] = opts[1]
            option3['text'] = opts[2]
            v1.set(opts[0])
            v2.set(opts[1])
            v3.set(opts[2])

            if index1 == len(options1) - 1:
                button_next['text'] = 'Проверить результаты'

    next_quest()


def ex_two():
    window = Toplevel()
    window.geometry("505x375")
    frame = Frame(window, padx=10, pady=10, bg='#DDA0DD')
    ques_label = Label(frame, height=5, width=30, bg='grey', fg='#fff', font=('Veranda', 20), wraplength=500)

    v1 = StringVar(frame)
    v2 = StringVar(frame)
    v3 = StringVar(frame)

    option1 = Radiobutton(frame, bg='#DDA0DD', variable=v1, font=('Veranda', 20), command=lambda: check_answer(option1))
    option2 = Radiobutton(frame, bg='#DDA0DD', variable=v2, font=('Veranda', 20), command=lambda: check_answer(option2))
    option3 = Radiobutton(frame, bg='#DDA0DD', variable=v3, font=('Veranda', 20), command=lambda: check_answer(option3))

    button_next = Button(frame, text='Далее', bg='#BA55D3', font=('Veranda', 20), command=lambda: next_quest())
    button_rule = Button(frame, text='Правило', bg='#BA55D3', font=('Veranda', 20), command=lambda: rule_two())

    frame.pack(fill='both')
    ques_label.grid(row=0, column=0, columnspan=2)

    option1.grid(sticky='W', row=1, column=0)
    option2.grid(sticky='W', row=2, column=0)
    option3.grid(sticky='W', row=3, column=0)

    button_next.grid(row=6, column=0)
    button_rule.grid(row=6, column=1)

    def disable_buttons(state):
        option1['state'] = state
        option2['state'] = state
        option3['state'] = state

    def check_answer(radio):
        global correct2, index2

        if radio['text'] == options2[index2][3]:
            correct2 +=1
            ques_label['bg'] = 'green'
            ques_label['text'] = 'Верно!'
        else:
            ques_label['bg'] = 'red'
            ques_label['text'] = f'Ошибка. Верный вариант: {options2[index2][3]}'

        index2 +=1
        disable_buttons('disable')

    def next_quest():
        button_rule.configure(state=DISABLED)
        global index2, correct2

        if button_next['text'] == 'Начать заново':
            correct2 = 0
            index2 = 0
            ques_label['bg'] = 'grey'
            button_next['text'] = 'Далее'

        if index2 == len(options2):
            button_rule.configure(state='normal')
            button_next['text'] = 'Начать заново'
            if correct2 > 3:
                ques_label['text'] = str(correct2) + '/' + str(len(options2)) + '\n' + 'Вы молодец!'
                ques_label['bg'] = 'green'
            else:
                ques_label['text'] = str(correct2) + '/' + str(len(options2)) + '\n' + 'Мы только учимся, вернитесь к правилу и попробуйте еще!'
                ques_label['bg'] = 'red'
        else:
            ques_label['text'] = questions2[index2]
            ques_label['bg'] = 'grey'

            disable_buttons('normal')
            opts = options2[index2]
            option1['text'] = opts[0]
            option2['text'] = opts[1]
            option3['text'] = opts[2]
            v1.set(opts[0])
            v2.set(opts[1])
            v3.set(opts[2])

            if index2 == len(options2) - 1:
                button_next['text'] = 'Проверить результаты'

    next_quest()


def ex_three():
    window = Toplevel()
    window.geometry("505x375")
    window.configure(background='#FA8072')
    frame = Frame(window, padx=10, pady=10, bg='#FA8072')
    ques_label = Label(frame, height=8, width=30, bg='#B22222', fg='#fff', font=('Veranda', 20), wraplength=500)

    btn1 = Button(frame, bg='#DDA0DD', width=10, text='Верно', font=('Veranda', 20), command=lambda: check_ans_right())
    btn2 = Button(frame, bg='#DDA0DD', width=10, text='Неверно', font=('Veranda', 20), command=lambda: check_ans_wrong())
    btn3 = Button(frame, text="Далее", font=('Veranda', 8), command=lambda: next_question())
    btn_rule = Button(frame, text="Правило", font=('Veranda', 8), command=lambda: rule_three())
    frame.pack(fill='both')
    ques_label.grid(row=0, column=0, columnspan=3)
    btn1.grid(row=2, column=0, pady=20, rowspan=2)
    btn2.grid(row=2, column=1, pady=20, rowspan=2)
    btn3.grid(row=2, column=2, pady=15)
    btn_rule.grid(row=3, column=2, pady=10)

    def check_ans_right():
        btn1.configure(state=DISABLED)
        btn2.configure(state=DISABLED)
        global correct3, index3
        if questions3[index3][0] == questions3[index3][1]:
            correct3 += 1
            ques_label['bg'] = 'green'
            ques_label['text'] = 'Молодец!'
        else:
            ques_label['bg'] = 'red'
            ques_label['text'] = f'Ошибка!\nВерный вариант:\n{questions3[index3][1]}'

        index3 += 1

    def check_ans_wrong():
        btn1.configure(state=DISABLED)
        btn2.configure(state=DISABLED)
        global correct3, index3
        if questions3[index3][0] != questions3[index3][1]:
            correct3 += 1
            ques_label['text'] = f'Правильно!\nВерный вариант:\n{questions3[index3][1]}'
            ques_label['bg'] = 'green'
        else:
            ques_label['bg'] = 'red'
            ques_label['text'] = f"Ошибка!\nЭто предложение правильное."

        index3 += 1

    def next_question():
        btn_rule.configure(state=DISABLED)
        global index3, correct3

        if btn3['text'] == 'Заново':
            correct3 = 0
            index3 = 0
            btn3['text'] = 'Далее'

        if index3 == len(questions3):
            btn_rule.configure(state='normal')
            ques_label['bg'] = '#B22222'
            ques_label['text'] = str(correct3) + '/' + str(len(questions3))
            btn3['text'] = "Заново"

        else:
            ques_label['bg'] = '#B22222'
            btn1.configure(state='normal')
            btn2.configure(state='normal')

            ques_label['text'] = questions3[index3][0]

            if index3 == len(questions3) - 1:
                btn3['text'] = "Результат"



    next_question()


root = Tk()
root.geometry("500x350")
root.title('培训课程')
root.configure(background='#ADD8E6')

for c in range(1): root.columnconfigure(index=c, weight=1)
for r in range(2): root.rowconfigure(index=r, weight=1)

t = Label(root, text='我们学习量词吧!', font='Times 30', fg='black', bg='#ADD8E6')
t.grid(row=0, column=0)
b = Button(root, text="Начать", bg='#87CEEB', activebackground='#00BFFF', border='10', font='Times 28',
           command=main_window)
b.grid(row=1, column=0)


root.mainloop()