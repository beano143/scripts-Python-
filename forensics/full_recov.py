import subprocess

file_name = 'challange_2.dd' 

def get_files(obj): #seperates out files from the rest of the outputs 
    if '*' in obj:
        if '.swp' not in obj:
            return obj

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
            print(objs)
                if len(objs) >1:
                    returned.append(objs[1])
    return returned


def main(): # main loop
    icat_global = []
    files_global = []
    partion_list = partions()

    for partion in pation_list:
        fls_local = run_fls(partion, 0, False)
        for object in fls_local:
            obj = object.split(": ")
            if "d/d" in object:
                node = obj[0].split("d/d ")
                files_global.append(node[-1])
            else:
                file = obj.split('.')
                file_type = file[-1]
                icat_files.append(get_files(obj[-1]), partion, file_type)

        
        while files_global:
            save_data = []
            for file in files_global:
                fls_local = run_fls(partion, file, True)
                for object in fls_local:
                    obj = object.split(": ")
                    if "d/d" in object:
                        node = obj[0].split("d/d ")
                        save_data.append(node[-1])
                    else:
                        file = obj.split('.')
                        file_type = file[-1]
                        icat_files.append(get_files(obj[-1]), partion, file_type)
            if save_data:
                files_global = save_data
            else:
                files_global = []

    if icat_global:
        file_num = 0
        for icat in icat_global:
            run = ['icat', '-r', '-o', icat[1], file_name, icat[0]]
            out = subprocess.run(run, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output = out.stdout

            file_num += 1
            with open(f'output{file_num}.{icat[2]}', 'w') as file:
                    file.write(output)
