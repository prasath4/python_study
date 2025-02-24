#simple thread using function
import threading
import time

# def print_hello():
#     for _ in range(5):
#         print("Hello from thread!")
#         time.sleep(1)  # Simulate some work

# # Create a thread
# t = threading.Thread(target=print_hello)

# # Start the thread
# t.start()

# # Wait for the thread to finish
# t.join()

# print("Main thread finished!")



#single thread using class

# class thread(threading.Thread):
#     def run(self):
#         for _ in range(5):
#             print('Say my name')
#             time.sleep(1)

# t=thread()

# t.start()
# t.join()

# print('threading successfull finished')


'''
multiple thread using function

def ask():
    for _ in range(5):
        print('say my name')
        time.sleep(1)

def tell():
    for _ in range(5):
        print('heisonberg')
        time.sleep(1)

t1=threading.Thread(target=ask)
t2=threading.Thread(target=tell)
t1.start()
t2.start()
t1.join()
t2.join()
print('finished')
'''




# multiple threading using classes

# class MyThread(threading.Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name  # Assign thread name

#     def run(self):
#         for i in range(3):
#             print(f"{self.name} is running - iteration {i+1}")
#             time.sleep(1)  # Simulate work

# # Creating multiple threads
# thread1 = MyThread("Thread 1")
# thread2 = MyThread("Thread 2")
# thread3 = MyThread("Thread 3")

# # Start all threads
# thread1.start()
# thread2.start()
# thread3.start()

# # Wait for all threads to finish
# thread1.join()
# thread2.join()
# thread3.join()

# print("All threads have finished execution!")


#THREAD POOLING 
# Thread Pooling in Python (Using concurrent.futures.ThreadPoolExecutor)
# Thread pooling is useful when you have multiple tasks to execute concurrently but don't want to create and manage threads manually. 
# The ThreadPoolExecutor class from the concurrent.futures module helps manage multiple threads efficiently.




'''
import concurrent.futures
import time

def worker():
    print("Worker thread is running")
    time.sleep(1)  # Simulate some work

# Create a thread pool with 2 workers
pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

# Submit tasks to the pool
pool.submit(worker)
pool.submit(worker)

# Shutdown the pool and wait for threads to complete
pool.shutdown(wait=True)

print("Done")

'''



# import concurrent.futures
# import time

# def task(n):
#     print(f'task {n} is statred')
#     time.sleep(2)
#     print(f'task {n} is finished')
#     return f'result {n} is completed'

# with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executer:
#     results = executer.map(task, range(5))

# for result in results:
#     print(result)


# print('all task completed successfully')

'''Why Use with in ThreadPoolExecutor?
Using with ensures that the ThreadPoolExecutor is properly initialized and 
shutdown when the block of code completes execution, preventing resource leaks and improving code readability.'''






# multi threading using lock method

counter = 0

lock=threading.Lock()

def increment():
    global counter
    for _ in range(5):
        with lock:
            local_counter = counter
            time.sleep(0.5)
            local_counter+=1
            counter = local_counter
            print(f'counted update is {counter}')


# Creating multiple threads
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print(f"Final counter value: {counter}")



'''import threading
import time

# Global variable
counter = 0

# Creating a Reentrant Lock
rlock = threading.RLock()

def increment():
    global counter
    with rlock:  # First lock acquisition
        for _ in range(3):
            nested_increment()  # Calling a function that acquires the lock again
            time.sleep(0.1)

def nested_increment():
    global counter
    with rlock:  # Second lock acquisition (same thread)
        counter += 1
        print(f"Counter updated to: {counter}")

# Creating multiple threads
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print(f"Final counter value: {counter}")
'''