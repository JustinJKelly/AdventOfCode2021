f = open('testinput.txt')

m_dec_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

m_bin_to_dec = {
    "0000":"0",
    "0001":"1",
    "0010":"2",
    "0011":"3",
    "0100":"4",
    "0101":"5",
    "0110":"6",
    "0111":"7",
    "1000":"8",
    "1001":"9",
    "1010":"A",
    "1011":"B",
    "1100":"C",
    "1101":"D",
    "1110":"E",
    "1111":"F"
} 

input = ''
for line in f:
    for c in line.strip():
        input += m_dec_to_bin[c]
        
version = input[0:3]
type = input[3:6]

packets = []
i=7
while i+4 < len(input):
    print(i, len(input))
    packets.append(input[i:i+5])
    if input[i] == "0":
        break
    i+=5
        
print(input)
print(version, m_bin_to_dec["0"+version])
print(type, m_bin_to_dec["0"+type])
print(packets)
    

print('Part 1')
print('====================================')
print('Part 2')
