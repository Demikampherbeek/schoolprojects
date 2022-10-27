with open(file="/homes/dckampherbeek/Desktop/Programmeren/MicroarrayExpression.csv") as micro:
    count = 0
    highest_avg = 0
    highest_max = 0
    current_probe = ""
    for line in micro:
        line = line.strip("\n")
        line = line.split(',')
        probe_id = line[0]
        rest = line[1:]
        lijst = []
        for value in rest:
            casted_value = float(value)
            lijst.append(casted_value)
            maximum = max(lijst)
            average = sum(lijst) / len(lijst)
            if count < 4:
                count = count + 1
                print("probe_id:", probe_id,"max:",maximum,"avg", average)
    if maximum > highest_max:
        highest_max = maximum
        current_probe = probe_id

                
    if average > highest_avg:
        highest_avg = average
            
    print("highest avg:",highest_avg,"highest max:",highest_max) 

with open(file="/homes/dckampherbeek/Desktop/Programmeren/Probes.csv") as probes:
    for lines in probes:
        lines = lines.strip("\n")
        lines = lines.split(",")
        probe_id = lines[0]
        gen_naam = lines[4]
        if current_probe == probe_id:
            print(gen_naam)
        
        

