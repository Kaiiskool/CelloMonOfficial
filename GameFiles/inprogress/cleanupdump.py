import json
#save files below
def save_file():
#to enter a name for your file
#if you don't want to just make it a string
#this is a string
  save_name = input("savename: ")
  #formats the savename you just input into the directory the file is i
  path = 'path_to_dir{0}.json'.format(save_name)
  #stores the savename in the file
  data = {
    'name': save_name
  }
  #drops everything as a json
  with open(path, 'w+') as f:
    json.dump(data, f)

#loadfile
def load_file():
  #loads the savename
  load_name = save_name
  #stores path_two as the location of the save
  path_two = 'path_to_dir{0}.json'.format(load_name)
  #loads it with the name stored in a var called name
  with open(path_two, 'r') as f:
    j = json.load(f)
    name = str(j['name'])