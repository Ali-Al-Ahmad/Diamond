# Diamond
# ----*----
# ---***---
# --*****--
# -*******-
# *********
# -*******-
# --*****--
# ---***---
# ----*----
rows  = int(input("Enter number of rows: "))

# all the patter lines will be 2 times the rows entered by the user
for i in range(1,rows*2):
    
    # each line will have also 2 times the rows entered by the user
    # for the pattern to be symmetrical
    for j in range(1,rows*2):
        # upper part of the pattern
        if j >= rows-i+1 and j <= rows+i-1 and i <= rows:
            print("*", end="")
            
        # lower part of the pattern
        elif j >= i-rows+1 and j <= (rows*2-1)-(i-rows) and i > rows:
            print("*", end="")
            
        else:
            print(" ", end="")
    # jump to new line of the pattern
    print()
