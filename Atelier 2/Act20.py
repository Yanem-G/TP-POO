classe_adresse_ip = {
    "192.168.0.1" : "classe C",
    "10.0.0.1" : "classe A",
    "172.16.0.1" : "classe B",
    "200.100.50.1" : "adresse IP publique",
    "169.254.0.1" : "adresse IP de lien local (APIPA)"
}

# en transformant un dictionnaire en une list on obtien une list des clé du dict
adresse_ip= list(classe_adresse_ip)

#Q1

print("la première adresse est ",adresse_ip[0])

#Q2

print("la première adresse est ",adresse_ip[-1])

# Q3

print("la première adresse est ",adresse_ip[2])

# Q4

adresse_ip.append("172.31.0.1")
classe_adresse_ip[adresse_ip[-1]] = "classe B"

#Q5

adresse_ip.remove("200.100.50.1")

#Q6 

print("le nombre d'adresse ip restant est ",len(adresse_ip))

#Q7

if "192.168.0.1" in adresse_ip:
    print("l'adresse 192.168.0.1 est présente dans la list")
else:
    print("l'adresse n'est présente dans la list")

#Q8

print("la classe de l'adresse ip 10.0.0.1 est ",classe_adresse_ip["10.0.0.1"])

#Q9

adresse_ip.sort()
print(adresse_ip)

#Q10
c = 0
for i in adresse_ip:
    if classe_adresse_ip[i] != "classe C":
        print("il existent des adresses n'appartiennent pas a classe C")
        c = 1
        break
if c == 0:
    print("toutes les adresses appartiennent a la classe C")

#Q11
count = 0
for i in adresse_ip:
    if classe_adresse_ip[i] == "adresse IP publique":
        count += 1
print("le nombre d'adresse IP public est ",count)


