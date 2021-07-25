from threading import Thread
from time import sleep, perf_counter


# Test function
def showname(name):
    '''Test function'''
    print(f'Starting {name}...')
    sleep(3)
    print(f'Finished {name}...')

    

'''
# Multi threading in construct instance way, (*:for test unString all this codes and comment all of other codes) #########
t1=Thread(target=showname, args=('One',))
t2=Thread(target=showname, args=('Two',))
start=perf_counter()


t1.start()
t2.start()

t1.join() # Use when the we want interpreter wait for finish `t1` work and continue compile, else after starting `t1` continue compile next codes
t2.join()

end=perf_counter()

print(f'{round(end-start)} seconds')
# #######################################################################################################################
'''



'''
# Multi threading in inheritance way, (*:for test unString all this codes and comment all of other codes) ###############
class myThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name=name

    def run(self):
        showname(self.name)

start=perf_counter()

t3=myThread('Three')
t4=myThread('Four')

t3.start()
t4.start()

t3.join() 
t4.join()

end=perf_counter()

print(f'{round(end-start)} seconds')
# #######################################################################################################################
'''




'''
# Multi threading in ThreadPoolExecutor way, (*:for test unString all this codes and comment all of other codes) #########
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executer:
    names=['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']
    
    executer.map(showname, names)
    
# #######################################################################################################################
'''









