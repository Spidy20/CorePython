try:
    def product(a, b):
        p = a * b
        print(p)

    def product(a, b,c):
        p = a * b *c
        print(p)
    product(4, 5,6)

except Exception as e:
    print(e)