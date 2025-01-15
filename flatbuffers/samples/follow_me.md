# What is this?
This file record the entire process of how I use flatbuffers.

# Build FlatBuffers Compiler
To use flatc command, under the root directory of flatbuffers project, use the following shell commands to build the flatbuffers compiler:
```sh
cmake -G "Unix Makefiles"
make -j
```
After this, `./flatc` command can be used only under the root directory of flatbuffers project(since the flatc file is in this directory), but `flatc` command is unavailable since the command path is not added to system path.

# Add FlatBuffers to System Path
Modify the bashrc file with `vim ~/.bashrc`, add `export PATH=$PATH:/home/ubuntu/flatbuffers` to the file, execute the bashrc file with `source ~/.bashrc`, now the command `flatc` can be used from any locations.

# Create a schema file
See [players.fbs](./players.fbs)

# Compile the Schema File to the Target Language
## To Python
`flatc --python players.fbs` will generate a Basketball folder at current location, or use `flatc --python -o /path/to/target players.fbs` to generate at another location.

## To Cpp
`flatc --cpp players.fbs` will generate a header file named `players_generated.h`, which warps the code with `namespace Basketball {...}`.

# FlatBuffers Python Library
Before using `import flatbuffers` in Python code, the library need to be installed. The flatbuffers python library is under flatbuffers/python, use `python setup.py install` to install flatbuffers library in current conda env.