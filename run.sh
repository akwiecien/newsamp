kick_off_date="20200410"
EEU_to_do=true
base_path="/lcms/extract/pbTmpData/ENTIREWORLDPLACES/0011229-191225202549706-oozie-oozi-W/extractOut"            # <- check

# EEU - change true or false if next week EEU is required or not -------------------------------------------------------------------------------------------------
EEU_countries=("SVK")
if $EEU_to_do
then
      for country in ${EEU_countries[@]};
      do
            mkdir ./xml/$country
            for file in $(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_);
            do
                  echo "copying files: EEU " $country $file
                  hadoop fs -copyToLocal $file ./xml/$country
            done
            python sample.py $country "EEU" $kick_off_date
            rm -rf ./xml/$country
      done
else
      echo "EEU = skipped"
fi

# WEU ------------------------------------------------------------------------------------------------------------------------------------------------------------
WEU_countries=("BEL")
for country in ${WEU_countries[@]};
do
      mkdir ./xml/$country
      for file in $(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_);
      do
            echo "copying files: WEU " $country $file
            hadoop fs -copyToLocal $file ./xml/$country
      done
      python sample.py $country "WEU" $kick_off_date
      rm -rf ./xml/$country
done

# APAC -----------------------------------------------------------------------------------------------------------------------------------------------------------
APAC_countries=("PHL")
for country in ${APAC_countries[@]};
do
      mkdir ./xml/$country
      for file in $(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_);
      do
            echo "copying files: APAC " $country $file
            hadoop fs -copyToLocal $file ./xml/$country
      done
      python sample.py $country "APAC" $kick_off_date
      rm -rf ./xml/$country
done

