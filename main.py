import statistik
def main():
    data = []
    d = input('Masukkan nama file: ')

    try:
        infile = open(d, 'r')
        for i in infile:
            y = float(i)
            data.append(y)
        statistik.mean(data)
        statistik.var(data)
        statistik.std(data)
        statistik.median(data)
    except FileNotFoundError:
        print('File tidak ditemukan.')
    except ValueError:
        print('File berisi data non-numerik.')

main()
