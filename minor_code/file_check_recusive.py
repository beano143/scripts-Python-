import subprocess
import time

def new_d(): #scans for all files in its local directory, can be changed
    	new_data = subprocess.run(['ls'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    	new_data = new_data.stdout
    	new_data = new_data.split("\n")
    	return new_data
  
try:
      # init directory data
    	old_data = new_d()

      # main loop
    	while True:

            	new_data = new_d()

              # compairs all objects in old data to the most recent check
            	for obj in new_data:
                    	if obj not in old_data:
                            	print(f"new file found: {obj}")

              # updates old data, removes repeating files
            	old_data = new_data
            	time.sleep(10)


except KeyboardInterrupt as e:
    	pass
