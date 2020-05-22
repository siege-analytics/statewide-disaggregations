# Disaggregating ACS/ CVAP Data 

## Credits & Acknowledgments

1. Yindra Cotman-Dixon, Blackbox NV
2. Jamaa Bickley-King, [NVM](https://www.newvirginiamajority.org)
3. Julie Goldberg, [Empower Engine](http://wwww.empowerengine.com)
4. Eric Aspengren 

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

