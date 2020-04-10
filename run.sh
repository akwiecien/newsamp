kick_off_date="20200410"
base_path="/lcms/extract/pbTmpData/ENTIREWORLDPLACES/0011229-191225202549706-oozie-oozi-W"            # <- check

# EEU - change true or false if next week EEU is required or not
EEU_todo=true
EEU_path="${base_path}/extractOut/EEU_201E1"                                                          # <- check
EEU_countries=("SVK" "POL")

# WEU
WEU_path="${base_path}/extractOut/WEU_201E1"                                                          # <- check
WEU_countries=("BEL")

if $EEU_todo
then
      for country in ${EEU_countries[@]};
      do
            echo "copyting files: EEU " $country
            hadoop fs -copyToLocal $EEU_path/$country ./xml
            python sample.py $country "EEU" $kick_off_date
            rm -rf ./xml/$country
      done
else
      echo "EEU = skipped"
fi

for country in ${WEU_countries[@]};
do
      echo "copyting files: WEU " $country
      hadoop fs -copyToLocal $WEU_path/$country ./xml
      python sample.py $country "WEU" $kick_off_date
      rm -rf ./xml/$country
done

