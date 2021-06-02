# -*- coding: utf-8 -*-
#python edit_tag_annotations.py csv_file
import sys
import csv

if __name__ == "__main__":
    args = sys.argv

    csv_file = open(args[1], "r", encoding="ms932", errors="", newline="" )
    cell = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    header = next(cell)

    #split path and tags
    wav_paths = []
    tag_value = []
    for row in cell:
        wav_paths.append(row.pop(0))
        values = []
        for i in range(len(row)):
            values.append(int(row[i]))
        tag_value.append(values)
    
    sum_tag = tag_value[0]
    sum_wav_paths = []
    sum_tags      = []
    output = []
    for i in range(len(wav_paths)):
        if int(i+1) != len(wav_paths):
            if wav_paths[i] == wav_paths[i+1]:
                for j in range(len(sum_tag)):
                    sum_tag[j] += tag_value[i+1][j]
            else:
                sum_tags.append(sum_tag)
                sum_wav_paths.append(wav_paths[i])
                sum_tag = tag_value[i+1]
        else:
            sum_tags.append(sum_tag)
            sum_wav_paths.append(wav_paths[i])

            for j in range(len(sum_wav_paths)):
                row = []
                row.append(sum_wav_paths[j])
                for k in range(len(sum_tags[j])):
                    row.append(sum_tags[j][k])
                output.append(row)
    
    output.insert(0, header)
                

    with open(args[2], 'w') as f:
        writer = csv.writer(f)
        for row in output:
            writer.writerow(row)
