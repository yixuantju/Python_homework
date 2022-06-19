import time


'''def ProgressBar(scale)
  for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    t=time.perf_counter()
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,t))'''

scale_all=17

def ProgressBar_begin(scale):
  for i in range(scale+1):
    a='*'*i
    b='.'*(scale_all-i)
    t=time.perf_counter()
    print("\r[{}->{}]{:.2f}s".format(a,b,t))
    global scale_now
    scale_now=0

def ProgressBar_inter(scale,scale_last):
  global scale_now
  scale_now+=scale_last
  for i in range(scale+1):
    a='*'*i
    b='.'*(scale_all-scale_now-i)  
    c='*'*scale_now
    t=time.perf_counter()
    print("\r[{}{}->{}]{:.2f}s".format(c,a,b,t))

def ProgressBar_end(scale,scale_last):
  global scale_now
  scale_now+=scale_last
  for i in range(scale+1):
    a='*'*i
    b='.'*(scale_all-scale_now-i) 
    c='*'*scale_now
    t=time.perf_counter()
    print("\r[{}{}->{}]{:.2f}s".format(c,a,b,t))
  print("----------程序执行结束----------")

