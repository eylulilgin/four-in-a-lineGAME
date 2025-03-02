
def four_in_line(board):
    N=len(board[1])
    for i in range(N):
        for j in range(N):
            
            if board[i][j]=="r" and i+4<=N :
                if board[i+1][j]=="r":
                    if board[i+2][j]=="r":
                        if board[i+3][j]=="r":
                            return "r"
                        break
                        
            if board[i][j]=="r" and j+4<=N:
                if board[i][j+1]=="r":
                    if board[i][j+2]=="r":
                        if board[i][j+3]=="r":
                            return "r"
                        break
                if board[i][j+1]=="r":
                    if board[i][j+2]=="r":
                        if board[i][j+3]=="r":
                            return "r"
                 
            if board[i][j]=="r" and i+4<=N and j+4<=N:
                if board[i+1][j+1]=="r":
                    if board[i+2][j+2]=="r":
                        if board[i+3][j+3]=="r":
                            return "r"   
                        break
                        
            if board[i][j]=="r" and i+4<=N:
                if board[i+1][j-1]=="r":
                    if board[i+2][j-2]=="r":
                        if board[i+3][j-3]=="r":
                            return "r"    
                        break
                        
            if board[i][j]=="y" and i+4<=N:
                if board[i+1][j]=="y":
                    if board[i+2][j]=="y":
                        if board[i+3][j]=="y":
                            return "y"
                        break
            
            if board[i][j]=="y" and j+4<=N:
                if board[i][j+1]=="y":
                    if board[i][j+2]=="y":
                        if board[i][j+3]=="y":
                            return "y"
                        break
                 
            if board[i][j]=="y" and i+4<=N and j+4<=N:
                if board[i+1][j+1]=="y":
                    if board[i+2][j+2]=="y":
                        if board[i+3][j+3]=="y":
                            return "y"   
                        break
                        
            if board[i][j]=="y" and i+4<=N:
                if board[i+1][j-1]=="y":
                    if board[i+2][j-2]=="y":
                        if board[i+3][j-3]=="y":
                            return "y"    
                        break
                         
            
    

        

def main():
    '''
    You can test your four_in_line implementation using the function calls here.
    These function calls are here only to help you test your function.
    What matters is whether your four_in_line function is correct.
    '''
    
    board1 = [['.',  '.',  '.',  '.', '.'],
             ['.',  'r',  '.',  'y', '.'],
             ['.',  'r',  '.',  'r', '.'],
             ['.',  'r',  'y',  'y', '.'],
             ['y',  'r',  'r',  'y', 'y']]
    print(four_in_line(board1))

 
    board2 = [['.',  '.',  '.',  '.', '.', '.'],
             ['.',  '.',  '.',  '.', '.', '.'],
             ['y',  '.',  '.',  'r', '.', '.'],
             ['r',  '.',  'r',  'r', '.', '.'],
             ['r',  '.',  'r',  'y', 'y', 'y'],
             ['r',  'y',  'y',  'y', 'y', 'r']]
    print(four_in_line(board2))

    
    board3 = [['r',  '.',  '.',  '.'],
             ['y',  'r',  '.',  '.'],
             ['y',  'y',  'r',  'r'],
             ['y',  'y',  'r',  'r']]
    print(four_in_line(board3))


    board4 = [['.',  'r',  '.',  '.', '.'],
             ['.',  'r',  'r',  'y', 'y'],
             ['.',  'r',  'y',  'y', 'r'],
             ['r',  'y',  'y',  'y', 'r'],
             ['r',  'y',  'r',  'r', 'y']]
    print(four_in_line(board4))
    
    
    board5 = [['.',  '.',  '.',  '.', '.'],
             ['.',  '.',  '.',  'r', '.'],
             ['.',  '.',  'y',  'y', 'r'],
             ['.',  'r',  'y',  'y', 'r'],
             ['r',  'y',  'r',  'y', 'y']]
    print(four_in_line(board5))
    
    
    board6 = [['.',  'r',  '.',  '.', '.', '.'],
             ['.',  'r',  'r',  '.', '.', '.'],
             ['y',  'y',  '.',  'r', '.', '.'],
             ['r',  'y',  'r',  'r', 'r', '.'],
             ['y',  'r',  'r',  'y', 'y', 'y'],
             ['r',  'y',  'y',  'y', 'r', 'y']]
    print(four_in_line(board6))
    
    
################################################################ 
'''
DO NOT EDIT BELOW THIS LINE
'''
main()
