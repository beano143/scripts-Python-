import subprocess

# gets all the disk data and seperates it for ease of access 
file_name = 'challenge.dd'
cmd = ["fls", file_name]
data_nodes = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
data_nodes = data_nodes.stdout
data_ = data_nodes.split('\n')


def get_files(del_files): # gets deleated files; removing swap files, remove if needed
        for obj in data_:
                if '*' in obj:
                        if '.swp' not in obj:
                                del_files.append(obj)
        return del_files

def get_type(del_files): # for each file gets the file type
        types = []
        for obj in del_files:
                obj = obj.split('.')
                file_type = obj[-1]
                types.append(file_type)
        return types

def get_node(obj_): # seperates the node from the files 
        obj_ = obj_.split("* ")
        obj_ = obj_[-1].split(":")
        return obj_[0]


def recov_files(file_type, del_files): # recovers each file with the correct file type from each node 
        for i in range(len(del_files)):
                node = get_node(del_files[i])
                cmd = ['icat', '-r', file_name, node]
                out = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                output = out.stdout
                with open(f'output{i}.{file_type[i]}', 'w') as file:
                        file.write(output)

if __name__ == "__main__": # runs the program 
        data = []
        data_files = get_files(data)
        data_type = get_type(data_files)
        recov_files(data_type, data_files)

        print("all files found have been recovered")
