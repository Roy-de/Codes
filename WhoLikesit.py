def likes(names):
    i =  0
    count =  len(names) - 2
    if len(names) == 0:
        print("No one likes this")
    elif len(names) == 1:
        print(names[0] + " likes this") 
    elif len(names) == 2:
        print(names[0] + " and" + names[1] + "likes this")
    elif len(names) == 3:
        print(names[0] + " ," + names[1] + " and " + names[2] + " likes this")
    else:
        print(names[0] + " ," + names[1] + " and " ,count ,"others  likes this")    

if __name__ == '__main__':
    names = ["peter","Jacob" , "Alex","Max"]
    likes(names)