import math

def left_rotate(x, c):
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

def md5(message):
    # Khởi tạo giá trị ban đầu
    a0 = 0x67452301
    b0 = 0xefcdab89
    c0 = 0x98badcfe
    d0 = 0x10325476

    # Bảng shift (chuẩn MD5)
    s = [
        7,12,17,22, 7,12,17,22, 7,12,17,22, 7,12,17,22,
        5,9,14,20, 5,9,14,20, 5,9,14,20, 5,9,14,20,
        4,11,16,23, 4,11,16,23, 4,11,16,23, 4,11,16,23,
        6,10,15,21, 6,10,15,21, 6,10,15,21, 6,10,15,21
    ]

    # Bảng hằng số K
    K = [int(abs(math.sin(i + 1)) * (2**32)) & 0xFFFFFFFF for i in range(64)]

    # ===== Padding =====
    original_length = len(message) * 8
    message += b'\x80'

    while (len(message) * 8) % 512 != 448:
        message += b'\x00'

    message += original_length.to_bytes(8, 'little')

    # ===== Xử lý từng block =====
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        M = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]

        A, B, C, D = a0, b0, c0, d0

        for i in range(64):
            if i < 16:
                F = (B & C) | ((~B) & D)
                g = i
            elif i < 32:
                F = (D & B) | ((~D) & C)
                g = (5*i + 1) % 16
            elif i < 48:
                F = B ^ C ^ D
                g = (3*i + 5) % 16
            else:
                F = C ^ (B | (~D))
                g = (7*i) % 16

            F = (F + A + K[i] + M[g]) & 0xFFFFFFFF
            A = D
            D = C
            C = B
            B = (B + left_rotate(F, s[i])) & 0xFFFFFFFF

        a0 = (a0 + A) & 0xFFFFFFFF
        b0 = (b0 + B) & 0xFFFFFFFF
        c0 = (c0 + C) & 0xFFFFFFFF
        d0 = (d0 + D) & 0xFFFFFFFF

    return ''.join(x.to_bytes(4, 'little').hex() for x in [a0, b0, c0, d0])

input_string = input("Nhập chuỗi cần băm: ")

import hashlib
print("MD5 hashlib:", hashlib.md5(input_string.encode()).hexdigest())