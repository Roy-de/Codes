
def mean(params):
    result = 0
    for i in params:
        result = result + i
        
    answer = result/len(params)
    return answer

if __name__ == '__main__':
    params = [1,2,3,4,5,6,7,8,9,10]
    result = mean(params)
    print(result)
        