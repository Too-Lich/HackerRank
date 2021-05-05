with open('input.txt', 'r', encoding='utf-8') as f:
    a, b = map(int, f.read().split())
    if not (a > 10 ** 9 or b > 10 ** 9):
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(str(a + b))
