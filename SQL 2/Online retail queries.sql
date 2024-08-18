SELECT * FROM allwellprac.online_retail_ii;

select Customer ID,
Quantity, Price, 
from allwellprac.online_retail_ii
where Price >
(select AvG(Price) FROM allwellprac.online_retail_ii);

SELECT 'Customer ID', Quantity, Price
FROM allwellprac.online_retail_ii
WHERE Price > (SELECT AVG(Price) FROM allwellprac.online_retail_ii);

select  Customer ID, Quantity, Price,Description
FROM allwellprac.online_retail_ii
where price >= 7.95 and Quantity <= 36

select Quantity, Price, country, Round(Quantity*price) as sales from allwellprac.online_retail_ii
having sales>=50 order by Country 

select Quantity, Price, country, Round(Quantity*price) as sales from allwellprac.online_retail_ii
having Quantity>(select avg(Quantity) from allwellprac.online_retail_ii)order by Country 

DELIMITER//
 CREATE PROCEDURE retrieve_all()
 BEGIN
	select * from allwellprac.online_retail_ii;
 END //
 DELIMITER;
 
 DELIMITER @  

CREATE PROCEDURE retrieve_all()  
BEGIN  
    SELECT * FROM allwellprac.online_retail_ii;  
END @

DELIMITER ;

select Price, Quantity,
(Case
	when Quantity >= 36 
	then Quantity * (Price * 0.25)
	else Price*Quantity
    end) as sales 
 from  allwellprac.online_retail_ii
 order by sales Desc
limit 15;
