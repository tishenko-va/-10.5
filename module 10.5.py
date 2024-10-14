import multiprocessing
import time

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            else:
                all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start = time.time()
for name in filenames:
    read_info(name)
end = time.time()
time = end - start
print(f'Линейный: {time}')

if __name__ == '__main__':
    import time #если не импортировать снова,то не работает в этой части кода.
                # Не замечала такого раньше
    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = time.time()
    time = end - start
    print(f' Многопроцессный: {time}')

