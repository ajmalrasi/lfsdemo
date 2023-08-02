import threading

def is_prime(size, ID):
    for num in range (1, size):
        count = 0
        for i in range(2, (num//2 + 1)):
            if(num % i == 0):
                count = count + 1
                break

        if (count == 0 and num != 1):
            pass
            # print("{} is prime: True".format(num))
        else:
            pass
            # print("{} is prime: False".format(num))
            
if __name__ == "__main__":
    size = 1000000  
    threads = 2

    jobs = []
    for i in range(0, threads):
        out_list = list()
        thread = threading.Thread(
            target=is_prime(size, i)
        )
        jobs.append(thread)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()