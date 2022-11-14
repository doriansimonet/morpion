
l=[[1,2,5],[4,5,6],[5,8,9]]
#for i in range(len(l)):
#    for j in range(len(l[i])):
#        print(l[i][j])
#print(l[1][2])

def align(L=[]):
    for i in range(len(L)):
        for j in range(len(L[i])-1):
            if L[j][i] == L[j+1][i] and L[j][i] == L[j+2][i]:
                print("c'est aligné1")
                return True
            if L[j][i] == L[j][i+1] and L[j][i] == L[j][i+2]:
                print("c'est aligné2")
                return True
            if L[j][i] == L[j+1][i+1] and L[j][i] == L[j+2][i+2]:
                print("c'est aligné3")
                return True
            if L[j][i] == L[j-1][i-1] and L[j][i] == L[j-2][i-2]:
                print("c'est aligné4")
                return True
    return False

def aligner(L=[]):
    if L[0][0] == L[0][1] and L[0][0] == L[0][2]:
        print("horizontal1")
        return True
    if L[1][0] == L[1][1] and L[1][0] == L[1][2]:
        print("horizontal2")
        return True
    if L[2][0] == L[2][1] and L[2][0] == L[2][2]:
        print("horizontal3")
        return True
    if L[0][0] == L[1][0] and L[0][0] == L[2][0]:
        print("vertical1")
        return True
    if L[0][1] == L[1][1] and L[0][1] == L[2][1]:
        print("vertical2")
        return True
    if L[0][2] == L[1][2] and L[0][2] == L[2][2]:
        print("vertical3")
        return True
    if L[0][0] == L[1][1] and L[0][0] == L[2][2]:
        print("diagonale1")
        return True
    if L[0][2] == L[1][1] and L[0][2] == L[2][0]:
        print("diagonale2")
        return True
    return False

print(aligner(l))