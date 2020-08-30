import time
input_file = "random_large.txt"

if __name__ == "__main__":
    n = int(input())
    fread = open(input_file, 'r')
    r = fread.read()
    fread.close()
    t_start = time.time()
    for i in range(n):
        fwrite = open("write_"+str(i)+".txt", 'w')
        fwrite.write(r)
        fwrite.close()
    t_end = time.time()
    print(t_end-t_start)