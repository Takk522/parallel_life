import torch
import esm
import biotite.structure.io as bsio

model = esm.pretrained.esmfold_v1()
model = model.eval().cuda()
file_path = "original_sequence_list.txt"  
prediction_out = './prediction_out/'

sequences = []
with open(file_path, 'r') as file:
    for line in file:
        sequences.append(line.rstrip())

counter = 1
for sequence in sequences:
    result = prediction_out + str(counter) + ".pdb"
    with torch.no_grad():
        output = model.infer_pdb(sequence)
    with open(result, "w") as f:
        f.write(output)
    struct = bsio.load_structure(result, extra_fields=["b_factor"])
    print(struct.b_factor.mean())  
    counter += 1

