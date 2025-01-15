# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Basketball

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class City(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = City()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCity(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # City
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # City
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # City
    def ZipCode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # City
    def Population(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def CityStart(builder):
    builder.StartObject(3)

def Start(builder):
    CityStart(builder)

def CityAddName(builder, name):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)

def AddName(builder, name):
    CityAddName(builder, name)

def CityAddZipCode(builder, zipCode):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(zipCode), 0)

def AddZipCode(builder, zipCode):
    CityAddZipCode(builder, zipCode)

def CityAddPopulation(builder, population):
    builder.PrependFloat32Slot(2, population, 0.0)

def AddPopulation(builder, population):
    CityAddPopulation(builder, population)

def CityEnd(builder):
    return builder.EndObject()

def End(builder):
    return CityEnd(builder)
