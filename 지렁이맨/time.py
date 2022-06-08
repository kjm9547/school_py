
import time
fseconds = time.time()//60

hour = fseconds//60%24
min = fseconds%60
print(hour)
print(min)