import time
import boto3

bucket = "akaisuisei99"

if __name__ == "__main__":
    n = int(input("n: "))
    fread = open(input("input file: ").strip(), 'r')
    r = fread.read()
    fread.close()
    s3 = boto3.resource('s3')
    t_start = time.time()
    for i in range(n):
        s3.Bucket(bucket).put_object(Key="write_"+str(i)+".txt", Body=r)
    t_end = time.time()
    print(t_end-t_start)