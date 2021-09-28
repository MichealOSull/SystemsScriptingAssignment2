#Micheal O' SUllivan
#R00128516
#Systems Scripting - Assignment 2
#
#The purpose of this task was to write a Python Script that implements the creation of a folder structure. Within this structure we also had to
#create functions which renamed certain files and zipped/archived certain files for the task to be completed. For this task I implemented 4 functions:
#folders() function which was used to create a folder structure, rename() to rename files, zip() to zip file and main() to execute functions.
#
#The first function folders(folderName) was to create a folder structure. For the structure to begin, a user was prompted to enter a name of the folder
#they would like. For the purpose of this submission I have attached the folder along with the tasks and named it: (Task4Folder). If this folder already
#existed, it was removed and replaced.A global path for this folder was created and we then moved within this directory and created two more folders named: #'backup' and 'working'. Global paths were also created for them too. From these two folders we then changed into the working directory and created 3 more #subfolders named: 'pics', 'docs' and 'movies. We printed these folders out to confirm this. We then moved into the docs folder and gave this a global path.
#5 files and 2 folders were created and added within the docs folder.
#
#The second function was to rename the files inside the 'docs' folder. Since we only wanted to change the name of the '.txt' files, we first split these files #into two by name and extension. There were also folders which were not to be changed so to avoid this if the file didn't contain a '.' it was skipped. After #splitting the name of the files into name and extension, we applied the .lower() method to the name and the .upper() method to the extension. We then joined 
#the name and extension back together and printed out the before and after to show that this worked.
#
#The third funciton was the zip function. For this task we were to take the 'docs' folder within the 'working' and archive it while also making 5 backups 
#within the backup folder. To do this we start by using shutil.make_archive() to create an archive of the docs.zip file within the workign directory.
#The ZipFile() function was then used to read the contents of the file and also allows us to print the content. Next within zip() we used shutil.copy to #create a copy of the zip file, but also creating 5 instances of this file. By copying this file we also needed to add a value to chaneg the file name as to #not overwrite it when copying. This was done within the range of (1 , 6) which created 5 copies of the zip file. The contents of one these files was also #read using the ZipFile() function and it's contents were printed to confirm that this worked
#
#The main function was used to execute the other functions.



#Import os, shutil and zipfile modules
import os
import shutil
import zipfile


#Create function for the creation of a folder structure
def folders(folderName):
    dir = os.path.join(folderName)
    if os.path.exists(dir):
        shutil.rmtree(dir)
        print("Folder already existed - removed and replaced!")
    os.mkdir(dir)

    #mainDir directory for the path to the folder created with user input
    global mainDir
    os.chdir(dir)
    mainDir = os.getcwd()


    os.mkdir("backup")
    os.mkdir("working")
    print()
    print("backup and working folder created inside:", dir)
    print()

    #workingDir directory for the path to the folder 'working'
    global workingDir
    os.chdir("working")
    workingDir = os.getcwd()
    
    #backupDir directory for the path to the folder 'backup'
    global backupDir
    os.chdir(mainDir)
    os.chdir("backup")
    backupDir = os.getcwd()
   
    os.chdir(workingDir)
  
    #folders to be created within 'working'
    subfolders = ["pics", "docs", "movies"]
    for folder in subfolders:
        os.mkdir(folder)
        print("Subfolder:", folder, "created in 'working'")
    
    #change directory to docs and create/add the following files and folders
    print()
    os.chdir("docs")
    global docsDir
    docsDir = os.getcwd()
    file = open("CORONAVIRUS.txt", "w")
    file = open("DANGEROUS.txt", "w")
    file = open("KEEPSAFE.txt", "w")
    file = open("STAYHOME.txt", "w")
    file = open("HYGIENE.txt", "w")
    files = os.listdir()
    print("Files added to", docsDir,"-", files)
    print()
    os.mkdir("school")
    os.mkdir("party")


#Create a function to rename the files within the 'docs' folder      
def rename():

    #Split file by name of file and extension to change character case
    docsDir = os.getcwd()
    files = os.listdir(docsDir)
    for f in files:
        if "." not in f:
            continue
        name, ext = f.split('.')
        name = name.lower()
        ext = ext.upper()

        newName=name+"."+ext
        os.rename(f, newName)
        print("Updated file name:", f, "to", newName)
    print()

        

#Create function to archive/zip folder
def zip():
    os.chdir(workingDir)
    shutil.make_archive("docs", "zip", "docs")
    zipDoc = zipfile.ZipFile("docs.zip")
    print("Content of docs.zip: ",zipDoc.namelist())

    #Copy zip file and add to path incrementing it with the range so files don't overwrite
    for i in range(1, 6):
        shutil.copy("docs.zip", os.path.join(backupDir, f"docs{i}.zip"))

    #List files in directory
    files = os.listdir(backupDir)
    print("Content of backup directory: ",files)

    os.chdir(backupDir)
    zipDoc2 = zipfile.ZipFile("docs4.zip")
    print("Content of backup/docs4.zip: ",zipDoc2.namelist())
        
        


#Create main function
def main():
    folderName = input("Enter folder name to be created: ")
    folderName = folders(folderName)
    rename()
    zip()

   

main()

