#!/usr/bin/env python3

import string
import random

#Character generating functions

#Generate Uppercase Letters
def Uppercase(Upper_Amount):
    U_Letter = []
    for i in range(Upper_Amount):
        U_Letter.append(random.choice(string.ascii_uppercase))
    return U_Letter

#Generate Lowercase Letters
def Lowercase(Lower_Amount):
    L_Letter = []
    for i in range(Lower_Amount):
        L_Letter.append(random.choice(string.ascii_lowercase))
    return L_Letter

#Generate Numbers
def Number(Num_Amount):
    Num = []
    for i in range(Num_Amount):
        Num.append(random.randint(1, 9))
    return Num

#Generate Special Characters
def Special(Special_Amount):
    Special = []
    for i in range(Special_Amount):
        Special.append(random.choice(string.punctuation))
    return Special

def Add_NumSpec(All, Start = 0, Spec_Num = 0):
    if Spec_Num < 2:
        if Start > 1:
            Start = 0
        else:
            All[Start] += 1
            Start += 1
    if Spec_Num < 1:
        if Start <= 1:
            All[Start] += 1
            Start += 1
        else:
            All[Spec_Num] += 1
            Start = 0
    Weak_Pass = Uppercase(All[0]) + Lowercase(All[1]) + Number(All[2]) + Special(All[3])
    return Weak_Pass, Start


#Generate Lists
def Generate(Pass_Length, Special_Val = False, Num_Val = False, Count = 4):

    Start = 0
    Remainder = Pass_Length%Count
    Base = Pass_Length//Count
    All = [Base,Base,Base,Base]
    while Remainder > 0:
        All[Start] += 1
        Start += 1
        Remainder -=1
    if Special_Val and Num_Val:
        Weak_Pass = Uppercase(All[0]) + Lowercase(All[1]) + Number(All[2]) + Special(All[3])
    elif Special_Val and not Num_Val:
        for i in range(All[2]):
            Add_NumSpec(All, 3)
            Weak_Pass = Uppercase(All[0]) + Lowercase(All[1]) + Special(All[3])
    elif not Special_Val and Num_Val:
        for i in range(All[3]):
            Add_NumSpec(All, 2)
            Weak_Pass = Uppercase(All[0]) + Lowercase(All[1]) + Number(All[2])
    elif not Special_Val and not Num_Val:
        for i in range(All[2]+All[3]):
            Add_NumSpec(All, Start)
            print(All)
            print(Start)
            Weak_Pass = Uppercase(All[0]) + Lowercase(All[1])
    #print(Weak_Pass)
    random.shuffle(Weak_Pass)
    Password = ""
    for i in Weak_Pass:
        Password += f"{i}"
    random.shuffle(Weak_Pass)
    print(Password)


def Main():
    # Variables
    Answers = ["Y","y","Yes","yes","no","No","N","n"]
    Count = 2
    Pass_Length = 0
    try:
        Pass_Length = int(input("Password Length? 12-16\n"))
    except ValueError:
        print("Not a number!")
    while Pass_Length not in range(12,17):
        try:
            Pass_Length = int(input("Password Length? 12-16\n"))
        except ValueError:
            print("Not a number!")
    Special_Var = input("Special Characters? (Y)es or (N)o\n")
    while Special_Var not in Answers:
        Special_Var = input("\nIncorrect Response\n Special Characters? (Y)es or (N)o")
    if Special_Var in Answers[:4]:
        Count += 1
    else:
        Special_Var = False
    Num_Var = input("\nNumbers? (Y)es or (N)o\n")
    while Num_Var not in Answers:
        Num_Var = input("\nIncorrect Response.\nChoose Y/y for yes or N/n for no\n")
    if Num_Var in Answers[:4]:
        Count +=1
    else:
        Num_Var = False

    Generate(Pass_Length, Special_Var, Num_Var, Count)
    close = input("\nPress Enter to exit")

if __name__ == "__main__":
    Main()