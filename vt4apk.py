# -*- coding: utf-8 -*-

# This is auto script for a lot of file checking.
# This script's output is txt file.

# jinn0525@gmail.com

import sys, os, string, time


def runvt(path):
	files = os.listdir(path)
	wholepath = path.split('/')
	category = wholepath[2]
	category = str(category)
	category = category + ".txt"
	benchmark = time.time()

	for apk in files:
		result_st1 = open(category, 'a')
		sys.stdout.write('...Print ' + apk + '...')
		apk = str(apk)
		result_st1.write(apk + "\n")
		result_st1.close()
		rapk = apk.replace(' ', '\ ')
		rapk = rapk.replace('(', '\(')
		rapk = rapk.replace(')', '\)')
		os.system("python vtlite.py -s " + path + rapk + " >> " + category)
		time2 = time.time()
		result_st2 = open(category, 'a')
		result_st2.write('\n------------------------------------------\n')
		print ('Done.')
		
		if (files.index(apk) % 4 == 3) and ((time2 - benchmark) < 60) :
			print "Sleep %d second..." % (63 - (time2 - benchmark))
			time.sleep(63 - (time2 - benchmark))
			benchmark = time.time()

		result_st2.close()


def main():
	if len(sys.argv) < 2 :
		print "Input argument directory."
		return 0

	print('This script uses public key.')
	runvt(sys.argv[1])


if __name__ == '__main__':
	main()
	sys.exit(0)


# 파일명 프린트 시 filename.decode("UTF-8") 기억하기
