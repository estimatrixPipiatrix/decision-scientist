.mode csv
.headers on
.import PS4_GamesSales.csv gameSales
select 
    Game,
    Genre,
    "North America",
    case 
    when "North America" < 2.00 then
	'Low Seller'
    when "North America" between 2.00 and 4.00 then
	'Medium Seller'
    when "North America" > 4.00 then
	'High Seller'
    else 
	'Other'
    end as "Sales Category"
from 
    gameSales
where
    "Sales Category" = "High Seller"
order by
    "North America"
