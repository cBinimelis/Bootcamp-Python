results = {}


def sum(num1, num2):
    return num1 + num2


def res(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def operations(num1, num2):
    answ_sum = sum(num1, num2)
    answ_res = res(num1, num2)
    answ_mul = mul(num1, num2)
    answ_div = div(num1, num2)
    return (answ_sum, answ_res, answ_mul, answ_div)


operations_test = operations(5, 5)

results = {
    "Suma": operations_test[0],
    "Resta": operations_test[1],
    "Multiplicacion": operations_test[2],
    "División": operations_test[3],
}
