-- 1. Database Setup
CREATE DATABASE quickbite;
USE quickbite;
CREATE TABLE restaurants (
  restaurant_id INT PRIMARY KEY,
  restaurant_name VARCHAR(100),
  cuisine VARCHAR(50),
  city VARCHAR(50),
  rating DOUBLE,
  avg_order_value DOUBLE,
  orders_count INT,
  delivery_fee DOUBLE,
  est_delivery_time INT,
  owner_name VARCHAR(100),
  brand VARCHAR(100)
);

-- 2. Restaurant Dataset — 30 Records
insert into restaurants values(101,"Spice Route","North Indian","Pune",4.5 ,420,18500,39,32,"Amit Sharma","Spice Route");
insert into restaurants values(102,"SouthTiffin House","South Indian","Pune",4.3,260,14300,29,25,"Priya Nair","South Tiffin");
insert into restaurants values(103,"Mumbai Zaika"," Maharashtrian","Mumbai",4.1,350,22000,49,38,"Rohit Patil","Zaika Foods");
insert into restaurants values(104,"Burger Garage","Fast Food","Pune",4.4,10,27500,29,30,"Neha Joshi","Burger Garage");
insert into restaurants values(105,"Pizza Planet","Italian","Mumbai",4.6,520,31000,19,35,"Vikas Mehta","Pizza Planet");
insert into restaurants values(106,"Biryani Junction","Biryani","Hyderabad",4.7,480,42000,29,40,"Arjun Reddy","Biryani Junction");
insert into restaurants values(107,"Chai & Snacks","Cafe","Pune",4.2,180,19500,19,22,"Sneha Kulkarni","Chai & Snacks");
insert into restaurants values(108,"Royal Thali","North Indian","Delhi",4.0,390,16800,39,42,"Manish Gupta","Royal Thali");
insert into restaurants values(109,"Tandoori Tales","Mughlai","Delhi",4.5 ,610 ,12100,59,45,"Karan Singh","Tandoori Tales");
insert into restaurants values(110,"Coastal Curry","Seafood","Goa",4.6,750,9800,69,48,"Riya Fernandes","Coastal Curry");
insert into restaurants values(111,"Green Bowl","Healthy","Bengaluru",4.3,330,11600,39,28,"Ananya Rao","Green Bowl");
insert into restaurants values(112,"Dosa Factory","South Indian","Bengaluru",4.5,240,27800,19,24,"Suresh Kumar","Dosa Factory");
insert into restaurants values(113,"Punjabi Dhaba","Punjabi","Chandigarh",4.1,370,13200,49,40,"Gurpreet Singh","Punjabi Dhaba");
insert into restaurants values(114,"The Wok House","Chinese","Pune","4.4",450,18400,39,36,"Rahul Jain","Wok House");
insert into restaurants values(115,"Sushi Street","Japanese","Mumbai","4.8 ",920,7600,89,50,"Meera Shah","Sushi Street");
insert into restaurants values(116,"Cafe Mocha","Cafe","Pune",4.2,290,15400,29,27,"Ishita Deshmukh","Cafe Mocha");
insert into restaurants values(117,"Street Tadka","Indian","Nagpur",3.9,220,10200,19,35,"Akash Verma","Street Tadka");
insert into restaurants values(118,"Hyderabadi House","Biryani","Hyderabad",4.6,430,35500,29,37,"Faizan Ali","Hyderabadi House");
insert into restaurants values(119,"Pasta Palace","Italian","Bengaluru",4.5,560,10900,49,41,"Nikhil Rao","Pasta Palace");
insert into restaurants values(120,"Sweet Cravings","Desserts","Pune",4.7 ,280 ,20500,19,26,"Pooja Patil","Sweet Cravings");
insert into restaurants values(121,"Kebab Kingdom","Mughlai","Delhi",4.4,530,14100,59,44,"Sameer Khan","Kebab Kingdom");
insert into restaurants values(122,"Taco Town","Mexican","Mumbai",4.2 ,460,8700,49,39,"Kabir Malhotra","Taco Town");
insert into restaurants values(123,"Farm Fresh","Healthy","Pune",4.6,390,12500,29,30,"Rohan Kulkarni","Farm Fres");
insert into restaurants values(124,"Midnight Bites","Fast Food","Pune",4.0,250,24800,39,43,"Tanvi Shah","Midnight Bites");
insert into restaurants values(125,"Kolkata Kitchen","Bengali","Kolkata",4.3,340,11400,39,43,"Soham Sen","Kolkata Kitchen");
insert into restaurants values(126,"Kerala Cafe","South Indian","Kochi",4.5,310,12700,29,31,"Akhil Menon","Kerala Cafe");
insert into restaurants values(127,"Royal Rajputana","Rajasthani","Jaipur",4.7,470,9200,49,46,"Vivek Rathore","Rajputana Foods");
insert into restaurants values(128,"Namma Meals","South Indian","Bengaluru",4.4,275,23900,19,27,"Kavya Shetty","Namma Meals");
insert into restaurants values(129,"Lassi Lab","Beverages","Pune",4.1,160,18200,19,21,"Dev Malhotra","Lassi Lab");
insert into restaurants values(130,"Flame & Grill","BBQ","Mumbai",4.8,880,8300,79,52,"Aditya Kapoor","Flame & Grill");

-- 3.  LEVEL 1 — Food Detective
select * from restaurants where rating > 4.5;
select * from restaurants where avg_order_value < 300;
select * from restaurants where city = "Pune";
select * from restaurants where orders_count > 20000;
select * from restaurants where est_delivery_time > 40;
select * from restaurants where rating between 4.2 and 4.7;
select * from restaurants where cuisine in ("South Indian","Italian","Biryani");
select * from restaurants where owner_name like "%Patil%";
select * from restaurants where restaurant_name = brand; 
select * from restaurants where delivery_fee < 30;

-- 4. n LEVEL 2 — Recommendation Team
select * from restaurants order by orders_count desc limit 5;
select * from restaurants order by orders_count asc limit 5;
select * from restaurants order by rating desc;
select distinct cuisine from restaurants;
select restaurant_name as Restaurant_Name, rating as Customer_Rating from restaurants;
select restaurant_name, owner_name , brand from restaurants;
select * from restaurants order by city asc, rating desc;
select * from restaurants where orders_count > 10000 order by rating desc limit 5;
select * from restaurants where city="Pune" order by orders_count desc limit 3;
select * from restaurants order by delivery_fee desc limit 5;

-- 5. n LEVEL 3 — Find the Hidden Restaurants
select* from restaurants where restaurant_name like "S%";
select* from restaurants where restaurant_name like "%House";
select* from restaurants where restaurant_name like "%Cafe%";
select* from restaurants where cuisine like "%Indian%";
select* from restaurants where char_length(restaurant_name)=5;
select* from restaurants where owner_name like "%Raj%";
select* from restaurants where brand like "%Foods%";
select* from restaurants where city like "P%";

-- 6. n LEVEL 4 — Business Team
select * from restaurants where avg_order_value > 400 and rating > 4.5;
select * from restaurants where orders_count > 20000 or rating > 4.7;
select * from restaurants where city not in ("Pune");
select * from restaurants where est_delivery_time between 25 and 40;
select * from restaurants where avg_order_value between 300 and 600;
select * from restaurants where city ="Pune" or city="Mumbai";
select * from restaurants where cuisine = "Fast Food" and orders_count > 20000;
select * from restaurants where rating > 4.5 and delivery_fee < 40;
select * from restaurants where city ="Bengaluru" and orders_count > 10000;
select * from restaurants where owner_name not in ("Rahul Jain");

-- 7. n LEVEL 5 — Boss Challenges
-- Challenge 1 — Hidden Gem
select * from restaurants where rating > 4.5 and orders_count < 10000;
-- Challenge 2 — Cheap & Popular
select * from restaurants where avg_order_value < 300 and orders_count > 20000;
-- Challenge 3 — Fast Delivery
select * from restaurants where est_delivery_time < 30 and rating > 4.3;
-- Challenge 4 — Trending Restaurants
select * from restaurants where city="Mumbai" order by orders_count desc limit 3;
-- Challenge 5 — Premium Restaurants
select * from restaurants where avg_order_value > (select avg(avg_order_value)from restaurants);
-- Challenge 6 — City Spotlight
select * from restaurants where city="Pune" order by orders_count desc ; 
-- Challenge 7 — Cuisine Report
 select restaurant_name, city, rating, avg_order_value from restaurants where cuisine="South Indian";
-- Challenge 8 — High Value Partners
select * from restaurants where avg_order_value > 500 and rating >=4.5;

-- 8. n FINAL BOSS — CEO Challenge
select restaurant_name, cuisine, city, rating, avg_order_value, orders_count, delivery_fee, owner_name, brand 
from restaurants where
rating > 4.4 
and orders_count > 10000 
and avg_order_value between 300 and 700 
order by orders_count desc limit 5;
