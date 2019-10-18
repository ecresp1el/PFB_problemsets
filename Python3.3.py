#!/usr/bin/env python3

fav_dic = {'book' : 'Jitterbug Perfume',
					 'song' : 'Ludacris ft. T-Pain', 
					 'diva' : 'Beyonce'} 
print (fav_dic)


fav_thing = 'book'
print(fav_dic[fav_thing])

print(fav_dic['diva'])

fav_dic['fav_thing'] = 'organism' 
print(fav_dic['fav_thing']) 


for favthings in fav_dic: 
	seq = fav_dic[favthings]
	print(favthings, seq)

