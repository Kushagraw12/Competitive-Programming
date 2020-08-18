import sys
from collections import deque
input = sys.stdin.readline
def Reverse(lst): 
    return [ele for ele in reversed(lst)]
    
def preprocessdate(dates):
    nd = deque(dates)
    n = []
    dict1 = {'Jan': '-01-', 'Feb':'-02-', 'Mar':'-03-', 'Apr':'-04-', 'May':'-05-', 'Jun':'-06-', 'Jul':'-07-', 'Aug':'-08-', 'Sep':'-09-', 'Oct':'-10-', 'Nov':'-11-', 'Dec':'-12-'}
    dict2 = {'1st':'01', '2nd':'02', '3rd':'03', '4th': '04', '5th':'05','6th':'06', '7th':'07', '8th':'08', '9th':'09', '10th':'10', '11th':'12', '12th':'13', '14th': '14', '15th':"15", '16th':'16', '17th':'17', '18th':'18', '19th':'19', '20th':'20', '21st':'21', '22nd':'22', '23rd':'23', '24th':'24', '25th':'25', '26th':'26', '27th':'27', '28th':'28', '29th':'29', '31st':'31'}
    for k in nd:
        for o in k.split():
            if o in dict2:
                n.append(dict2[o])
                
            elif o in dict1:
                n.append(dict1[o])
                
            elif len(o) == 4:
                n.append(o)
                
    print (''.join(n))
    return Reverse(n)
    
t = int(input())
for _ in range(t):
    d = ["23rd Oct 2020"]
    print(''.join(preprocessdate(d)))