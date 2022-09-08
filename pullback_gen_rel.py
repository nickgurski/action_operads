n = 6

generators = []

rel1 = []

rel2 = []

rel3 = []

rel4 = []

rel5 = []

rel6 = []

rel7 = []

rel8 = []

# Produces the list of generators and their duals
for a in ["z", "y"]:
	for i in range(1,n+1):
		generators.append("{}".format(a) + str(i))
		for b in ["z", "y"]:
			for j in range(1,n+1):
				generators.append("{}".format(a) + str(i) + "{}".format(b) + str(j))

# Produces the relations for <x>^{-1} = <x*}
for i in range(1,n+1):
		rel1.append("z" + str(i) + "." + "y" + str(i) + "= 1")

# Produces the relations for <xy>^{-1} = <y*x*>

for a in ["z", "y"]:
	for b in ["z", "y"]:
		for i in range(1,n+1):
			for j in range(1,n+1):
				if a == "z":
					a2 = "y"
				elif a == "y":
					a2 = "z"
				if b == "z":
					b2 = "y"
				elif b == "y":
					b2 = "z"
				rel2.append("{}".format(a) + str(i) + "{}".format(b) + str(j) + "." + "{}".format(b2) + str(j) + "{}".format(a2) + str(i) + "= 1")
				rel5.append("{}".format(a) + str(i) + "{}".format(b) + str(j) + "." + "{}".format(a2) + str(i) + "." + "{}".format(a) + str(i) + "{}".format(b2) + str(j) + "=" + "{}".format(a) + str(i))
				rel3.append("{}".format(a) + str(i) + "{}".format(a2) + str(i) + "= 1")
				rel4.append("{}".format(a) + str(i) + "{}".format(a) + str(i) + "=" + "{}".format(a) + str(i) + "." + "{}".format(a) + str(i))
				rel6.append("{}".format(a) + str(i) + "{}".format(b) +str(j) + "." + "{}".format(a2) + str(i) + "." + "{}".format(b2) + str(j) + "." + "{}".format(b) + str(j) + "{}".format(a) + str(i) + "=" + "{}".format(a) + str(i) + "." + "{}".format(b) + str(j))			
				rel7.append("{}".format(a) + str(i) + "." + "{}".format(b) + str(j) + "=" + "{}".format(b) + str(j) + "{}".format(a) + str(i) + "." + "{}".format(a2) + str(i) + "." + "{}".format(b2) + str(j) + "." + "{}".format(a) + str(i) + "{}".format(b) + str(j))

for a in ["z", "y"]:
	for b in ["z", "y"]:
		for c in ["z", "y"]:
			for i in range(1,n+1):
				for j in range(1,n+1):
					for k in range(1,n+1):
						if a == "z":
							a2 = "y"
						elif a == "y":
							a2 = "z"
						if b == "z":
							b2 = "y"
						elif b == "y":
							b2 = "z"
						if c == "z":
							c2 = "y"
						elif c == "y":
							c2 = "z"
						rel8.append("{}".format(a) + str(i) + "{}".format(b) + str(j) + "." + "{}".format(a2) + str(i) + "." + "{}".format(a) + str(i) + "{}".format(c) + str(k) + "." + "{}".format(a2) + str(i) + "." + "{}".format(c2) + str(k) + "." + "{}".format(b2) + str(j) + "." + "{}".format(b) + str(j) + "{}".format(c) + str(k) + "." + "{}".format(b2) + str(j) + "." + "{}".format(b) + str(j) + "{}".format(a) + str(i) + "." + "{}".format(b2) + str(j) + "." + "{}".format(a2) + str(i) + "." + "{}".format(c2) + str(k) + "." + "{}".format(c) + str(k) + "{}".format(a) + str(i) + "." + "{}".format(c2) + str(k) + "." + "{}".format(c) + str(k) + "{}".format(b) + str(j) + "=" + "{}".format(a) + str(i) + "." + "{}".format(b) + str(j) + "{}".format(c) + str(k))	

# Produces the relations for <xx*> = 1 = <x*x>
# for a in ["z", "y"]:
# 	for i in range(1,n+1):
# 		if a == "z":
# 			a2 = "y"
# 		elif a == "y":
# 			a2 = "z"
# 		rel3.append("{}".format(a) + str(i) + "{}".format(a2) + str(i) + "= 1")
# 		rel4.append("{}".format(a) + str(i) + "{}".format(a) + str(i) + "=" + "{}".format(a) + str(i) + "." + "{}".format(a) + str(i))


print(generators)
print(rel1)
print(len(rel1))
print(rel2)
print(len(rel2))
print(rel3)
print(len(rel3))
print(rel4)
print(len(rel4))
print(rel5)
print(len(rel5))
print(rel6)
print(len(rel6))
print(rel7)
print(len(rel7))
print(rel8)
print(len(rel8))

with open('pullback.txt', 'w') as f:
	f.write("<" + str(', '.join(generators)) + " | "
                + str(', '.join(rel1))
        + str(', ')
	+ str(', '.join(rel2))
        + str(', ')
	+ str(', '.join(rel3))
        + str(', ')
        + str(', '.join(rel4))
        + str(', ')
        + str(', '.join(rel5))
        + str(', ')
        + str(', '.join(rel6))
        + str(', ')
        + str(', '.join(rel7))
        + str(', ')
        + str(', '.join(rel8))
        + ">")
