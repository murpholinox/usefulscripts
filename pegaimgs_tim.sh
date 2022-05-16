#!/bin/bash
#
# Pega fotos, del mismo pozo, tomadas cada n días. Imagen final: 1 fila, 3 columnas.

DATE1=./033122
DATE2=./041022
DATE3=./042122

for i in `seq -w 01 12`
do
for j in `seq 1 72`
do
IMG01=`ls -1 $DATE1/${i} | sed -n ${j},${j}p`
IMG02=`ls -1 $DATE2/${i} | sed -n ${j},${j}p`
IMG03=`ls -1 $DATE3/${i} | sed -n ${j},${j}p`
montage $DATE1/$i/$IMG01 $DATE2/$i/$IMG02 $DATE3/$i/$IMG03 -tile 3x1 -geometry +2+2 /home/murphy/Documents/montados/${i}/${j}.png
done
done

