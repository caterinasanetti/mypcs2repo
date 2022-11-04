def birthdayCakeCandles(candles):
    tcandles=0
    tallest= max(candles)
    for i in candles:
        if i != tallest:
            tcandles += 0
        else:
            tcandles += 1
                
    return tcandles