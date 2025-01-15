import flatbuffers
from Basketball import Player, City, Position, Vec3, Salary, Parameters
import numpy as np
import torch

def save_buf():
    # Create a FlatBuffer builder 
    builder = flatbuffers.Builder(0)

    # Create city table
    city_name = builder.CreateString("Boston") # build string before starting city builder
    zip_code = builder.CreateString("10086")
    City.Start(builder)
    City.AddName(builder, city_name)
    City.AddZipCode(builder, zip_code)
    City.AddPopulation(builder, 14.0001)
    city = City.End(builder)

    # Create param table
    w = torch.randn(224, 224, dtype=torch.float32).flatten().tolist()
    w = builder.CreateNumpyVector(torch.randn(1, 224, dtype=torch.float32).numpy())
    b = builder.CreateNumpyVector(torch.randn(1, 224, dtype=torch.float32).numpy())
    ln = builder.CreateNumpyVector(torch.randn(1, 224, dtype=torch.float32).numpy())
    pos_embed = builder.CreateNumpyVector(torch.randn(1, 224, dtype=torch.float32).numpy())
    Parameters.Start(builder)
    Parameters.AddWeights(builder, w)
    Parameters.AddBiases(builder, b)
    Parameters.AddLayerNorms(builder, ln)
    Parameters.AddPositionEmbeddings(builder, pos_embed)
    param = Parameters.End(builder)

    # Create player table
    player_name = builder.CreateString("Jason")
    nationality = builder.CreateString("US")
    age = 20
    position = Position.Position.PF
    # It's incorrect to create a struct here, then AddPos(pos) later, need to be added inline
    # pos = Vec3.CreateVec3(builder, 0.12, 0.22, 0.89)
    height = 198
    weight = 100
    retired = False
    Player.Start(builder)
    Player.AddName(builder, player_name)
    Player.AddNationality(builder, nationality)
    Player.AddAge(builder, age)
    Player.AddPosition(builder, position)
    Player.AddPos(builder, Vec3.CreateVec3(builder, 0.12, 0.22, 0.89))
    Player.AddHeight(builder, height)
    Player.AddWeight(builder, weight)
    Player.AddCity(builder, city)
    Player.AddRetired(builder, retired)
    Player.AddSalary(builder, Salary.CreateSalary(builder, [18.8, 23.3, 24.5, 28.8, 31.2]))
    Player.AddParam(builder, param)
    player = Player.End(builder)

    # Finish the buffer
    builder.Finish(player)
    buf = builder.Output()

    # Save buf to file
    with open('player.bin', 'wb') as f:
        f.write(buf)

def read_buf():
    # Load the buffer from the file 
    with open('player.bin', 'rb') as f: 
        buf = f.read()

    player = Player.Player.GetRootAsPlayer(buf, 0)
    # Decode string
    player_name = player.Name().decode('utf-8')
    player_age = player.Age()
    position = player.Position()
    pos = player.Pos()
    salary = player.Salary()
    retired = player.Retired()

    city = player.City()
    city_name = city.Name().decode('utf-8')
    city_zip_code = city.ZipCode().decode('utf-8')
    city_population = city.Population()

    param = player.Param()


    print(f"{player_name}, {type(player_name)}")
    print(f"{player_age}, {type(player_age)}")
    print(f"{position}, {type(position)}")
    print(f"{pos}, {type(pos)}")
    print(f"{salary}, {type(salary)}")
    print(f"{retired}, {type(retired)}")
    print(f"{city_name}, {type(city_name)}")
    print(f"{city_zip_code}, {type(city_zip_code)}")
    print(f"{city_population}, {type(city_population)}")
save_buf()