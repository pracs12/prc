
class Fibonacci:
    
    def fibonacci(n):
        if n <= 1:
            return n
        
        return Fibonacci.fibonacci(n-1) + Fibonacci.fibonacci(n-2)
    

    def recursive(n):
        result = []
        for i in range(n):
            result.append(Fibonacci.fibonacci(i))
        
        print(" ".join(map(str,result)))

    
    def iterative(n):
        a,b = 0,1
        result = [a,b]

        for _ in range(2,n):
            c = a + b
            result.append(c)
            a, b = b,c

        print(" ".join(map(str,result)))


if __name__ == "__main__":
    recusive_count = int(input("Enter the number of fibonacci numbers for recursive method:"))
    Fibonacci.recursive(recusive_count)
    iterative_count = int(input("Enter the number of fibonacci numbers for iterative method:"))
    Fibonacci.iterative(iterative_count)