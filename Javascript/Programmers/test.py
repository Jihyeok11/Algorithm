d = {
    "k1":1,
    "k2":2,
    "k3":3,
    "k4":4,
    "k5":5,
    "k1":4
}
for key in d:
    print(key,d[key])
print(d.items())
print(d.keys())
for key,value in d.items():
    print(key,value)