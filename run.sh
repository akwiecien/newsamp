kick_off_date="20200410"
EEU_to_do=true
base_path="/lcms/extract/pbTmpData/ENTIREWORLDPLACES/0011229-191225202549706-oozie-oozi-W/extractOut"            # <- check
# check hdfs location for point 3 from this confluence page
# https://confluence.in.here.com/display/LCM/Places+XML+Products
mkdir $kick_off_date


# # Big 7 -----------------------------------------------------------------------------------------------------------------------------------------------------------
# BIG7_countries=("AUS" "DEU" "ESP" "GBR" "ITA" "FRA" "USA")
# # BIG7_countries=("ITA")
# for country in ${BIG7_countries[@]};
# do
#       echo "------------------------------------------------------------------------------------------------------------------------------------------------------------"
#       mkdir ./xml/$country
#       num_files=$(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_ | wc -l);
      
#       for file in $(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_);
#       do
#             echo "copy file: BIG7 " $country $file
#             hadoop fs -copyToLocal $file ./xml/$country
#             echo "proc file: BIG7 " $country $file
#             python sample.py $country $num_files
#             rm ./xml/$country/* 
#       done
#       python process.py $country "BIG7" $kick_off_date
#       rm -rf ./xml/$country
# done

# # EEU - change true or false if next week EEU is required or not -------------------------------------------------------------------------------------------------
# EEU_countries=("TUR" "POL" "RUS" "RUM" "GRC" "CHE" "HUN" "HRV" "BGR" "SVK" "KAZ")
# # EEU_countries=("SVK")
# if $EEU_to_do
# then
#       for country in ${EEU_countries[@]};
#       do
#             echo "------------------------------------------------------------------------------------------------------------------------------------------------------------"
#             mkdir ./xml/$country
#             num_files=$(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_ | wc -l);
            
#             for file in $(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_);
#             do
#                   echo "copy file: EEU " $country $file
#                   hadoop fs -copyToLocal $file ./xml/$country
#                   echo "proc file: EEU " $country $file
#                   python sample.py $country $num_files
#                   rm ./xml/$country/* 
#             done
#             python process.py $country "EEU" $kick_off_date
#             rm -rf ./xml/$country
#       done
# else
#       echo "EEU = skipped"
# fi

# # WEU ------------------------------------------------------------------------------------------------------------------------------------------------------------
# WEU_countries=("NLD" "SWE" "BEL" "PRT" "AUT" "DNK" "NOR" "FIN" "CHE" "IRL" "LUX" "MLT" "ISL")
# # WEU_countries=("ISL")
# for country in ${WEU_countries[@]};
# do
#       echo "------------------------------------------------------------------------------------------------------------------------------------------------------------"
#       mkdir ./xml/$country
#       num_files=$(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_ | wc -l);
      
#       for file in $(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_);
#       do
#             echo "copy file: WEU " $country $file
#             hadoop fs -copyToLocal $file ./xml/$country
#             echo "proc file: WEU " $country $file
#             python sample.py $country $num_files
#             rm ./xml/$country/* 
#       done
#       python process.py $country "WEU" $kick_off_date
#       rm -rf ./xml/$country
# done

# # APAC -----------------------------------------------------------------------------------------------------------------------------------------------------------
# APAC_countries=("THA" "IDN" "VNM" "MYS" "PHL" "TWN" "SGP" "HKG" "IND" "BGD" "NPL" "LKA")
# # APAC_countries=("LKA")
# for country in ${APAC_countries[@]};
# do
#       echo "------------------------------------------------------------------------------------------------------------------------------------------------------------"
#       mkdir ./xml/$country
#       num_files=$(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_ | wc -l);
      
#       for file in $(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_);
#       do
#             echo "copy file: APAC " $country $file
#             hadoop fs -copyToLocal $file ./xml/$country
#             echo "proc file: APAC " $country $file
#             python sample.py $country $num_files
#             rm ./xml/$country/* 
#       done
#       python process.py $country "APAC" $kick_off_date
#       rm -rf ./xml/$country
# done
# python apac_join.py $kick_off_date


# North America -----------------------------------------------------------------------------------------------------------------------------------------------------------
NA_countries=("CAN" "BHS" "CYM" "JAM" "VGB")
# NA_countries=("JAM")
for country in ${NA_countries[@]};
do
      echo "------------------------------------------------------------------------------------------------------------------------------------------------------------"
      mkdir ./xml/$country
      num_files=$(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_ | wc -l);
      
      for file in $(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_);
      do
            echo "copy file: NA " $country $file
            hadoop fs -copyToLocal $file ./xml/$country
            echo "proc file: NA " $country $file
            python sample.py $country $num_files
            rm ./xml/$country/* 
      done
      python process.py $country "NA" $kick_off_date
      rm -rf ./xml/$country
done
python na_join.py $kick_off_date

# Latino America -----------------------------------------------------------------------------------------------------------------------------------------------------------
# LAM_countries=("BRA" "MEX" "ARG" "COL" "CHL" "PER" "ECU" "PRY" "PAN" "VEN")
# # LAM_countries=("VEN")
# for country in ${LAM_countries[@]};
# do
#       echo "------------------------------------------------------------------------------------------------------------------------------------------------------------"
#       mkdir ./xml/$country
#       num_files=$(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_ | wc -l);
      
#       for file in $(hadoop fs -ls -R -C $base_path | grep ".*.xml" | grep /$country/$country_);
#       do
#             echo "copy file: LAM " $country $file
#             hadoop fs -copyToLocal $file ./xml/$country
#             echo "proc file: LAM " $country $file
#             python sample.py $country $num_files
#             rm ./xml/$country/* 
#       done
#       python process.py $country "LAM" $kick_off_date
#       rm -rf ./xml/$country
# done
# python lam_join.py $kick_off_date


