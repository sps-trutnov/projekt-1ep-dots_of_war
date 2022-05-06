body = [
    (0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), 
    (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), #7
    (0,2), (1,2), (2,2), (3,2), (4,2), (5,2), (6,2), #14
    (0,3), (1,3), (2,3), (3,3), (4,3), (5,3), (6,3), #21
    (0,4), (1,4), (2,4), (3,4), (4,4), (5,4), (6,4), #28
    (0,5), (1,5), (2,5), (3,5), (4,5), (5,5), (6,5), #35
    (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6),
        ]

vyhybky_s = [
    {"pozice":body[10],"stav":False,"hrac":"s","rozcesti":("Z","JZ"),"vybrano":False},
    {"pozice":body[16],"stav":False,"hrac":"s","rozcesti":("JZ","J"),"vybrano":False},
    {"pozice":body[18],"stav":False,"hrac":"s","rozcesti":("Z","J"),"vybrano":False},
    {"pozice":body[25],"stav":False,"hrac":"s","rozcesti":("JZ","J"),"vybrano":False},
    {"pozice":body[26],"stav":False,"hrac":"s","rozcesti":("JZ","J"),"vybrano":False},
            ]
    
vyhybky_j = [
    {"pozice":body[22],"stav":False,"hrac":"j","rozcesti":("S","SV"),"vybrano":False},
    {"pozice":body[23],"stav":False,"hrac":"j","rozcesti":("S","SV"),"vybrano":False}, 
    {"pozice":body[30],"stav":False,"hrac":"j","rozcesti":("S","V"),"vybrano":False},
    {"pozice":body[32],"stav":False,"hrac":"j","rozcesti":("S","SV"),"vybrano":False},
    {"pozice":body[38],"stav":False,"hrac":"j","rozcesti":("SV","V"),"vybrano":False},
            ]

cesty = [
    (body[22], body[15], body[9], body[10]), (body[10], body[12]), #A, B
    (body[16], body[10]), (body[18], body[12]), #C, D
    (body[22], body[16]), (body[23], body[16]), (body[23], body[17], body[18]), (body[25], body[18]), (body[26], body[12]), #E, F, G, H, R
    (body[30], body[23]), (body[30], body[31], body[25]), (body[32], body[25]), (body[32], body[26]), #I, J, K, L
    (body[36], body[22]), (body[36], body[30]), (body[36], body[38]), (body[38], body[32]), (body[38], body[39], body[33], body[26]) #M, N, O, P, Q
        ]

veze_s = [
    {"pozice":((abs(cesty[0][1][0] - cesty[0][2][0])/2) + cesty[0][1][0], (abs(cesty[0][1][1] - cesty[0][2][1])/2) + cesty[0][2][1]),"hrac":"s","hp":1,"vybrano":True}, #A
    {"pozice":((abs(cesty[1][0][0] - cesty[1][1][0])/2) + cesty[1][0][0], (abs(cesty[1][0][1] - cesty[1][1][1])/2) + cesty[1][1][1]),"hrac":"s","hp":1,"vybrano":False}, #B
    {"pozice":((abs(cesty[6][1][0] - cesty[6][2][0])/2) + cesty[6][1][0], (abs(cesty[6][1][1] - cesty[6][2][1])/2) + cesty[6][2][1]),"hrac":"s","hp":1,"vybrano":False}, #G
    {"pozice":((abs(cesty[8][0][0] - cesty[8][1][0])/2) + cesty[8][0][0], (abs(cesty[8][0][1] - cesty[8][1][1])/2) + cesty[8][1][1]),"hrac":"s","hp":1,"vybrano":False}, #R
         ]
    
veze_j = [
    {"pozice":((abs(cesty[10][0][0] - cesty[10][1][0])/2) + cesty[10][0][0], (abs(cesty[10][0][1] - cesty[10][1][1])/2) + cesty[10][1][1]),"hrac":"j","hp":1,"vybrano":False}, #J
    {"pozice":((abs(cesty[13][0][0] - cesty[13][1][0])/2) + cesty[13][0][0], (abs(cesty[13][0][1] - cesty[13][1][1])/2) + cesty[13][1][1]),"hrac":"j","hp":1,"vybrano":False}, #M
    {"pozice":((abs(cesty[15][0][0] - cesty[15][1][0])/2) + cesty[15][0][0], (abs(cesty[15][0][1] - cesty[15][1][1])/2) + cesty[15][1][1]),"hrac":"j","hp":1,"vybrano":False}, #O
    {"pozice":((abs(cesty[17][1][0] - cesty[17][2][0])/2) + cesty[17][1][0], (abs(cesty[17][1][1] - cesty[17][2][1])/2) + cesty[17][2][1]),"hrac":"j","hp":1,"vybrano":False} #Q
         ]

mapa = {"body":body,"vyhybky_s":vyhybky_s,"vyhybky_j":vyhybky_j,"cesty":cesty,"veze_s":veze_s,"veze_j":veze_j}
