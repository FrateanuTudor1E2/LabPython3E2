import os
def path_to(my_path):

    if os.path.isfile(my_path):
        with open(my_path,"rb") as f:
            file_size = os.path.getsize(my_path)
            assert(file_size>=20),"File needs to have min 20 chrs"
            f.seek(file_size-20)
            return f.read()
    elif os.path.isdir(my_path):
        lista = {}
        for root, dirs, files in os.walk(my_path):
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext in lista:
                    lista[ext] += 1
                else:
                    lista[ext] = 1
        lista = lista.items()
        return sorted(lista,key=lambda el:el[1],reverse=True)
    else:
        raise Exception("Invalid parameter.")

print(path_to("C:\\Users\\tudor\\ex3.txt"))