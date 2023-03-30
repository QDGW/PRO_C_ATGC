from Bio.Seq import CodonTable

# 获取标准密码子表
standard_table = CodonTable.unambiguous_dna_by_id[1]

# 定义氨基酸短写名称和相应的ATGC编码
aa_code = {"A": "GCT", "R": "CGT", "N": "AAT", "D": "GAT", "C": "TGT",
           "Q": "CAA", "E": "GAA", "G": "GGT", "H": "CAT", "I": "ATT",
           "L": "CTT", "K": "AAA", "M": "ATG", "F": "TTT", "P": "CCT",
           "S": "TCT", "T": "ACT", "W": "TGG", "Y": "TAT", "V": "GTT"}

# 定义氨基酸序列
aa_sequence = "CAN"

# 将氨基酸序列转换为相应的DNA序列
dna_sequence = ""
for aa in aa_sequence:
    dna_sequence += aa_code[aa]

# 输出DNA序列
print(dna_sequence)