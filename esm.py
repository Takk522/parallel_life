from transformers import AutoTokenizer, EsmForProteinFolding

model = EsmForProteinFolding.from_pretrained("facebook/esmfold_v1")
tokenizer = AutoTokenizer.from_pretrained("facebook/esmfold_v1")
print("models have been loaded.")

sequence = "MNLNDILKELK:MNLNDILKELK"
length = len(sequence)
print("the length of sequence is " + str(length))

inputs = tokenizer([sequence], return_tensors="pt", add_special_tokens=False)
outputs = model(**inputs)
folded_positions = outputs.positions
print("position tensor have gianed.")

file_path = "demo.pdb"
content_str = EsmForProteinFolding.infer_pdb(model, sequence)

with open('demo.pdb','w') as f:
    f.writelines(content_str)