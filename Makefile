down:
	docker-compose down

up:
	docker-compose up -d

build:
	docker-compose stop
	docker-compose build

# 1
ensure-paths:
	docker-compose exec python \
		python3 python/ensure_paths.py

# 2
fetch-census-shapefiles:
	docker-compose exec python \
		python3 python/fetch_census_shapefiles.py

#3
fetch-census-acs:
	docker-compose exec python \
		python3 python/fetch_census_acs.py

# 4
load-census-shapefiles:
	docker-compose exec python \
		python3 python/load_census_shapefiles.py

# 5
load-census-acs:
	docker-compose exec python \
		python3 python/load_census_acs.py

## 6
#run-jobs:
#	docker-compose exec python \
#		python3 run_jobs.py
#
## 7
#export-shapefiles:
#	docker-compose exec python \
#		python3 export_results.py

