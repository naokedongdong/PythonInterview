# -*- coding:utf-8 -*-

file_path = "/Users/Sander/Downloads/map.rar"
def read_file(fpath):
  BLOCK_SIZE = 1024
  with open(fpath, 'rb') as f:
    while True:
      block = f.read(BLOCK_SIZE)
      if block:
        yield block
      else:
        return

for block in read_file(file_path):
  print(block)
