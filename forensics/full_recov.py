import subprocess

file_name = 'challange_2.dd'

def get_files(del_files):
        for obj in data:
                if '*' in obj:
                        if '.swp' not in obj:
                                del_files.append(obj)
def get_type(del_files):
        types = []
        for obj in del_files:
                obj = obj.split('.')
                file_type = obj[-1]
                types.append(file_type)
        return types

def run_fls(part, node, is node):
  
