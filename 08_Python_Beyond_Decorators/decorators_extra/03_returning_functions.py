def create_exp(x):
    def exp(num):
        return x ** num
    return exp

exp2 = create_exp(2)
exp3 = create_exp(3)

print(exp2(2))
print(exp3(2))