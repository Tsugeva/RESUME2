def treug (a, b, c):
   p = (a + b + c) / 2
   s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
   return s

#запроашиваем значение сторон треугольника
a = int(input("введите длину стороны a: "))
b = int(input("введите длину стооны b: "))
c = int(input("введите длину сторны с: "))

#вычесление площади
area = treug(a, b, c)

#вывод самого результата
print(f"площадь треугольника со сторонами {a} {b} {c} равна: {area}") 