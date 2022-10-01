def validStringShuffleDP(X, Y, shuffle) -> bool:
    dp = {}
    
    # initialize all the alphabets to 0 in a data structure
    for index in range(26):
        dp[ index + ord('A') ] = 0

    # checking if char in X, if yes than updating the value to +1
    for char in X:
        dp[ ord(char) ] += 1

    # checking if char in Y, if yes than updating the value to +1
    for char in Y: 
        dp[ ord(Y) ] += 1
        
    # finding char if char in shuffle and decrementing if char is 

    for char in shuffle:
        dp[ ord(char) ] -= 1

    for i in range(26):
        if( dp[ i + ord('A') ] != 0):
            return False 

    return True
    

if __name__ == '__main__':
    a = "DYNAMIC"
    b = "PROGRAMMING"
    c = "PRODGYRNAMAMMIINCG"
    print(main(a, b, c))