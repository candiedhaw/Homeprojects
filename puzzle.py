def num_to_letter(num):
    return chr(num+64)

alist=[]

a=''


while True:
    num = input()
    if num == ' ': a= a +' '
    elif num == ',': a = a+','
    else: a = a + num_to_letter(int(num))

print(a)


