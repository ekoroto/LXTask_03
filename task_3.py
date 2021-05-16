from concurrent.futures import ThreadPoolExecutor, as_completed


def function(arg, a):
    for _ in range(arg):
        a += 1
    return a


def main():
    a = 0
    with ThreadPoolExecutor(max_workers=5) as pool:
        result = [pool.submit(function, 1_000_000, a) for _ in range(5)]

        for future in as_completed(result):
            a += future.result()

        print("----------------------", a)


main()
