def xoa_phan_tu(dictionary,key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
    
my_dict = {'a':1,'b':2,'c':3,'d':4}
key_to_del = 'b'
res = xoa_phan_tu(my_dict,key_to_del)
if res:
    print("Phan tu da duoc xoa tu dict:",my_dict)
else:
    print("Khong tim thay phan tu can xoa trong dict")