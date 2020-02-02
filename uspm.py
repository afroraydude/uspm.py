#!/usr/bin/env python3
import os
import parser
import config
import json
import sys

origin_dir = os.getcwd()


config = config.getConfig()

def checkDepsAndDl(package):
  installed_packages = parser.getPackages()
  packages = open(package+'/PACKAGEDATA', 'r').read()
  packageData = json.loads(packages)
  for dep in packageData['dependencies']:
    if dep not in installed_packages or not parser.checkVersion(packageData['dependencies'][dep],installed_packages[dep]['version']):
      print(dep + ' is a dependency and is missing, will install')
      install(dep)

def checkDeps(package):
  installed_packages = parser.getPackages()
  packages = open(package+'/PACKAGEDATA', 'r').read()
  packageData = json.loads(packages)
  for dep in packageData['dependencies']:
    deps = ""
    if dep not in installed_packages or not parser.checkVersion(packageData['dependencies'][dep],installed_packages[dep]['version']):
      deps += (dep + ' (missing)')
    else:
      deps += dep
    print(deps)



def uninstall(package):
  os.chdir(config['storage_dir'])
  os.system('sh ./' +package+'/PACKAGECODE uninstall')
  os.system('rm -rf ./'+package)
  parser.removePackage(package)

def install(package):
  os.chdir(config['storage_dir'])
  parser.getPackages()
  if not os.path.exists(sys.argv[2] + '.uspm'):
    download(sys.argv[2])
  os.system('tar xf '+package+'.uspm')
  checkDeps(package)
  os.system('sh ./' +package+'/PACKAGECODE install')
  packages = open(package+'/PACKAGEDATA', 'r').read()
  packageData = json.loads(packages)
  parser.addPackage(package, packageData)

def download(package):
  site = config['mirror']
  package = site+package+'.uspm'
  parser.download(package)

if len(sys.argv) < 3:
  print('No command found')
  sys.exit(0)

if sys.argv[1] == 'install':
  install(sys.argv[2])

elif sys.argv[1] == 'uninstall':
  uninstall(sys.argv[2])

elif sys.argv[1] == 'deps':
  checkDeps(sys.argv[2])

else:
  print('Use install or uninstall command')

