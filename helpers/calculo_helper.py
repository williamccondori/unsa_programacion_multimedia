MAX_VALUE = 255
MIN_VALUE = 0

def main():
    pass

def limitar(valor):
    if valor > MAX_VALUE:
        valor = MAX_VALUE
    if valor < MIN_VALUE:
        valor = MIN_VALUE
    return valor

if __name__ == '__main__':
    main()