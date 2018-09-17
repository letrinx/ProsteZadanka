# ProsteZadanka

1. Napisz funkcję `sum_range(min, max)`, która zwróci sumę liczb całkowitych od `min` do `max` włącznie.

```py
print(sum_range(2,5)) # zwróci 14

print(sum_range(-2,2)) # zwróci 0
```

2. Napisz funkcję `min_and_max(lista)`, która przyjmuję listę liczb a zwraca krotkę z najmniejszą i największą liczbą z listy

```py
min_and_max([3,5,-3,12,-2,0]) # zwróci (-3, 12)

min_and_max([12]) # zwróci (12,12)

min_and_max([]) # zwróci (None, None)
```

3. Napisz funkcję `speed(distance, time)`, która policzy i zwróci średnią prędkość dla pokonanej drogi (`distance`) w metrach i czasu w sekundach (`time`). `Hint` użyj formatowanie stringa.

```py
speed(100,10) # zwróci 10 m/s
speed(2,10) # zwróci 0.2 m/s
```

4. Napisz funkcję `split_list(lista)`, która podzieli listę na dwie listy (pierwszy element do pierwszej drugi do drugiej, trzeci do pierwszej, czwarty do drugiej itd.) i zwróci jaką krotkę list.

```py
print(split_list([1,3,5,7,10,11,12,13]))
# Zwróci ([1,5,10,12], [3,7,11,13])
```

5. Napisz funkcję `multiply_list(lista, num)`, która pomnoży każdy element listy przez liczbę `num` i ją zwróci.

```py
print(multiply_list([3,5,2,6], 2))
# zwróci [6,10,4,12]
```

6. Napisz funkcję `count_character(text, letter)`, która zróci liczbę wystąpień podanej litery `letter` w tekscie `text`. Zliczamy duże i małe litery.

```py
print(count_character('Mam dzisiaj dobry humor', 'm'))
# zwróci 3
```