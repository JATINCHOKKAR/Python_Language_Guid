from multiprocessing import Pool

def job(i):
	return i*2

if __name__ == '__main__':
	p = Pool(processes=20)
	data = p.map(job, range(20))
	p.close()
	print(data)

