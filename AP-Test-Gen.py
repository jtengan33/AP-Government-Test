import tkinter, random, time, math

def GUI(answer, qs, qtxt):
    clear()
    T = tkinter.Text(master = frame, height = int(math.ceil(len(qtxt)/75)), width = 75)
    T.pack()
    T.insert(tkinter.END, qtxt)
    pos = [[] for i in range(4)]
    ans_pos = random.randint(0,3)
    pos[ans_pos] = answer
    for i in range(len(pos)):
        if pos[i] == []:
            pos[i] = qs[0]
            del qs[0]

    for i in range(4):
        bs = tkinter.Button(master = frame, text = pos[i], command = correct if i == ans_pos else wrong)
        bs.pack()
    
def correct():
    goodbut = tkinter.Button(master = frame, bg = '#45B39D', text = 'Correct!', command = grab_data)
    goodbut.pack()

def wrong():
    badbut = tkinter.Button(master = frame, bg = '#FF5733', text = 'Incorrect')
    badbut.pack()
    
def clear():
    for widget in frame.winfo_children():
        widget.destroy()
        
def grab_data():
    path = 'QuestionData.txt'
    parse_data(str(open(path).read()).split('\n'))

def parse_data(data):
    
    while True:
        item = data[random.randint(0,len(data))]
        if item not in seen:
            seen.append(item)
            break
    del data[data.index(item)]
    item = str(item)

    item = item.split(',')
    qtype = ''
    question = ''
    answer = ''
    bads = []

    question = item[0]
    del item[0]
    answer = item[0]
    del item[0]

    for _ in range(4):
        bads.append(item[0])
        del item[0]
    qytpe = item[0]
    GUI(answer, bads, question)
        

    
def welcome():
    start = tkinter.Button(master = frame, text = 'BEGIN', command = grab_data)
    T = tkinter.Text(master = frame, height = 2, width = 50)
    T.pack()
    T.insert(tkinter.END, "Welcome to the AP Government Test Generator\nClick the button to begin\n")
    
    start.pack()
    
def main():
    welcome()
    
frame = tkinter.Tk()
if __name__ == '__main__':
    seen = []
    main()

