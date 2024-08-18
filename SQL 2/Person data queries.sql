SELECT * FROM allwellprac.person;
UPDATE allwellprac.person

SET lastname = 'rohim'
WHERE lastname = 'rojer';

select count(personid) from allwellprac.person where lastname = 'rohim';

alter table allwellprac.person modify personid varchar(20);
alter table  allwellprac.person add column power1001 varchar(20);
insert into allwellprac.person(id,firstname,lastname,country)
values('9bz','allen','tivo','norway');
INSERT INTO allwellprac.person
(id, firstname, lastname, country, power1001)  
VALUES ('9bz', 'allen', 'tivo', 'norway','insane');

select* from allwellprac.person where lastname like'%r'

select * from allwellprac.person where firstname='john' or lastname= 'xavier';
select* from allwellprac.person  where firstname in ('john');

select city, firstname from allwellprac.person where firstname like 'j%' order by 1 desc

select  Ucase(city), count(firstname) from allwellprac.person where city='nigeria' group by city



SELECT firstname, COUNT(city) 
FROM allwellprac.person 
GROUP BY  firstname 
HAVING COUNT(city) > 4;
