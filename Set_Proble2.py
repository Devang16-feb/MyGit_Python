s = set()
s.add(18)
s.add("18")
# both print as diffrent value
print(s)

s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations? 
print(s)