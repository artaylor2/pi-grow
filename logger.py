import os
import datetime

class Logger:
    def __init__(self, config):
        # Create dict of active log files
        self.logfiles = {}
        self.deltadict = {}
        # Pull format type from config
        #if 'format' in config['logger']:
        #    if config['logger']['format'] is "csv":
        #        self.suffix = '.csv'
        #        self.delim = ','
        #else:
        self.suffix = '.csv'
        self.delim = ','

        # Load keys and make associated file paths
        for c in config['logger']['keys']:
            filepath = "logs/" + str(c) + self.suffix
            self.logfiles.update({c: filepath})
            self.deltadict[c] = "" 
        
        return

    # Logs the content of a dictionary in a file
    #   associated with a given key
    def log(self, key, dict):
        # if key is found and the log values have changed
        if key in self.logfiles and dict is not self.deltadict[key]:
            # open log file associated with the given key
            if os.path.exists(self.logfiles[key]): 
                f =  open(self.logfiles[key], 'a')

            # if file does not exist, create new file and write headers
            else:
                f =  open(self.logfiles[key], 'w')

                newline = "time"

                for d in dict:
                    newline = newline + self.delim + d

                f.write(newline + "\n")

            # Write new set of field contents 
            newline = datetime.datetime.now().isoformat() 

            for d in dict:
                
                newline = newline + self.delim + str(dict[d])

            f.write(newline + "\n")

            # Close file
            f.close()

            # store dict as the new delta
            self.deltadict[key] = dict
            
        else:
            print("[Error] Key not found in log dictionary")
        return
