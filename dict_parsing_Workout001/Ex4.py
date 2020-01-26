l = [
    {
        "color": "red",
        "value": "#f00"
    },
    {
        "color": "green",
        "value": "#0f0"
    },
    {
        "color": "blue",
        "value": "#00f"
    }
]

#Print all the value in the list
#print the hex value of green
#print the hex codes of all colors

for i in range(len(l)):
    print(l[i])
v = "value"
g = "green"
for i in range(len(l)):
    for j in l[i]:
        if v in l[i].keys():
            print("hex value:  ", l[i][v])
            break
        #print(l[i][j])

for i in range(len(l)):
    for j in l[i]:
        if g in l[i].values():
            print("green hex code:  ", l[i][v])
            break
