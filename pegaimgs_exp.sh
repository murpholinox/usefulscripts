#!/bin/bash
#
# Pega imágenes desde pH 4 hasta pH 10. Imagen final: 2 filas, 6 columnas.

# 01-12
DATE1=./310322
DATE2=./100422
DATE3=./200422
DATE4=./300422
# 13-16
DATE5=./110422
DATE6=./210422
DATE7=./010522
DATE8=./
# 27-30

cd $DATE3/
for i in `seq -w 01 12`
do
cd $i
# convert jpgs to pngs
for image in *.jpg ;  do convert "$image" "${image%.*}.png" ; done
ls -1 *.png | sed -n '1,12p'  >0112
ls -1 *.png | sed -n '13,24p' >1324
ls -1 *.png | sed -n '25,36p' >2536
ls -1 *.png | sed -n '37,48p' >3748
ls -1 *.png | sed -n '49,60p' >4960
ls -1 *.png | sed -n '61,72p' >6172
LIST1=`cat 0112 | tr '\n' ' '`
LIST2=`cat 1324 | tr '\n' ' '`
LIST3=`cat 2536 | tr '\n' ' '`
LIST4=`cat 3748 | tr '\n' ' '`
LIST5=`cat 4960 | tr '\n' ' '`
LIST6=`cat 6172 | tr '\n' ' '`
montage $LIST1 -tile 6x2 -geometry +1+1 /home/murphy/Documents/montados/${i}/rep_${i}_01.png
montage $LIST2 -tile 6x2 -geometry +1+1 /home/murphy/Documents/montados/${i}/rep_${i}_02.png
montage $LIST3 -tile 6x2 -geometry +1+1 /home/murphy/Documents/montados/${i}/rep_${i}_03.png
montage $LIST4 -tile 6x2 -geometry +1+1 /home/murphy/Documents/montados/${i}/rep_${i}_04.png
montage $LIST5 -tile 6x2 -geometry +1+1 /home/murphy/Documents/montados/${i}/rep_${i}_05.png
montage $LIST6 -tile 6x2 -geometry +1+1 /home/murphy/Documents/montados/${i}/rep_${i}_06.png
cd ..
done
