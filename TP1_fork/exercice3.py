import os,sys

# EXO 3

N = 4
v=1
while os.fork()==0 and v<=N :   # os.fork() = 0 represents the created child process 
    v += 1
print(v)
sys.exit(0)

# N = 10 : affiche 1 2 .... 10 11 11
# N = 4 : affiche 1 2 3 4 5 5

# EXPLICATION
# 


print("debut")
for i in range(4) :
    pid = os.fork()
    if pid != 0 :      # le père print ok 
        print("Ok !")
    print("Bonjour !")      # le père et le fils print bonjour
sys.exit(0)



# 1 arrière grand père + 4 grand-pères + 6 père + 4 fils + 1 petit fils
# total ! 16
# 15 ok et 29 bonjour