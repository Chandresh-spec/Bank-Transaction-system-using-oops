class A:
    def greet(self):
        print("Hello from class A")

class B(A):
    def greet(self):
        super().greet()   # Call parent method
        print("Hello from class B")

# b = B()
# b.greet()
