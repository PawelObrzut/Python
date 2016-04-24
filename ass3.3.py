def computegrade(x):
    if x > 0.9: print 'A'
    elif x > 0.8: print 'B'
    elif x > 0.7: print 'C'
    elif x > 0.6: print 'D'
    elif x <= 0.6: print 'F'
    
while True:
    try:
        int = raw_input('Enter score: ')
        if int == 'done' : break
        int = float(int)
        if int > 1.0:
            print 'Bad score'
            continue
        elif int < 0.0:
            print 'Bad score'
            continue
        print computegrade(int)
    except:
        print 'Bad score'