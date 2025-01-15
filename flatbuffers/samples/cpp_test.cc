#include "include/flatbuffers/flatbuffers.h"
#include "include/torch_generated.h"
#include <iostream> // C++ header file for printing
#include <fstream> // C++ header file for file access


int main() {
    std::ifstream infile;
    infile.open("/home/ubuntu/tutorials/flatbuffers/samples/model.bin", std::ios::binary | std::ios::in);
    infile.seekg(0, std::ios::end);
    int length = infile.tellg();
    infile.seekg(0, std::ios::beg);
    char *data = new char[length];
    infile.read(data, length);
    infile.close();

    auto model = fbs_torch::GetModel(data);
    auto weight = model -> weight();
    auto bias = model -> bias();
    std::cout << "model name: " << model -> name() -> c_str() << std::endl;
    std::cout << "weight name: " << weight -> name() -> c_str() << std::endl;
    std::cout << "bias name: " << bias -> name() -> c_str() << std::endl;
    delete[] data;
    data = nullptr;
    return 0;
}

