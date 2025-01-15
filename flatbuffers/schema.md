# Tables
Tables are the main way of **defining objects** in FlatBuffers, each table contains a name and a list of fields. Each field has a name, a type and a default value(optional).
```Flatbuffers
table Student {
    name:string;
    age:short;
    score:short = 60; // Default value set to 60
    registered:bool = false;
    ...
}
```
Default value: 0 for scalar types; null for other types.

# Structs
Also a way of defining objects, only contain scalars or other structs.  
Advantages over tables: Structs **use less memory** than tables and are even **faster to access**(always stored **in-line** in their parent object, and use no virtual table).
```Flatbuffers
struct Vec3 {
    x:float;
    y:float;
    z:float;
}
```

# Types
## Scalar Types
+ 8 bit: byte(int8), ubyte(uint8), bool
+ 16 bit: short(int16), ushort(uint16)
+ 32 bit: int(int32), uint(uint32), float(float32)
+ 64 bit: long(int64), ulong(uint64), double(float64)  
The alias names can be used in place of type names without affecting code generation, for example *int8* == *byte*, *int16* == *short*, *double* == *float64*.

## Non-scalar Types
+ string

# Array
Array is a **fixed-length** collections of elems, only supported in a struct. The following two structs are binary equivalent:
```Flatbuffers
struct Vec3 {
    x:float;
    y:float;
    z:float;
}

struct Vec3 {
    v:[float:3]; // An array consists of 3 float elems
}
```

# Unions
```Flatbuffers
table PointPosition {
    x:uint; 
    y:uint; 
}
table MarkerPosition {}
union Position {
  Start:MarkerPosition,
  Point:PointPosition,
  Finish:MarkerPosition
}
```

# Namespaces
These will generate the corresponding namespace in C++ for all helper code, and packages in Java. You can use `.` to specify nested namespaces / packages.

# Includes
Include other schemas files in current one:
```Flatbuffers
include "mydefinitions.fbs";
```
This makes it easier to refer to types defined elsewhere.  
**NOTICE:** When using the flatc compiler to generate code for schema definitions, only definitions in the current file will be generated, not those from the included files (those you still generate separately).
```sh
# Compile both fbs files
flatc --python common.fbs main.fbs
```

# Root type
This declares what you consider to be the root table of the serialized data.  
This is particularly important for parsing JSON data.
```Flatbuffers
root_type Player;
```