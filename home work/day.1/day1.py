#1 davaleba
def find_needle(haystack):
    if "neddle" in haystack:
        return "found the needle at position {}" formart(haystack.index("needle"))
#---------------------------------------------------------------------------------------
#2 davaleba

def invert(list):
    list= []
    for char in list:
        list.append(char * -1)
    return list 
#--------------------------------
#3 davaleba 
def make_upper_case(s):
    return s.upper()
#---------------------------
#4 davaleba
def sum_array(a):
    return sum(a)
#-----------------
#5 davaleba
def are_you_playing_banjo(name):
    if name[0]=="R" or name[0]=="r":
        return name + "plays banjo" 
    else:
        return name + "doesn't play banjo"         