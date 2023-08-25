import os


def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendants."""
    total = os.path.getsize(path)   # account for direct usage

    if os.path.isdir(path):     # if this is a directory
        for filename in os.listdir(path):   # then for each child
            childpath = os.path.join(path, filename)    # compose full path to the child
            total += disk_usage(childpath)  # add childs usage to the total
    
    print('{0:<7}'.format(total), path)     # descriptive output
    return total
            