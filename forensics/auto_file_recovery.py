import subprocess

file_name = 'challenge_2.dd'


def get_files(del_files, part):
        for obj in data:
                if '*' in obj:
                        if '.swp' not in obj:
                                del_files.append(obj)
                if 'd/d' in obj:
                        obj.split('d/d')
                        obj = obj[-1].split(': ')
                        node = obj[0]
                        layer_2 = fls_parts(part, True, node)

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

def multi_partions():
        cmd = ['mmls', file_name]
        out = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = out.stdout
        output = output.split('\n')
        returned = []

        for obj in output:
                if 'Meta' not in obj and '-' not in obj and 'Slot' not in obj and 'GUID' not in obj and 'Off' not in obj and 'Units' not in obj:
                        obj = obj.split('    ')
                        objs = obj[-1].split('   ')
                        print(objs)
                        if len(objs) >1:
                                returned.append(objs[1])

        return returned

def fls_parts(part, isnode, node):
        if isnode:
                cmd = ['fls', '-o', part, file_name, node]
        else
                cmd = ['fls', '-o', f"{part}", file_name]
        out = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = out.stdout
        data = output.split('\n')
        return data

def recov_files(file_type, del_files, partions, output_index):
        file_num = 0

        for i in range(len(del_files)):
                node = get_node(del_files[i])
                cmd = ['icat', '-r', file_name, node]
                out = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                output = out.stdout

                file_num += 1

                with open(f'output{output_index+i}.{file_type[i]}', 'w') as file:
                        file.write(output)
        output_index += i
        return file_num, output_index

if __name__ == "__main__":
        indexing = 0

        partions = multi_parttions()
        for partion in partions:
                data = fls_parts(partion)

                data_files = get_files(data, partion)
                data_type = get_type(data_files)
                file_num, indexing = recov_files(data_type, data_files, indexing)


        print("all files found have been recovered")
        print(f"files recoverd: {file_num}")
