#here this approach i am reading text file..
file1 = open('read.txt');
readfilecontent = file1.read(); # here i am reading the text file..
file1.close();
print('reading file from the text file??',readfilecontent);

#here i am writing this file..
file2 = open('read2.txt','w');
file2.write('i am writing this file....');
file2.write('abdul jabir khan');
file2.close();  #here i am closing the file..
print('writing text into the file...??',file2);

#here another approach for opening the file with keyword..
with open('read.txt','r') as readFile:
    read_content = readFile.read();
    print('read_content........))))))))',read_content);

#here current directory........
#python directory and file management..
import os;

print('current working directory...',os.getcwd());



