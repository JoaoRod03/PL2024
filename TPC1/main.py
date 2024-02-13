csv = "./emd.csv"

# Leitura do csv

data = []
with open(csv, 'r') as f:
    lines = f.readlines()[1:] 
    for line in lines:
        data.append(line.strip().split(','))

# Lista ordenada alfabeticamente das modalidades desportivas

modalities = set()
for linha in data:
    modalities.add(linha[8]) 
modalities = sorted(modalities)

# Percentagens de atletas aptos e inaptos para a prática desportiva

stats = {'Aptos': 0, 'Inaptos': 0}
for linha in data:
    if linha[12] == 'true':
        stats['Aptos'] += 1
    else:
        stats['Inaptos'] += 1
for key, value in stats.items():
    stats[key] = (value / len(data)) * 100

# Distribuição de atletas por escalão etário

min_age = 100
for linha in data:
    age = int(linha[5])
    agee = int(linha[5])
    if age < min_age:
        min_age = age

age_distribution = {}
for linha in data:
    age = int(linha[5])
    age_adjusted = age - min_age
    age_start = (age_adjusted // 5) * 5 + min_age
    age_end = age_start + 4
    age_group = "[" + str(age_start) + "-" + str(age_end) + "]"
    if age_group in age_distribution:
        age_distribution[age_group] += 1
    else:
        age_distribution[age_group] = 1

age_distribution = dict(sorted(age_distribution.items()))

# Resultados

print("Lista ordenada alfabeticamente das modalidades desportivas:")
for modality in modalities:
    print(modality)

print("\nPercentagens de atletas aptos e inaptos para a prática desportiva:")
for key, value in stats.items():
    print(key + ":", value,"%")

print("\nDistribuição de atletas por escalão etário:")
for age_group, count in age_distribution.items():
    print(age_group + ": " + str(count))

