base_path = 'format.txt'
auto_report = 'reported_TBR.txt'

def gform(file_dir):
        lines = []
        with open(file_dir, 'r') as file:
                for line in file:
                        line_split = line[:-1].split(" ")
                        lines.append(line_split)
        return lines, lines[-1:]

def kform(format):
        items_to_find = ['Domain', 'Key', 'Type']
        positions = {item: [] for item in items_to_find}
        for index, item in enumerate(format[0]):
                print(f"{index}, {item}")
                if item in items_to_find:
                        positions[item].append(index)
        print(positions)
        return positions

def mform(key, data):
        print(key)
        Domain_slot = key['Domain']
        Key_slot = key['Key']
        Type_slot = key['Type']

        vulnerable = ""
        with open (auto_report, 'a') as file:
                for obj in data:
                        domain = obj[Domain_slot[-1]]
                        file.write(f"<FILLER_DATA> {domain}, vulnerable to {vulnerable}")

format, data = gform(base_path)
positions = kform(format)
mform(positions, data)
