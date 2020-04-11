kick_off_date="20200410"
EEU_to_do=true
base_path="/lcms/extract/pbTmpData/ENTIREWORLDPLACES/0011229-191225202549706-oozie-oozi-W/extractOut"            # <- check
mkdir $kick_off_date

# # EEU - change true or false if next week EEU is required or not -------------------------------------------------------------------------------------------------
# EEU_countries=("TUR" "POL" "RUS" "RUM" "GRC" "CHE" "HUN" "HRV" "BGR" "SVK" "KAZ")
# EEU_countries=("SVK")
# if $EEU_to_do
# then
#       for country in ${EEU_countries[@]};
#       do
#             echo "------------------------------------------------------------------------------------------------------------------------------------------------------------"
#             mkdir ./xml/$country
#             for file in $(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_);
#             do
#                   echo "copying files: EEU " $country $file
#                   hadoop fs -copyToLocal $file ./xml/$country
#             done
#             python sample.py $country "EEU" $kick_off_date
#             rm -rf ./xml/$country
#       done
# else
#       echo "EEU = skipped"
# fi

# # WEU ------------------------------------------------------------------------------------------------------------------------------------------------------------
# WEU_countries=("NLD" "SWE" "BEL" "PRT" "AUT" "DNK" "NOR" "FIN" "CHE" "IRL" "LUX" "MLT" "ISL")
# WEU_countries=("ISL")
# for country in ${WEU_countries[@]};
# do
#       echo "------------------------------------------------------------------------------------------------------------------------------------------------------------"
#       mkdir ./xml/$country
#       for file in $(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_);
#       do
#             echo "copying files: WEU " $country $file
#             hadoop fs -copyToLocal $file ./xml/$country
#       done
#       python sample.py $country "WEU" $kick_off_date
#       rm -rf ./xml/$country
# done

# # APAC -----------------------------------------------------------------------------------------------------------------------------------------------------------
# APAC_countries=("THA" "IDN" "VNM" "MYS" "PHL" "TWN" "SGP" "HKG" "IND" "BGD" "NPL" "LKA")
# APAC_countries=("LKA")
# for country in ${APAC_countries[@]};
# do
#       echo "------------------------------------------------------------------------------------------------------------------------------------------------------------"
#       mkdir ./xml/$country
#       for file in $(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_);
#       do
#             echo "copying files: APAC " $country $file
#             hadoop fs -copyToLocal $file ./xml/$country
#       done
#       python sample.py $country "APAC" $kick_off_date
#       rm -rf ./xml/$country
# done
# python apac_join.py $kick_off_date


# # North America -----------------------------------------------------------------------------------------------------------------------------------------------------------
# NA_countries=("CAN" "BHS" "CYM" "JAM" "VGB")
# NA_countries=("JAM")
# for country in ${NA_countries[@]};
# do
#       echo "------------------------------------------------------------------------------------------------------------------------------------------------------------"
#       mkdir ./xml/$country
#       for file in $(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_);
#       do
#             echo "copying files: NA " $country $file
#             hadoop fs -copyToLocal $file ./xml/$country
#       done
#       python sample.py $country "NA" $kick_off_date
#       rm -rf ./xml/$country
# done
# python na_join.py $kick_off_date

# # Latino America -----------------------------------------------------------------------------------------------------------------------------------------------------------
# LAM_countries=("BRA" "MEX" "ARG" "COL" "CHL" "PER" "ECU" "PRY" "PAN" "VEN")
# LAM_countries=("VEN")
# for country in ${LAM_countries[@]};
# do
#       echo "------------------------------------------------------------------------------------------------------------------------------------------------------------"
#       mkdir ./xml/$country
#       for file in $(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_);
#       do
#             echo "copying files: LAM " $country $file
#             hadoop fs -copyToLocal $file ./xml/$country
#       done
#       python sample.py $country "LAM" $kick_off_date
#       rm -rf ./xml/$country
# done
# python lam_join.py $kick_off_date

# Big 7 -----------------------------------------------------------------------------------------------------------------------------------------------------------
BIG7_countries=("AUS" "DEU" "ESP" "GBR" "ITA" "FRA" "USA")
BIG7_countries=("SVK")
for country in ${BIG7_countries[@]};
do
      echo "------------------------------------------------------------------------------------------------------------------------------------------------------------"
      mkdir ./xml/$country
      num_files=$(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_ | wc -l);
      
      for file in $(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_);
      do
            echo "copying files: BIG7 " $country $file
            hadoop fs -copyToLocal $file ./xml/$country
            echo "processing files: BIG7 " $country $file
            python sample.py $country $num_files
            rm ./xml/$country/* 
      done
      python process.py $country "BIG7" $kick_off_date
      rm -rf ./xml/$country
done
