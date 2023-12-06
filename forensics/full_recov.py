import subprocess

file_name = 'challenge_2.dd'

def run_fls(part, node, isnode): # for init and recursive folder discovery
        if isnode:
                cmd = ['fls', '-o', part, file_name, node] # runs when on a folder
        else:
                cmd = ['fls', '-o', part, file_name] # used for the init run
        out = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = out.stdout
        data = output.split('\n')
        return data

def partions(): # finds each partion
        cmd = ['mmls', file_name]
        out = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = out.stdout
        output = output.split('\n')

        returned = []
        for obj in output:
                if 'Meta' not in obj and '-' not in obj and 'Slot' not in obj and 'GUID' not in obj and 'Off' not in obj and 'Units' not in obj: # removes useless data
                        obj = obj.split('    ')
                        objs = obj[-1].split('   ')
                        if len(objs) > 1:
                                returned.append(objs[1])
        return returned


def icat_data(partion, file):
        file_type = file[-1]
        file_data = file[0].split(':\t')
        file_name = file_data[-1]
        file_node = file_data[0].split('r/r ')
        file_node = file_node[-1].split("* ")
        file_node = file_node[-1]
        return file_name, file_type, file_node, partion

def main(): # main loop
        icat_global = []
        files_global = []
        partion_list = partions()
        fls_local = []

        for partion in partion_list:
                fls_local = run_fls(partion, 0, False)

                for object in fls_local:
                        if "d/d" in object:
                                node = object.split("d/d ")
                                node = node[-1].split(":\t")
                                node.append(partion)
                                files_global.append(node)

                        else:
                                if '.' in object:
                                        file = object.split('.')
                                        if file != ['']:
                                                data = icat_data(partion, file)
                                                icat_global.append(data)

        while files_global:
                save_data = []
                for file in files_global:
                        partion = file[2]
                        node = file[0]
                        fls_local = run_fls(partion, node, True)
                        for object in fls_local:
                                if "d/d" in object:
                                        node = object.split("d/d ")
                                        save_data.append(node[-1])
                                else:
                                        file = object.split('.')
                                        if file != ['']:
                                                file_type = file[-1]
                                                data = icat_data(partion, file)
                                                icat_global.append(data)

                if save_data:
                        files_global = save_data
                else:
                        files_global = []

        if icat_global:
                file_num = 0
                for icat in icat_global:
                        cmd = ['icat', '-r', '-o', icat[3], file_name, icat[2]]
                        out = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                        if out.returncode == 0:

                                file_num += 1
                                with open(f'{icat[0]}:output{file_num}.{icat[1]}', 'wb') as file:
                                        file.write(out.stdout)


main()
