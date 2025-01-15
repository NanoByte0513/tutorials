# What is FlatBuffers?
FlatBuffers([GitHub Page](https://github.com/google/flatbuffers), [Tutorials](https://flatbuffers.dev/index.html#flatbuffers_overview), [White paper](https://flatbuffers.dev/flatbuffers_white_paper.html)) is a serialization library that allows us to efficiently store and access structured data. We can use fbs to store and transfer model params, training data, etc. See guidance in [C++](https://flatbuffers.dev/flatbuffers_guide_use_cpp.html) and [Python](https://flatbuffers.dev/flatbuffers_guide_use_python.html).

# Why not Use ProtoBuf?
The primary difference between FlatBuffers and protobuf is that FlatBuffers does not need a **parsing/ unpacking step** to a secondary representation before you can access data, often coupled with per-object memory allocation. The code is an order of magnitude bigger, too.

# A Basic Workflow for Using FlatBuffers
## Step 1: Write a Schema File
First define the data structures we want to serialize using FlatBuffers' **Interface Definition Language (IDL)**, this is the `monster.fbs` file:
```Flatbuffers
namespace MyGame.Sample;

enum Color:byte {
  Red = 0,
  Green,
  Blue = 2
}

table Vec3 {
  x:float;
  y:float;
  z:float;
}

table Monster {
  pos:Vec3;
  mana:short (default=150);
  hp:short (default=100);
  name:string;
  inventory:[ubyte];
  color:Color (default=Blue);
  weapons:[Weapon];
  equipped:Equipment;
  path:[Vec3];
}

table Weapon {
  name:string;
  damage:short;
}

union Equipment {
  Weapon;
}

root_type Monster;

```

## Step 2: Compile the Schema
With a prepared schema file monster.fbs, we can use **flatc** compiler to generate code for the target language, 
### To Generate Cpp Code
```sh
flatc --cpp monster.fbs
```
This will produce a header file **monster_generated.h** and a source file **monster_generated.cpp**
### To Generate Python Code
```sh
flatc --python monster.fbs
```
This will produce a monster directory containing the generated Python files.

## Step 3: Use the Generated Classes in Cpp and Python
```python
import flatbuffers
import Monster

builder = flatbuffers.Builder(0)
monster = Monster.CreateMonster(builder, ...)
builder.Finish(monster)

# Save buffer as a file
buf = builder.Output()
with open("monster.bin", "wb") as f:
  f.write(buf)
```
