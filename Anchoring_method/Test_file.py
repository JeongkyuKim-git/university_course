# 전체 염기서열을 한 줄로 변경한다.
def read_file02(file_name):
    data_storege = ""
    with open(file_name, "r", encoding="EUC-kr") as raw_file:
        for line in raw_file:
            data_storege += line.strip()
    return data_storege


def header(file_name):
    with open(file_name) as f1:
        data_storege = ""
        for line in f1:
            if line.startswith('>'):
                header = line
    return header


def seq(file_name):
    with open(file_name) as f1:
        data_storege = ""
        for line in f1:
            if line.startswith('>'):
                header = line
            else:
                data_storege += line.strip()
    return data_storege


file_path = 'Req_01.fasta'
Result = seq(file_path)
# Result = read_file02(file_path)
# print(Result)

length = 20
Call = [Result[i:i+length] for i in range(0, len(Result), length)]

print(" ")
print("--------------------")
print(header(file_path).strip())
print("length = 20", end="")

for x in range(len(Call)):
    input_data = open("split_" + str(x) + ".fasta", "w")
    # input_dat.write(referenceHeader +'\n')
    input_data.write(Call[x])