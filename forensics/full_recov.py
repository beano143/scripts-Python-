import subprocess

file_name = 'challenge_2.dd' # init variables 
icat_global = []
files_global = []
files_local = []
icat_local = []
returned_folders = []

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


def icat_data(partion, file): # returns data used for the icat command
        file_type = file[-1]
        file_data = file[0].split(':\t')
        file_name = file_data[-1]
        file_node = file_data[0].split('r/r ')
        file_node = file_node[-1].split("* ")
        file_node = file_node[-1]
        return file_name, file_type, file_node, partion

def filtering_data(partion, node, isnode): # used for recursive file checking; filters files and folders
        files = []
        icat = []
        fls_local = run_fls(partion, node, isnode)
        for object in fls_local:
                if "d/d" in object:
                        node = object.split("d/d ")
                        node = node[-1].split(":\t")
                        node.append(partion)
                        files.append(node)
                else:
                        if '.' in object:
                                file = object.split('.')
                                if file != ['']:
                                        data = icat_data(partion, file)
                                        icat.append(data)
        return files, icat

partion_list = partions() # gets the partions of the drive

for partion in partion_list:
        files_local, icat_local = filtering_data(partion, 0, False)
        for file in files_local:
                files_global.append(file)
                returned_folders.append(file[1])
        for icat in icat_local:
                icat_global.append(icat)

while files_global: # runs recusive file discovery
        save_data = [] # any folders found  are put here
        for file in files_global:
                partion = file[2]
                node = file[0]
                files_local, icat_local = filtering_data(partion, node, True)
                for file in files_local:
                        save_data.append(file)
                        returned_folders.append(file[1])
                for icat in icat_local:
                        icat_global.append(icat)
        if save_data:
                files_global = save_data # swaps files_glo for save data; this removes double running and skiping folders 
        else:
                 files_global = [] # this will end the loop

if icat_global: # if there are any files found; save them
        file_num = 0
        for icat in icat_global:
                cmd = ['icat', '-r', '-o', icat[3], file_name, icat[2]]
                out = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                if out.returncode == 0:
                        file_num += 1
                        with open(f'{icat[0]}:output{file_num}.{icat[1]}', 'wb') as file:
                                file.write(out.stdout)

print(f"all folders found have been saved: there were {file_num} files")
print("folders found: ")
print(returned_folders)
