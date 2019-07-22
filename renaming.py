import os

os.chdir('YOUR PATH')

for f in os.listdir():
	file_name, file_ext = os.path.splitext(f)

	file_arr = file_name.split(' - ')

	file_num = file_arr[1][1:].zfill(2)
	file_title = file_arr[2]

	new_name = '{} - {}'.format(file_num, file_title)

	os.rename(f, new_name)





