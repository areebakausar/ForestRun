#Faiz Khan (fk6jr)

def mean (a,b,c):
   avg= (a+b+c)/3
   return avg

def median (a,b,c):
    if c<a<b:
        return a
    elif b<a<c:
        return a
    elif a<b<c:
        return b
    elif c<b<a:
        return b
    else:
        return c

def rms(a,b,c):
    square=(mean(a**2,b**2,c**2))**0.5
    return square

def middle_average(a,b,c):
    midavg=median(mean(a,b,c),median(a,b,c),rms(a,b,c))
    return midavg


