import json
import os

def getConfig():
  if (os.path.exists('config.json')):
    config = open('config.json', 'r').read()
    returnVal = json.loads(config)
    return returnVal
  else:
    config_file = {
      "root_dir":"/var/uspm",
      "storage_dir":"/var/uspm/storage/",
      "mirror":"http://packages.afroraydude.com/uspm/"
      # "config_dir:":"/var/uspm/config"
    }
    jsonFile = json.dumps(config_file)
    f = open('config.json', 'a')
    f.write(jsonFile)
    f.close()
    return config_file