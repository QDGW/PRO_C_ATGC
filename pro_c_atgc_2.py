import os
from Bio.Seq import CodonTable

# 获取标准密码子表
standard_table = CodonTable.unambiguous_dna_by_id[1]

# 定义氨基酸短写名称和相应的ATGC编码
aa_code = {"A": "GCT", "R": "CGT", "N": "AAT", "D": "GAT", "C": "TGT",
           "Q": "CAA", "E": "GAA", "G": "GGT", "H": "CAT", "I": "ATT",
           "L": "CTT", "K": "AAA", "M": "ATG", "F": "TTT", "P": "CCT",
           "S": "TCT", "T": "ACT", "W": "TGG", "Y": "TAT", "V": "GTT",
           "\n": ""}

# 目标文件夹路径
folder_path = "X:\working_space"

# 遍历目标文件夹中的所有文件
for file_name in os.listdir(folder_path):
    # 仅处理.txt文件
    if file_name.endswith(".txt"):
        # 读取文件内容并转换为ATGC名称
        with open(os.path.join(folder_path, file_name), "r") as f:
            aa_sequence = f.read().strip()
            dna_sequence = ""
            for aa in aa_sequence:
                dna_sequence += aa_code[aa]
        
        # 将转换后的序列保存为.txt文件
        with open(os.path.join(folder_path, file_name.replace(".txt", "_ATGC.txt")), "w") as f:
            f.write(dna_sequence)