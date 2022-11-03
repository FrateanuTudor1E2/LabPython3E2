import os

def drf(director, fisier):

    try:
        with open(fisier,"w") as f:
            for el in os.listdir(director):
                name = os.path.join(director,el)
                if os.path.isfile(name) and el.startswith("A"):
                    print(repr(os.path.abspath(name)+os.linesep))
                    f.write(os.path.abspath(name)+os.linesep)
    except Exception as e:
        print(str(e))

print(drf("D:\\SpotifyMusic","SpotifyMusic"))