# 需要pip install transformers datasets，需要有torch或tensorflow
# 修改自：https://huggingface.co/docs/transformers/model_doc/esm#transformers.EsmForProteinFolding
# By guo stone
from transformers import AutoTokenizer, EsmForProteinFolding
path = "/mnt/data/public/ESMFold_huggingface/esmfold_v1/"  # 在@node2上
model = EsmForProteinFolding.from_pretrained(path)  # 加载模型，有warning不用管
tokenizer = AutoTokenizer.from_pretrained(path)

# 下面代码可以得到蛋白的position tensor, [8, 1, L, 14, 3]
inputs = tokenizer(["MLKNVQVQLV"], return_tensors="pt", add_special_tokens=False)  # 输入序列
outputs = model(**inputs)
folded_positions = outputs.positions

# 下面代码可以得到预测结构的pdb文件
file_path = "demo1.pdb"
content_str = EsmForProteinFolding.infer_pdb(model, "MLKNVQVQLV")
with open('demo1.pdb', 'w') as f:
    f.writelines(content_str)
