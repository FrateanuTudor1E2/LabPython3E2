import os


def drctr(director):

    try:
        return sorted(list(set([os.path.splitext(el)[1][1:] for el in os.listdir(director) if os.path.isfile(os.path.join(director,el)) and os.path.splitext(el)[1]!=""])))
    except Exception as e:
        print(str(e))
        return []

print(drctr("C:\\Users\\tudor"))