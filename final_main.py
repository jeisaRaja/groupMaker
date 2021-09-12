import random
import csv
from tkinter import filedialog
from tkinter import *

# people = ['Jeisa', 'kresna', 'Frendo', 'Vito', 'Hapiz', 'Kevin']
# file = input("Directory file:")

root = Tk()
root.title('Group Maker')
def opening():
    global file
    global people
    root.filename = filedialog.askopenfilename(initialdir="/C:/", title="Select A File", filetypes=(("csv files", "*.csv"),))
    file = root.filename
    root.destroy()
    with open(f'{file}', 'r') as f:
        reader = csv.reader(f)
        people = list(reader)

my_btn = Button(root, text="Select File", command=opening).pack()
root.mainloop()
n = len(people)
print(f'Terdapat {n} orang pada file ini')
judul = input('Kelompok Apa Ini?    : ')
fh = open(f'kelompok/{judul}.txt', 'w')


opsi = int(input('Jumlah Kelompok atau Jumlah Anggota  : '))

temp = []
temp2 = []


def acak(x, y, sisa):
    if (sisa > 0):
        for sis in range(sisa):
            temp2.clear()
            print('\n')
            fh.write('\n')
            fh.write(f'Kelompok {sis + 1}')
            fh.write('\n')
            for j in range(int(y) + 1):
                u = random.choice(people)
                people.remove(u)
                temp2.append(u)
            # print(temp2)
            for line in temp2:
                print(line)
                fh.write("%s\n" % line)
    for i in range(x - sisa):
        temp.clear()
        print('\n')
        fh.write('\n')
        fh.write(f'Kelompok {i + sisa + 1}')
        fh.write('\n')
        for j in range(int(y)):
            r = random.choice(people)
            people.remove(r)
            temp.append(r)
        # print(temp)
        for line2 in temp:
            fh.write("%s\n" % line2)
            print(line2)


if opsi == 1:
    x = input("Jumlah Kelompok  :  ")
    x = int(x)
    y = n / x
    sisa = n % x
    acak(x, y, sisa)
elif opsi == 2:
    z = input("Jumlah Anggota  :  ")
    z = int(z)
    y = z
    x = int(n / y)
    sisa = n % y
    acak(x, y, sisa)

fh.close()
# print(f"SISA:{people}")
# print(len(people))
