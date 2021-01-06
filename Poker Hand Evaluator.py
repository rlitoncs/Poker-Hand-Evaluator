#Ralph Liton 


def evaluate(hand):
    ranks = ''
    allranks = '0123456789TJQKA'

    if len(hand) > 0:                                           #flush
        result = hand.count(hand[1]) == len(hand[1::2])         #This counts the number of times hand[1] reoccurs in the hand. It reoccurs 5 times
                                                                #Therefore if the length of hand[1::2] (which is 5), is equal to hand.count(hand[1])
    if result == True:                                          #we have a flush
        return 'flush' 
                 

    for t in hand[0::2]:        
        ranks = ranks + t                                       #Takes only the Ranks from the hand
    
    from collections import Counter
    counters = Counter(ranks)


    for q in ranks:                                             #full house
        for p in ranks:
            if counters[q] == 3:
                if counters[p] == 2:
                    return 'full house'
    else:
        for p in ranks:                                         #four of a kind
            if counters[p] == 4:
                return 'four of a kind'

            elif counters[p] == 3:                              #three of a kind
                return 'three of a kind'

            elif counters[p] == 2:                              #pair
                return 'pair'


    for y in allranks[::-1]:                                    #highestrank
        for x in hand[0::2]:
            if y == x:
                largestrank = y + ' high'
                return largestrank
     

    

#TestCode:

hand_list = ['Qs7s2s4s5s', '7h8hKsTs8s', '2h4d2d4s4c', 'KsKhKc8sKd', '3s9hTh9s9d', '2s8hThQs9d']

for b in hand_list:
    print(evaluate(b))










