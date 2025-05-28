# Exericio 1 ------> True
A = 10
B = 15
C = 4

if A < B and A < C or C != 0:
    print("A resposta da 1 é: True")
else:
    print("A resposta da 1 é: False")

# Exericio 2 ------> True
A = 10
B = 15
C = 4

if A < B and (A < C or C != 0):
    print("A resposta da 2 é: True")
else:
    print("A resposta da 2 é: False")

# Exericio 3 ------> True
A = 1
B = 9
C = 0

if not (A >= 0 and B == C):
    print("A resposta da 3 é: True")
else:
    print("A resposta da 3 é: False")

# Exericio 4 ------> False
A = 1
B = 9
C = 9

if not (A >= 0) and not (B == C):
    print("A resposta da 4 é: True")
else:
    print("A resposta da 4 é: False")

# Exericio 5 ------> True
A = 1
B = 9
C = 0

if (A >= 0 or B == C) and B > A:
    print("A resposta da 5 é: True")
else:
    print("A resposta da 5 é: False")

# Exericio 6 ------> True
A = 0
B = 1
C = 0

if A == 0 and B != 0 and C == 0:
    print("A resposta da 6 é: True")
else:
    print("A resposta da 6 é: False")

# Exericio 7 ------> True
A = -2
B = 0
C = 2

if not (A <= B) or C > B:
    print("A resposta da 7 é: True")
else:
    print("A resposta da 7 é: False")

# Exericio 8 ------> False
A = -2
B = 0
C = 2

if not (A <= B or C > B):
    print("A resposta da 8 é: True")
else:
    print("A resposta da 8 é: False")

# Exericio 9 ------> False
A = 5
B = 0
C = 0

if A == 0 and B != 0 and C == 0:
    print("A resposta da 9 é: True")
else:
    print("A resposta da 9 é: False")

# Exericio 10 ------> True
A = 5
B = 0
C = 0

if A == 0 or B != 0 or C == 0:
    print("A resposta da 10 é: True")
else:
    print("A resposta da 10 é: False")
