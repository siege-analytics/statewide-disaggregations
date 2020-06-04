# Disaggregating ACS/ CVAP Data 

## Credits & Acknowledgments

1. Yindra Cotman-Dixon, Blackbox NV
2. Jamaa Bickley-King, [NVM](https://www.newvirginiamajority.org)
3. Julie Goldberg, [Empower Engine](http://wwww.empowerengine.com)
4. Eric Aspengren, [Street Level Strategies](http://streetlevelstrat.com)

## Requirements

1. PostgreSQL
2. Python
    * GeoPandas
    * pysal-tobler
    * psycopg2
    * sqlalchemy
    
## Inputs: 

1. Census CVAP Data 
    * [About CVAP Data](https://www.census.gov/programs-surveys/decennial-census/about/voting-rights/cvap.2018.html)
    * [Direct link to CVAP Data CSV File](https://www2.census.gov/programs-surveys/decennial/rdo/datasets/2018/2018-cvap/CVAP_2014-2018_ACS_csv_files.zip?#)  
2. 2018 Census Shapefiles
    * COUNTY
    * CD 
    * SLDL (State Legislature)
    * SLDU (State Senate)
    * TABBLOCK
    * BG

## How to use this code

I have built a _Makefile_ that has some shortcuts.  Essentially, you are going to use Docker containers to execute Python and PSQL so that you can avoid having to configure both on your computers.

1. Build the containers
    
    ```make build```
    
    ```make up```

2. Ensure that everything is set up correctly in the filesystem
    
    ```make ensure-paths```

3. Get the data from the Census

    ```make fetch-census-shapefiles```
    ```make fetch-census-shapefiles```

4. Load the shapefiles and ACS from the Census

    ```make load-census-shapefiles```
    ```make load-census-acs```

Once these data are in, you can use this the same way you would use any other VM.