import subprocess

file_name = 'challenge.dd'
cmd = ["fls", file_name]
data_nodes = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
data_nodes = data_nodes.stdout
data_ = data_nodes.split('\n')


def get_files(del_files):
        for obj in data_:
                if '*' in obj:
                        if '.swp' not in obj:
                                del_files.append(obj)
        return del_files

def get_type(del_files):
        types = []
        for obj in del_files:
                obj = obj.split('.')
                file_type = obj[-1]
                types.append(file_type)
        return types

def get_node(obj_):
        obj_ = obj_.split("* ")
        obj_ = obj_[-1].split(":")
        return obj_[0]


def recov_files(file_type, del_files):
        file_num = 0

        for i in range(len(del_files)):
                node = get_node(del_files[i])
                cmd = ['icat', '-r', file_name, node]
                out = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                output = out.stdout

                file_num += 1
                with open(f'output{i}.{file_type[i]}', 'w') as file:
                        file.write(output)
        return file_num

if __name__ == "__main__":
        data = []  
        data_files = get_files(data)
        data_type = get_type(data_files)
        file_num = recov_files(data_type, data_files)

        print("all files found have been recovered")
        print(f"files recoverd: {file_num}")

