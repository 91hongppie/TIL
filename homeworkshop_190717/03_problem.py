show = int(input())

def tax(me):
    if me <= 1200:
        return me * 0.06
    elif 1200< me <= 4600:
        return 1200 * 0.06 + (me-1200)* 0.15
    elif 4600 < me:
        return 1200 * 0.06 + 3400* 0.15 + (me-4600) * 0.35

money = tax(the)
print(money)


time, distance = int(input()), int(inpue())

def calculater(t, d):
    d_fee = 0
    t_fee = 0
    i_fee = 0
    if t % 2 == 0:
        t_fee=(t//10)*1200
    else:
        t_fee=((t//10)+1)*1200
    if t % 60 > 30:
        i_fee = (t // 30 + 1) * 525
    else:
        i_fee = (t // 30) * 525
    if d <= 100:
        d_fee = d * 170
    else:
        d_fee = 100*170+(d-100)*85
    return t_fee+i_fee+d_fee

result = calculater(time, distance)
print(result)


    
    