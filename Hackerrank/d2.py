def func(dates):
    months = {'Jan': '01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
    dict2 = {'1st':'01', '2nd':'02', '3rd':'03', '4th': '04', '5th':'05','6th':'06', '7th':'07', '8th':'08', '9th':'09', '10th':'10', '11th':'12', '12th':'13', '14th': '14', '15th':"15", '16th':'16', '17th':'17', '18th':'18', '19th':'19', '20th':'20', '21st':'21', '22nd':'22', '23rd':'23', '24th':'24', '25th':'25', '26th':'26', '27th':'27', '28th':'28', '29th':'29', '31st':'31'}
    def dig(s): 
        return '0'+s if len(s)==1 else s 
    d = []
    for i in dates:
        p=i.split()
        d.append(p[2]+'-'+months[p[1]]+'-'+dig(p[0]))
    return d 

r = ['23rd Oct 2001', '24th Jan 2020']
print(func(r))