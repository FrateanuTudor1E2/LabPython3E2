import os
def path_dict(fisier):

    try:
        assert(os.path.isfile(fisier)),"The parameter needs to be a file path"
        return {"full_path":os.path.abspath(fisier),
                "file_size":os.path.getsize(fisier),
                "file_extension":os.path.splitext(fisier)[1],
                "can_read":os.access(fisier,os.R_OK),
                "can_write":os.access(fisier,os.W_OK)}
    except Exception as e:
        print(str(e))
        return {}

print(path_dict("C:\\Users\\tudor\\ex7.txt"))