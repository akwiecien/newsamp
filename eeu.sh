declare -a path="/lcms/extract/pbTmpData/ENTIREWORLDPLACES/0011229-191225202549706-oozie-oozi-W"

declare -a StringArray=("EST")

for country in ${StringArray[@]};
do
  	echo $country;
        hadoop fs -copyToLocal $path/extractOut/EEU_201E1/$country ./xml
        python xml2csv.py $country
        rm -rf ./xml/$country
done

