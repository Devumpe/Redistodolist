import os
file = open("task.txt","a")
print('please enter a chore or task.')
text = input('')
if(text != ' '): {
	file.write (text+'\n')
	print('Do add list please check Y/N')

	if(Y):
		{
		 print('please enter a chore or task.')
			text = input('')
		if(text != ' '):
			file.write (text+'\n') 
				print('Do add list please check Y/N')
			if(Y):
		{
		 print('please enter a chore or task.')
			text = input('')
		if(text != ' '):
			file.write (text+'\n') 
			
		} else {
			break
		}
		} 
		}

		
file.close()

file = open("task.txt", 'r') 
print(file.read())
