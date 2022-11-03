import os
import sys
def uni_ext():

    try:
        assert(len(sys.argv)>1),"Invalid number of parameters"
        assert(os.path.isdir(sys.argv[1])),"Invalid director"
        return sorted(list(set([os.path.splitext(el)[1][1:] for el in os.listdir(sys.argv[1]) if os.path.isfile(os.path.join(sys.argv[1],el)) and os.path.splitext(el)[1]!=""])))
    except Exception as e:
        print(str(e))
        return []
print(uni_ext())
