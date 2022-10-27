from random import sample


with open("/homes/dckampherbeek/Desktop/Programmeren/MicroarrayExpression.csv") as micro: 
    Dict_micro = {}
    for line in micro:
        line = line.strip("\n")
        line = line.split(',')
        probe_id = line[0]
        values = line[1:]
        casted_value_list = []
        for value in values:
            casted_value = float(value)
            casted_value_list.append(casted_value)
        average = sum(casted_value_list) / len(casted_value_list)
        Dict_micro.update({probe_id:casted_value})
# #     print(Dict_micro)

probes_same_name= {}

with open("/homes/dckampherbeek/Desktop/Programmeren/Probes.csv") as probes_file:
    for line in probes_file:
        line = line.split(',')
        if line[2] == 'gene_id':
            continue
        elif not line[2] in probes_same_name:
            probes_same_name.setdefault(line[2],[]).append(line[0])
        else: 
            probes_same_name[line[2]].append(line[0])
print (probes_same_name)            

for probes in probes_same_name:
    values = []
    values.append(probes_same_name[probes])
    temp_value = 0
    for value in values:
        if Dict_micro[value] >= temp_value:
            temp_value = Dict_micro[value]
        elif Dict_micro[vlaue] <= temp_value:
            del Dict_micro[value]

with open("/homes/dckampherbeek/Desktop/Programmeren/SampleAnnot.csv") as sample_annotation:
    lmh = {}
    pha = {}
    for line in sample_annotation:
        line = line.strip("/n")
        line = line.split(',')
        regio = line[5]
        probe_id = line[2]
        if regio =='LMH':
            lmh.update({probe_id:regio})
        elif regio == "PHA":
            pha.update({probe_id:regio})    
        else: continue
            
        

        








    

    
