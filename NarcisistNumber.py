import numpy as np
import numpy.testing as npt
def narcicist(value):
    arrayofValue = [int(i) for i in str(value)]
    lenofArray = len(arrayofValue)
    result = 0
    for i in range(len(arrayofValue)): 
        result = arrayofValue[i]**lenofArray + result  
    if (result == value):
        return True
    else:
        return False 
    
if __name__ == '__main__':
   npt.assert_equal(narcicist(7),True,'7 is narcisist')