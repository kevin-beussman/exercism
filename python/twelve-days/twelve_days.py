twelve_items = {1:"a Partridge in a Pear Tree.", \
    2:"two Turtle Doves, ", \
    3:"three French Hens, ", \
    4:"four Calling Birds, ", \
    5:"five Gold Rings, ", \
    6:"six Geese-a-Laying, ", \
    7:"seven Swans-a-Swimming, ", \
    8:"eight Maids-a-Milking, ", \
    9:"nine Ladies Dancing, ", \
    10:"ten Lords-a-Leaping, ", \
    11:"eleven Pipers Piping, ", \
    12:"twelve Drummers Drumming, "}

days = {1:"first", \
    2:"second", \
    3:"third", \
    4:"fourth", \
    5:"fifth", \
    6:"sixth", \
    7:"seventh", \
    8:"eighth", \
    9:"ninth", \
    10:"tenth", \
    11:"eleventh", \
    12:"twelfth"}
    
def verse(n):
    v = "On the " + days[n] + " day of Christmas my true love gave to me: "
    for i in range(n, 0, -1):
        if (n >= 2) and (i == 1):
            v += "and "
        v += twelve_items[i]
    return [v]

def recite(start, end):
    vs = []
    for i in range(start, end+1, 1):
        vs += verse(i)
    return vs