# SONYC-Urban-Sound-Tagging-split

## INSTALL  
Download Dataset -> [SONYC Urban Sound Tagging (SONYC-UST)](https://zenodo.org/record/3966543#.YLetrZP7S-E)  

## PREPARE
Unpack audio-##.tar.gz
```fish
. unpack_audio.sh  
``` 

## RUN
Sum up the ratings of multiple annotators for a single wavfile
```fish
python edit_tag_annotations.py tag_annotations.csv sum_annotations.csv
```

Move the wavfile to folders with a label that has a rating of 3 or higher
```fish
python sonyc_tag_split.py sum_annotations.csv
```
