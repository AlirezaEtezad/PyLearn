import time
import threading



def A(name, family):
      for i in range(10):
            print("Hello", name, family)
            time.sleep(1)

def B(name):
      for i in range(10):
            print("Bye", name)
            time.sleep(1)


t1 = threading.Thread(target=A, args=["ali", "hoseini"])
t2 = threading.Thread(target=B, args=["mamad"])

t2.start()
t1.start()



