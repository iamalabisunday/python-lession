# Write a Python program to print "Hello Python".
print("Hello Python")

# standard Method
class Python:
    def __init__(self, words: str):
        self.words = words
    def __str__(self):
        return f"{self.words}"
    def __repr__(self):
        return f"Python: {self.words}"

def main():
    words = input("Enter your first statement: ")
    result = Python(words)
    print("------------------------------------")
    print(result)
    print("------------------------------------")

def try_again():
    while True:
        again = input("Do you want to try again (y|n): ").strip().lower()
        if again in ("y", "yes"):
            return True
        elif again in ("n", "no"):
            return False
        print("Invaild: Kindly enter yes or no")

if __name__ == "__main__":
    while True:
        main()
        if not try_again():
            print("------------------------------------")
            print("GoodBye")
            break