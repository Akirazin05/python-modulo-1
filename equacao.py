print("Olá, me informe o Valor de A, B e X para representar uma função do primeiro grau:\n")


#pede os valores das variaveis ao usuario
a = input("Qual o Valor de A é: ")
b = input("Qual o Valor de B é: ")
x = input("Qual o Valor de X é: ")


#as reconhece com tipo inteiro
a = int(a)
b = int(b)
x = int(x)


#formula da equaçao de primeiro grau
f_x = (a)*x + b


#apresenta o resultado para o usuario
print(f"f(x) = ({a})x + ({b})")
print(f"f({x}) = {f_x}")
                    
