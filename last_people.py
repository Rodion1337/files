def josephus_survivor(people, step):
	spis = spis0 = []
	step0 = 0


	for i in range(0, people):
		i+=1
		spis.append(i)

	if step==1:
		return(people)

	while len(spis) >1:
		spis0 = spis
		spis2 = josephus_survivor2(spis, step, step0, spis0)
		spis = spis2[0]
		step0 = spis2[1]


	return(spis[0])


def josephus_survivor2(spis, step, step0, spis0):

	del_spis = []
	c = int((len(spis) + step0) // step)  # посчет сколько шт. удалить
	step00 = step0 + (len(spis0) % step)  # подсчет сдвига

	for a in range(1, c + 1):
		del_spis.append((a * step) - step0)
		spis.pop((del_spis[a - 1]) - a)
		a += 1


	else:
		step0 = step00
		if step0 >= step:  # проверка сдвига  на превышения шага выбытия из списка
			step0 -= step



	return(spis, step0)