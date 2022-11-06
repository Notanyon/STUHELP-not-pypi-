import numpy
import os
from time import sleep

print("""
░█▀▀▀█ ▀▀█▀▀ ░█─░█ ░█─░█ ░█▀▀▀ ░█─── ░█▀▀█ 
─▀▀▀▄▄ ─░█── ░█─░█ ░█▀▀█ ░█▀▀▀ ░█─── ░█▄▄█ 
░█▄▄▄█ ─░█── ─▀▄▄▀ ░█─░█ ░█▄▄▄ ░█▄▄█ ░█───            ᵐᵃᵈᵉ ᵇʸ ᵃᵈⁱᵗʸᵃ ʲʰᵃ""")

Length = int(input("Enter the length of data(must be in integer or numerical value only) : "))
Length_str = str(Length)

def Length_fun(l,ls):
    print(l)
    print(ls)

while Length == str(Length):
    print("Error : The amount of length of data is in string format please solve it and try again.")
    sleep(3)
    os.system('cls')
    Length_1 = input("Enter the length of data : ")
    Length_str_1 = str(Length_1)
    if Length_1 != Length_str_1:
        break

Array_process = []
a = 1
while a <= Length:
    Input = float(input("Enter the data(one by one): "))
    Array_process.append(Input)
    a = a+ 1

print(Array_process)
Confirm = str(input("The above Data is the data you entered kindly confirm it: yes(y) or no(n): "))
if Confirm.lower() == 'y':
    print('The list of data is ready.')
    Action_Array = str(input("Kindly choose the action you want to do with this array - Sort(s), Mean(m), Medium(md), Mode(mo) : "))

    if Action_Array.lower() == 's':
        Array_process.sort()
        print(Array_process)
        print("Kindly press any key to exit")
        Exit_s = input()

    if Action_Array.lower() == 'm':
        Array_process_m_1 = numpy.array(Array_process)
        Array_process_m_2 = numpy.mean(Array_process_m_1)
        print(Array_process_m_2)
        print("Kindly press any key to exit")
        Exit_s = input()

    if Action_Array.lower() == 'md':
        Array_process_md_1 = numpy.array(Array_process)
        Array_process_md_2 = numpy.median(Array_process_md_1)
        print(Array_process_md_2)
        print("Kindly press any key to exit")
        Exit_s = input()

    if Action_Array.lower() == 'mo':
        most = max(list(map(Array_process.count, Array_process)))
        RETURN = list(set(filter(lambda x: Array_process.count(x) == most, Array_process)))
        print(RETURN)
        print("Kindly press any key to exit")
        Exit_s = input()
else:
    exit()
