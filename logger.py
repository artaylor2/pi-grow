import os
import time

class Logger:
    def __init__(self, config):
        # Create dict of active log files
        self.logfiles = {}

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

        return

    # Logs the content of a dictionary in a file
    #   associated with a given key
    def log(self, key, dict):
        if key in self.logfiles:
            # open log file associated with the given key
            try:
                f =  open(self.logfiles[key], 'a')
        
            # If file does not exist, write headers
            except:
                f =  open(self.logfiles[key], 'w')

                newline = "time"
                for d in dict:
                    newline = newline + self.delim + d

                f.write(newline + "\n")

            # Write new set of field contents 
            newline = time.asctime() 

            for d in dict:
                newline = newline + self.delim + str(dict[d])

            f.write(newline + "\n")

            # Close file
            f.close()
        else:
            print("[Error] Key not found in log dictionary")
        return
