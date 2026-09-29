meaning_ABC = [(0,0,0), (0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)]
meaning_ABC_TF = [(False,False,False), (False,False,True),(False,True,False),(False,True,True),(True,False,False),(True,False,True),(True,True,False),(True,True,True)]


print("A | B | C | №1| №2| №3")
print("-" * 23)
for A,B,C in (meaning_ABC):
    exercise1 = int(not(A & B)) | int(not(A | C))
    exercise2 = int(A & B) | int((not(B)) & C)
    exercise3 = int(A & B) | int(not(C))
    print(f"{A} | {B} | {C} | {exercise1} | {exercise2} | {exercise3} |")

print("\n" + "-"*30 + "\n")

print("A \t|B \t| C \t|  №1 \t| №2 \t| №3\t|")
print("-" * 40)
for A,B,C in (meaning_ABC_TF):
            exercise1 = (not(A and B)) or (not(A or C))
            exercise2 = (A and B) or (not(B) and C)
            exercise3 = (A and B) or not(C)
            
            print(f"{A}\t| {B}\t| {C}\t| {exercise1}\t| {exercise2}\t| {exercise3}\t|")