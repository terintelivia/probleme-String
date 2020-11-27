s=str(input("introdu sirul de caractere: "))
nrm = 0
nrc = 0
nrs = 0
for i in s:
    if ((ord(i))>=65) and ((ord(i))<=90):
        nrm+=1
    if ((ord(i))>=48) and ((ord(i))<=57):
        nrc+=1
    if((ord((i))>=33)and(ord((i))<=47))or((ord((i))>=58)and(ord((i))<=64))or((ord((i))>=91)and(ord((i))<=96))or((ord((i))>=123)and(ord((i))<=127)):
            nrs+=1
print(f'Numarul de litere majuscule este {nrm}')
print(f'Numarul de cifre este {nrc}')
print(f'Numarul de caractere speciale este {nrs}')