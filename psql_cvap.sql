CREATE extension IF NOT EXISTS tablefunc;
drop table if exists cit_est_pivot;
drop table if exists cvap_est_pivot;
drop table if exists geo_lookup;

select geoname, geoid into geo_lookup from cvap_master;

SELECT * into cit_est_pivot
FROM crosstab( $$select geoid, lntitle, cit_est from cvap_master order by 1,2
$$)

as cit_est_pivot(geoid varchar(19), "American_Indian_or_Alaska_Native_Alone" numeric,
				"American_Indian_or_Alaska_Native_and_Black_or_African_American" numeric,
				"American_Indian_or_Alaska_Native_and_White" numeric,
				"Asian_Alone" numeric,
				"Asian_and_White" numeric,
				"Black_or_African_American_Alone" numeric,
				"Black_or_African_American_and_White" numeric,
				"Hispanic_or_Latino" numeric,
				"Native_Hawaiian_or_Other_Pacific_Islander_Alone" numeric,
				"Not_Hispanic_or_Latino" numeric,
				"Remainder_of_Two_or_More_Race_Responses" numeric,
				"Total" numeric,
				"White_Alone" numeric);
				
SELECT  * into cvap_est_pivot
FROM crosstab( $$select geoid, lntitle, cvap_est from cvap_master order by 1,2
$$)

as cvap_est_pivot(geoid varchar(19), "American_Indian_or_Alaska_Native_Alone" numeric,
				"American_Indian_or_Alaska_Native_and_Black_or_African_American" numeric,
				"American_Indian_or_Alaska_Native_and_White" numeric,
				"Asian_Alone" numeric,
				"Asian_and_White" numeric,
				"Black_or_African_American_Alone" numeric,
				"Black_or_African_American_and_White" numeric,
				"Hispanic_or_Latino" numeric,
				"Native_Hawaiian_or_Other_Pacific_Islander_Alone" numeric,
				"Not_Hispanic_or_Latino" numeric,
				"Remainder_of_Two_or_More_Race_Responses" numeric,
				"Total" numeric,
				"White_Alone" numeric);				
				
select * 
	

from cit_est_pivot

left join cvap_est_pivot
on cit_est_pivot.geoid = cvap_est_pivot.geoid