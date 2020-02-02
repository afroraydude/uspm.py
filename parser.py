import os
import json
import urllib.request

def getPackages():
  if (os.path.exists('packages.json')):
    packages = open('packages.json', 'r').read()
    returnVal = json.loads(packages)
    return returnVal
  else:
    packages_file = {
      "blank": {
        "version":"1.0.0",
        "dependencies":[]
      }
    }
    jsonFile = json.dumps(packages_file)
    f = open('packages.json', 'a')
    f.write(jsonFile)
    f.close()
    return packages_file

def version(package):
  versionStr = package['version'].split('.')
  returnVal = {
    "major": versionStr[0],
    "minor": versionStr[1],
    "build": versionStr[2]
  }
  return returnVal

def checkVersion(minVersion, version):
  versionStr = version.split('.')
  minVersionStr = minVersion.split('.')
  if int(versionStr[0]) >= int(minVersionStr[0]):
    return True
  else:
    return False

  if int(versionStr[1]) >= int(minVersionStr[1]):
    return True
  else:
    return False

  if int(versionStr[2]) >= int(minVersionStr[2]):
    return True
  else:
    return False

def addPackage(package, packageJson):
  packages = open('packages.json', 'r').read()
  packages_file = json.loads(packages)
  packages_file[package] = packageJson
  jsonFile = json.dumps(packages_file)
  f = open('packages.json', 'w')
  f.write(jsonFile)
  f.close()

def removePackage(package):
  packages = open('packages.json', 'r').read()
  packages_file = json.loads(packages)
  del packages_file[package]
  jsonFile = json.dumps(packages_file)
  f = open('packages.json', 'a')
  f.write(jsonFile)
  f.close()

def download(url):
  packageName = url.split('/')[-1]
  urllib.request.urlretrieve(url, './'+packageName)
