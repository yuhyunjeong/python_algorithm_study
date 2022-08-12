book = []
total = int(input())
for i in range (1,10):
    price = int(input())
    book.append(price)
    
print(total - sum(book))

