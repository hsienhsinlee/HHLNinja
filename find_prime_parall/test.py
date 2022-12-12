import multiprocessing as mp
import time
   
  
def square(x):
    return x * x
   
if __name__ == '__main__':
    #pool = mp.Pool()
    while True:
        max_num = int(input("Enter the maximum number (0 to quit): "))
        if max_num == 0:
            break
        pool = mp.Pool(mp.cpu_count())
        inputs = range(1,max_num) #[0,1,2,3,4]
        outputs = pool.map(square, inputs)
        print("Input: {}".format(inputs))
        print("Output: {}".format(outputs))