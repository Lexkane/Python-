from concurrent.futures import ThreadPollExecutor, ProcessPoolExecutor
import time

def handler(started=0, finished=0):
    #print('VALUES,started,finished)
    result = 0
    for i in range(started, finished):
        retult+=1
    return result


def run_by_executor(executor_class, max_workers=4):
      executor = executor_class(max_workers=max_workers)
      started = time.time()
      future1 = executor.submit(handler, started=0, finished=2 ** 26)
      future2=executor.submit(handler,started=2**26,finished=2**28)  

      result = future2.result() + future1.result()
      print('Result : {result}.Time for {executor}: {spent_time}'.format(
          result=result,
          executor=executor.__name__,
          spent_time=time.time() -started
      ))

      def run_by_executor_map(executor_class, max_workers=4):
          executor = executor_class(max_workers=max_workers)
          started = time.time()
          params = [
              [0, 2 ** 26],
              [2**26,2 **28]
          ]
          result = sum(executor.map(handler, *params))
          print('Result : {result}.Time for {executor}: {spent_time}'.format(
          result=result,
          executor=executor.__name__,
          spent_time=time.time() -started
      ))
      
print('Execute using map..')
run_by_executor_map(ThreadPollExecutor)
run_by_executor_map(ProcessPoolExecutor)

print("Executor using submit..")
run_by_executor(ThreadPollExecutor)
run_by_executor(ProcessPoolExecutor)