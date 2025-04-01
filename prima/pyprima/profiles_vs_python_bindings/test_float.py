import struct
import numpy as np

np.set_printoptions(precision=53, floatmode='fixed', suppress=False)

bin2float = lambda b: struct.unpack('>d', int(b, 2).to_bytes(8, byteorder="big"))[0]
float2bin = lambda f: f'{struct.unpack(">Q", struct.pack(">d", f))[0]:064b}'

simi_bin = [['1011111111000001000100010101001001010100001001001111111001101101','1011111110110010100111001100000010110101010010101000101000001110','0011111111011000000100110110001111000001001110111000111100111100','0000000000000000000000000000000000000000000000000000000000000000','0011111111011110001101100101111010010011011001110111100100101010','0011111111001011011101101011001010010110011101111010000000001101','1011111111100101111110001101101111101111010100011010010010011000','1011111111100101111110001101101111101111010100011010010010011000','1011111111100101111110001101101111101111010100011010010010011000','0011111111010100000011100100100000100001010111001011011011010001','1011111111100101111110001101101111101111010100011010010010011000',],
['0011111111011111100101110111111011100110000101010000100110101011','1011111111100100010000100100011100101010001101100001110111100110','1011111111011101111101111110101001101001011001101000011111111110','0000000000000000000000000000000000000000000000000000000000000000','1011111111101010010010110001100111000001111000101010110011100011','1011111110000001001101100001100101101001101100101101110010100000','0011111111101010100011111111001000100111100010010111100001011010','0011111111101010100011111111001000100111100010010111100001011010','0011111111101010100011111111001000100111100010010111100001011010','0011111111101010100011111111001000100111100010010111100001011010','0011111111101010100011111111001000100111100010010111100001011010',],
['1011111111001001110010110111011011000011000111111111011000011101','1011111111000110001000101100000001110010011000101001110100000101','0011111111111000000111001101010000001100111000101110001101111101','1000000000000000000000000000000000000000000000000000000000000000','0011111111100100000110010010111110101001000001101011010101100001','1011111111101101011000011011001000111011100100101000011110000110','0011111111010010100100010000010100100101000101111010010001001000','0011111111010010100100010000010100100101000101111010010001001000','0011111111010010100100010000010100100101000101111010010001001000','0011111111010010100100010000010100100101000101111010010001001000','0011111111010010100100010000010100100101000101111010010001001000',],
['0011111111101001111100000111001010111011000101001101000000010111','0011111111101000001000001111011010100100000001010010000110111111','1011111111010101110111011100111010000011111010110010100101011100','1011111111110000000000000000000000000000000000000000000000000000','0011111111011110100011000100001100001111000111110011010111101110','1011111111100000001110100101001111011000110100000111100110100100','0011111110011110100001100100101000101000000110111101010110100000','0011111110011110100001100100101000101000000110111101010110100000','0011111110011110100001100100101000101000000110111101010110100000','0011111110011110100001100100101000101000000110111101010110100000','0011111110011110100001100100101000101000000110111101010110100000',],
['1011111111100110000001111000010110111001001101111101010011110110','1011111111100100110001100000010101000101110000100100000111011110','0011111111011011011000110110000010010000011001110100100100100011','0011111111110000000000000000000000000000000000000000000000000000','1011111111101011011101011010110011100010000100000110110001010110','0011111110110000010101100001000011010110000110011101000000110000','1011111111001010010101000101010011100010110010110011011011000011','1011111111001010010101000101010011100010110010110011011011000011','1011111111001010010101000101010011100010110010110011011011000011','1011111111001010010101000101010011100010110010110011011011000011','1011111111001010010101000101010011100010110010110011011011000011',],
['0011111111011010110000010001011010010010111111111000101010010000','0011111111011011111000001001010111011101011101110001101001011110','1011111110111100101110110011110101000011010001001001011100000000','0000000000000000000000000000000000000000000000000000000000000000','0011111111011010101000011010000000001101110101111000101001111001','1011111111010010001000001100111011001110001111111110100111011011','1011111111000001000000011010001001111111001011110100000100111101','1011111111000001000000011010001001111111001011110100000100111101','1011111111000001000000011010001001111111001011110100000100111101','1011111111000001000000011010001001111111001011110100000100111101','1011111111000001000000011010001001111111001011110100000100111101',],
['1011111111001000011100110110000001101000000010001110100110011001','1011111111010111101111010111010110101111001101111110111000001101','1011111110100101001000001010010000010001001000111010000010011011','0000000000000000000000000000000000000000000000000000000000000000','0011111111000111100011000101001111100001100000010110100110011000','0011111110110011010111111000111100110111001011101000000010111001','0011111111100111101100001111100100100000101110011101010110000010','1011111111010000100111100000110110111110100011000101010011111011','1011111111010000100111100000110110111110100011000101010011111011','1011111111010000100111100000110110111110100011000101010011111011','1011111111010000100111100000110110111110100011000101010011111011',],
['1011111110110101000011101001111100010110001100001110100010010000','1011111111001001010000101011101010101010000011001110100100111010','0011111110101011000000001010010111100111011010101000111011110011','0000000000000000000000000000000000000000000000000000000000000000','0011111111001011100111111111001011000011010101000100101011111010','0011111110111010001111010111000001011010000000000010110000110100','1011111111010100010111110101010101111000001010100011000010001011','0011111111100101110100000101010101000011111010101110011110111011','1011111111010100010111110101010101111000001010100011000010001011','1011111111010100010111110101010101111000001010100011000010001011','1011111111010100010111110101010101111000001010100011000010001011',],
['1011111110100000101111001000110000100101100111100011101010111100','1011111110110001110111001011000000110010011000111011111010001100','1011111111000001001110010111001001000001110001000111101011010111','0000000000000000000000000000000000000000000000000000000000000000','0011111110100111001111010100001000001010011011111101011111000110','0011111110011101101010110101011100010000100010000110110000001000','1011111110110011000010010111011011001001010110100000011011100101','1011111110110011000010010111011011001001010110100000011011100101','0011111111101101100111101101000100100110110101001011111100100011','1011111110110011000010010111011011001001010110100000011011100101','1011111110110011000010010111011011001001010110100000011011100101',],
['0011111111100100100110111100000010110100110001010101000001101101','1011111111010101010000001110101000110001010111101101111101010010','0011111111100011011100011011010100110100000100000110010000010001','0000000000000000000000000000000000000000000000000000000000000000','1011111111001110000000000111010000110000001101011011101001010110','0011111111011011111111101110001111101111100110000100101111110111','1011111111001001111111010101001110101110111110101101110110011010','1011111111001001111111010101001110101110111110101101110110011010','1011111111001001111111010101001110101110111110101101110110011010','1011111111001001111111010101001110101110111110101101110110011010','1011111111001001111111010101001110101110111110101101110110011010',],
['0011111110001101111011101011000111001011001011100000001101100110','0011111110001001101011111011101010001110111010001100010001010101','1011111110111011111110101111101110010001000111001001011101111100','0000000000000000000000000000000000000000000000000000000000000000','1011111110100111010100101000000001010100100010100010111001101101','0011111110110001000011000001101110101010011100101110000010100001','1011111110010101100010110110111000000000101101110010010110100110','1011111110010101100010110110111000000000101101110010010110100110','1011111110010101100010110110111000000000101101110010010110100110','1011111110010101100010110110111000000000101101110010010110100110','0011111111101111010100111010010010001111111110100100011011010011',],]

simi = np.zeros((len(simi_bin), len(simi_bin[0])))
for i in range(len(simi_bin)):
    for j in range(len(simi_bin[0])):
        simi[i, j] = bin2float(simi_bin[i][j])

# for i in range(simi.shape[0]):
#     print(repr(simi[i]))

simi = np.random.random((3, 3))

tempsum = -np.sum(simi, axis=0)
mysum = np.zeros(simi.shape[1])
for i in range(simi.shape[1]):
        for j in range(simi.shape[0] - 1, -1, -1):
             mysum[i] += simi[j, i]
        # mysum[i] = -sum(simi[:, i])
print(tempsum + mysum)
# if any(np.abs(tempsum - mysum) > 0):
#     print("abs(tempsum - mysum) > 0")