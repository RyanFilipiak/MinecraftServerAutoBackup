import os
import datetime
import shutil


def write_file(backup_path, text):
    """Write to file to log it

    Args:
        backup_path (string): path to backup directory
        text (string): text to write
    """
    
    with open(backup_path + "backup-logs.txt", 'a+') as file:
        file.write(text)      
        
    file.close()        



def log_backup(bol, backup_path):
    """Function that logs if the backup was successful

    Args:
        bol (boolean): if backup was successful
        backup_path (string): path to backup folder
    """
    
    date = str(datetime.datetime.now()).split()
    month = date[0] 
    time = date[1][0 : date[1].rfind(":")]
        
    if bol:
        write_file(backup_path, "On {} at {}, the backup was {} \n".format(month, time, "successful"))
    elif bol == False:
        write_file(backup_path, "On {} at {}, the backup {} \n".format(month, time, "failed"))
        

def copy_content(source, dest):
    """Copy the contents from one directory to another

    Args:
        source (string): path to the source file
        dest (string): path to the source file
    """
    
    
    # create title for folder back up based on date
    folder_name = "minecraft-world-backup-{}".format(str(datetime.datetime.now()).split()[0])
    
    # check if folder exists
    if not os.path.exists(dest + folder_name):
        
        # Copy the entire contents of the source folder to the destination folder
        shutil.copytree(source, dest + folder_name)
        log_backup(True, dest)

    else:
        log_backup(False, dest)
    
        
def main():
    
    # CHANGE THIS 
    # source -- the path to the folder of the minecraft world
    # dest -- the path of the save folder for the minecraft world
    source = "C:/..."
    dest = "C:/..."
    
    try:
        # copy contents from one folder to another
        copy_content(source, dest)  
    except:
        log_backup(False, dest)
            



if __name__ == "__main__":
    main()
