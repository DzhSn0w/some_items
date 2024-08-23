import os

dir_path = "ceshi"
def change_file_name(dir_path):
    files = os.listdir(dir_path)
    for f in files:
        oldname = os.path.join(dir_path,f)
        newname = os.path.join(dir_path,'rename_'+ f)
        os.rename(oldname,newname)
        print(oldname,"===>",newname)

cname = change_file_name(dir_path)