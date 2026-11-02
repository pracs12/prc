def f(x):
    return (x+3)**2

def gradient(x):
    return 2*(x+3)


x = 2
lr = 0.1
iterations = 100

for i in range(iterations):
    x = x - lr * gradient(x)

print("Local Minimum x : ",x)
print("Minimum value y : ",f(x))