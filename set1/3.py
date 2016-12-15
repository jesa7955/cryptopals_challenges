feq = {'w': '0.02360', 'q': '0.00095', 'o': '0.07507', 'x': '0.00150', 'l': '0.04025', 'u': '0.02758', 'n': '0.06749', 'i': '0.06966', 'v': '0.00978', 'k': '0.00772', 'm': '0.02406', 's': '0.06327', 'f': '0.02228', 'y': '0.01974', 'p': '0.01929', 'c': '0.02782', 'z': '0.00074', 'e': '0.12702', 'j': '0.00153', 'g': '0.02015', 'a': '0.08167', 'b': '0.01492', 't': '0.09056', 'd': '0.04253', 'h': '0.06094', 'r': '0.05987'}

def encrypto(cryptoed, key):
    origin = hex(int(cryptoed) ^ int(key))[2:]
    if len(origin) == 1:
        origin = '0' + origin
    hex_char = chr(int(origin, 16))
    return hex_char

def cal_distance(string):
    feq_dict = {}
    temp_str = string.lower()
    temp_list = list(temp_str)
    feq_res = 0.0
    for temp_char in temp_list:
        if temp_char in feq:
            feq_res += abs((temp_list.count(char) / len(temp_list)) - float(feq[temp_char]))
        else:
            feq_res += 1.0
    return feq_res

def handle(string):
    res = []
    char_list = [input_str[index:index+2] for index in range(0, len(input_str)-1, 2)]
    for key in range(256):
        temp_str = ""
        for char in char_list:
            temp_str += encrypto(int(char, 16), key)
        res.append((temp_str, cal_distance(temp_str)))
    res.sort(key=lambda x: x[1])
    print(res[0][0])

input_str = input()
handle(input_str)
