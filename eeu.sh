declare -a path="/lcms/extract/pbTmpData/ENTIREWORLDPLACES/0011229-191225202549706-oozie-oozi-W"

declare -a StringArray=("POL")
declare -a region="EEU"

for country in ${StringArray[@]};
do
  	echo $country;
      #   hadoop fs -copyToLocal $path/extractOut/EEU_201E1/$country ./xml
        python sample.py $country $region
      #   rm -rf ./xml/$country
done

