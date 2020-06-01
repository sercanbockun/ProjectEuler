square_toplam=0
toplamin_square=0
ilk100toplam=0
for x in range(1,101):
    square_toplam=square_toplam + x**2


print(square_toplam)


for x in range(1,101):
    ilk100toplam=ilk100toplam + x

toplamin_square=ilk100toplam**2
print(toplamin_square)
print(toplamin_square-square_toplam)

