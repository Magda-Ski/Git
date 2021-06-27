groceries = {
    "tesco":['pączki' ,' bułki' ,' chleb'],
    "warzywniak":['seler',' marchewka', ' rukola']
}
first = [key for key in groceries]
#print(first)
zakupy = first[0]
zakupy_2 = first[1]
pieczywo = groceries["tesco"]
#print(pieczywo)
warzywa = groceries["warzywniak"]
#print(warzywa)
sum= warzywa + pieczywo
x = len(sum)

pieczywo= [p.title() for p in pieczywo]
#print(pieczywo)
warzywa = [w.title() for w in warzywa]
print("Idę do " ,  zakupy.capitalize(), " i kupuję tam " , pieczywo)
print("Idę do " ,zakupy_2.capitalize() , " i kupuję tam" , warzywa)
print('W sumie kupuję' , x , 'produktów.')
print("Chyba o to chodzi w tych branch'ach")
print("Branch")