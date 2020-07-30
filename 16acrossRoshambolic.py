def solution(a, b):
    win_cond = {"R":0,"S":1,"P":2}

        #Main loop
    round_no = 0
    while ((len(a) > 0 and len(b) > 0)):
        annie_play = a[len(a)-1]
        betty_play = b[len(b)-1]
        if (win_cond[annie_play] == (win_cond[betty_play]+2)%3):
            a,b = annie_wins(a,b)[0],annie_wins(a,b)[1]
        elif (win_cond[betty_play] == (win_cond[annie_play]+2)%3):
            a,b = betty_wins(a,b)[0],betty_wins(a,b)[1]
        else:
            a = a[len(a)-1] + a
            a = a[0:len(a)-1]
            b = b[len(b)-1] + b
            b = b[0:len(b)-1]
        round_no+=1

        # if (round_no%10000 == 0):
        #     print("Round Number: ", round_no)
        #     print("a: ", a)
        #     print("b: ", b)
        #     print("")
        #     print("")
    return round_no

def annie_wins(a,b):
    a = a[len(a)-1] + b[len(b)-1] + a
    a = a[0:len(a)-1]
    b = b[0:len(b)-1]
    return [a,b]
    
def betty_wins(a,b):
    b = b[len(b)-1] + a[len(a)-1] + b
    a = a[0:len(a)-1]
    b = b[0:len(b)-1]
    return [a,b]


#print(solution("RPRPPSRSRRRSPSSRPPPPRPRRPSRSRP PSRPPPRSRSSRSRRRPPSRRPRPSSRPPPPSSSRSPRPSRRSRRRRRRSRSPPPRPPPRPSRPSRSRPS","SPRPPRSSSSPSSSSSRPSSPSPRSSRSRRSRSSSRRRPSRPSSSPRRRRSSRRRPSRRPRSPPPRRRPPSPRRPSPPPRRRPSPPRRPSRSSPPPSRRP"))