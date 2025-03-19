alphabetToNumbers = {"A":1, "B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
def calculateIP(rack_label):
    # rack_label[0] = int(rack_label[0])
    rack_label[1] = alphabetToNumbers[rack_label[1].upper()]
    # print(f"Numerical equivalent: {rack_label[1]}")
    decimalEquivalent = int(str(rack_label[0]) + str(rack_label[1]), 8)
    print(f"Octal numeral: {decimalEquivalent}")
    # decimal_equivalent = int(str(octal_numeral), 8)
    last_octet_isp1 = decimalEquivalent * 4
    print(f"ISP1: 172.17.9.{last_octet_isp1}/30")
    multiplied_value = decimalEquivalent * 8
    q = multiplied_value // 256
    r = multiplied_value % 256
    print(f"ISP1: 203.149.{210 + q}.{r}/29")
    print(f"ISP2: 172.17.10.{last_octet_isp1}/30")
    print(f"ISP2: 129.126.{142 + q}.{r}/29")
def calculateAllRack():
    for i in range(1,8):
        for j in range(1,7):
            rack_label = [i,j]
            print(f"Rack {i}{chr(64+j)}")
            calculateIP(list(F"{i}{chr(64+j)}"))
            print("\n")
# rack_label = list(input("Enter your rack label: "))
# calculateIP(rack_label)
calculateAllRack()

#Thanks to the person in rack 3f for the idea of writing this script, however, some should learn to be nice.
#Do validate the output of this script with the output of rackIPCalculator.py