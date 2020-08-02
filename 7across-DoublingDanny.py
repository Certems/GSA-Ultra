#a = [2,5,1]#list of ints
#m = [3,2,4]#list of ints

#import pickle
#a = pickle.load(open("sl_doubling_danny.pkl","rb"))[0]
#m = pickle.load(open("sl_doubling_danny","rb"))[1]

def solution(a, m):
    x = 0; # CAN BE REMOVED ONCE CONFIRMED WORKING
    sumation = 0
    for index in range(len(a)):
        x = a[index] # CAN BE REMOVED ONCE CONFIRMED WORKING
        sumation += ( 2**x )
    sumation = sumation % m

    return sumation

#print(solution(a,m))
