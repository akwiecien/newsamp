kick_off_date="20200410"
base_path="/lcms/extract/pbTmpData/ENTIREWORLDPLACES/0011229-191225202549706-oozie-oozi-W"            # <- check

# EEU - change true or false if next week EEU is required or not -------------------------------------------------------------------------------------------------
EEU_todo=true
EEU_countries=("HUN" "SVK")
if $EEU_todo
then
      for country in ${EEU_countries[@]};
      do
            mkdir ./xml/$country
            echo "copying files: EEU " $country
            for file in $(hadoop fs -ls -R $base_path | grep .xml | grep $country/$country);
            do
                  hadoop fs -copyToLocal $file ./xml/$country
            done
            # hadoop fs -ls -R $base_path
            # hadoop fs -copyToLocal $EEU_path/$country ./xml
            python sample.py $country "EEU" $kick_off_date
            rm -rf ./xml/$country
      done
else
      echo "EEU = skipped"
fi

# # EEU - change true or false if next week EEU is required or not -------------------------------------------------------------------------------------------------
# EEU_todo=true
# EEU_path="${base_path}/extractOut/EEU_201E1"                                                          # <- check
# EEU_countries=("HUN")
# if $EEU_todo
# then
#       for country in ${EEU_countries[@]};
#       do
#             echo "copying files: EEU " $country
#             hadoop fs -copyToLocal $EEU_path/$country ./xml
#             python sample.py $country "EEU" $kick_off_date
#             rm -rf ./xml/$country
#       done
# else
#       echo "EEU = skipped"
# fi

# # WEU ------------------------------------------------------------------------------------------------------------------------------------------------------------
# WEU_path="${base_path}/extractOut/WEU_201E1"                                                          # <- check
# WEU_countries=("BEL")
# for country in ${WEU_countries[@]};
# do
#       echo "copying files: WEU " $country
#       hadoop fs -copyToLocal $WEU_path/$country ./xml
#       python sample.py $country "WEU" $kick_off_date
#       rm -rf ./xml/$country
# done

# # APAC -----------------------------------------------------------------------------------------------------------------------------------------------------------
# APAC_path="${base_path}/extractOut/APAC_201E0"
# APAC_countries=("PHL")
# for country in ${APAC_countries[@]};
# do
#       echo "copying files: APAC " $country
#       hadoop fs -copyToLocal $APAC_path/$country ./xml
#       python sample.py $country "APAC" $kick_off_date
#       rm -rf ./xml/$country
# done

