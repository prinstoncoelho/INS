def matrix_creation(key):
    key=key.upper().replace('J','I')
    matrix=[]
    set_=set()
    for char in key:
        if char.isalpha(): 
            if char not in set_:
                matrix.append(char)
                set_.add(char)
    
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in set_:
            matrix.append(char)
            set_.add(char)
    
    return [matrix[i:i+5] for i in range(0,25,5)]

def msg_processing(msg):
    msg=msg.upper().replace('J','I')
    pairs=[]
    l=0
    while(l<len(msg)):
        
        if(l==len(msg)-1):
            pairs.append(msg[l]+"X")
            l=l+1
        elif(msg[l]==msg[l+1]):
            pairs.append(msg[l]+"X")
            l=l+1
        else:
            pairs.append(msg[l]+msg[l+1])
            l=l+2
    return pairs
    
def position_finder(mat,letter):
    
    for i,row in enumerate(mat):
        for j,col in enumerate(row):
            if(letter==col):
                return i,j


msg=input("Enter the msg: ")
key=input("Enter the key: ")
pairs=msg_processing(msg)
mat=matrix_creation(key)

def encryp(mat):
    cipher=""
    for pair in pairs:
        row1,col1=position_finder(mat,pair[0])
        row2,col2=position_finder(mat,pair[1])
        #same row
        if(row1==row2):
            cipher=cipher+(mat[row1][(col1+1)%5])+(mat[row2][(col2+1)%5])
        elif(col1==col2):#same column
            cipher=cipher+(mat[(row1+1)%5][col1])+(mat[(row2+1)%5][col2])
        else:#normal case
            cipher=cipher+(mat[row1][col2])+(mat[row2][col1])
    print(cipher)
encryp(mat)