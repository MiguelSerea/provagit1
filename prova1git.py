n = input("Por favor digite seu salário: ")
total = n

def aumento(n):
    if(n < 400.01){
        n = n * (15 / n)
    }else if(n >= 400.01 && n < 800.01){
        n = n * (12 / n)
    }else if(n >= 800.01 && n < 1200.01){
        n = n * (10 / n)
    }else if(n >= 1200.01 && n < 2000.01){
        n = n * (7 / n)
    }else if(n >= 2000.1){
        n = n * (4 / n)
    }

aumento(n)
total = total + n

print("Seu reajuste foi de "+ n " seu salário após o reajuste é de " + total)