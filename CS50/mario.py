def main():
    height=int(input("What is height? "))
    prymid(height)
def prymid(n):
    for i in range(n):
        print("#"*i)
main()