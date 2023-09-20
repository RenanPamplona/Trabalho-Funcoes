def f(function, x):
    return eval(function)


def g(function, x):
    return eval(function)


def gof(f_function, g_function, x):
    return g(g_function, f(f_function, x))


def fog(f_function, g_function, x):
    return f(f_function, g(g_function, x))


def gog(g_function, x):
    return g(g_function, g(g_function, x))


def fof(f_function, x):
    return f(f_function, f(f_function, x))


function_input_rules = "\nRegras:\n"
function_input_rules += " => Digite o x em minúsculo\n"
function_input_rules += " => Digite x² ou x³ como (x * x) ou (x * x * x)\n"
function_input_rules += (
    " => Utilize os seguintes sinais: +, -, * (multiplicação), / (divisão)\n"
)
function_input_rules += (
    " => Se for o caso de haver chaves ou colchetes, utilize apenas parênteses ()\n"
)
function_input_rules += (
    " => Digite apenas a equação. Se sua função for f(x) = x + 1, digite apenas x + 1\n"
)

print(function_input_rules)

is_written_wrong = True

f_function = input("Digite a função para f => ")
g_function = input("Digite a função para g => ")

while is_written_wrong:
    try:
        f(f_function, 1)
        g(g_function, 1)
        is_written_wrong = False
    except:
        is_written_wrong = True
        print("Declaração de função inválida, tente novamente")
        f_function = input("Digite a função para f => ")
        g_function = input("Digite a função para g => ")

x_value = int(input("Digite o valor de x => "))

print(f"g o f: {gof(f_function, g_function, x_value)}")
print(f"g o g: {gog(g_function, x_value)}")
print(f"f o f: {fof(f_function, x_value)}")
print(f"f o g: {fog(f_function, g_function, x_value)}")
