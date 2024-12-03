# exercice 3 : table de multiplication 9
def table_multiplication():
    for i in range(1,10,1):
        for e in range(1,10,1):

            print(f"{i*e:2}", end="  ")
        print()

table_multiplication()