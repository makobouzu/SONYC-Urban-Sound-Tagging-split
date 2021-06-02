# -*- coding: utf-8 -*-
#python sonyc_tag_split.py csv_file
import os
import sys
import shutil
import csv

def make_folder(path):
    if not os.path.isdir(path):
        os.makedirs(path)

if __name__ == "__main__":
    args = sys.argv

    csv_file = open(args[1], "r", encoding="ms932", errors="", newline="" )
    cell = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    header = next(cell)
    header.pop(0)

    #create tag_folder
    for tag in header:
        make_folder(tag)
    
    #split path and tags
    wav_paths = []
    tag_value = []
    for row in cell:
        wav_paths.append(row.pop(0))
        values = []
        for i in range(len(row)):
            values.append(int(row[i]))
        tag_value.append(values)

    #copy wavfile to including tag
    for i in range(len(wav_paths)):
        for j in range(len(tag_value[i])):
            if tag_value[i][j] >= 3:
                if(os.path.exists(header[j] + "/" + wav_paths[i])):
                    print("already copying")
                    # os.remove("audio/" + wav_paths[i])
                else:
                    shutil.copyfile("audio/" + wav_paths[i], header[j] + "/" + wav_paths[i])
                    print(header[j] + "/" + wav_paths[i])
