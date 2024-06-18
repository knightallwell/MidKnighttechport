--select*
--from [allwell first practice].dbo.employeedemo
--select jobtitle, salary,
--CASE   
--  WHEN salary > '500000' then 'excecutive'
--  WHEN SALARY BETWEEN 300000 AND 500000 THEN 'MID-LEVEL'
--  ELSE 'LOWER-LEVEL' 
--END
--from [allwell first practice].dbo.employeesalary
--WHERE JOBTITLE <>'TAX ACCOUNTANT'
--ORDER BY salary DESC
----group by stage 

--select*,
--case 
--when salary > 500000 then 'excecutive'
--when salary between 300000 and 500000 then 'mid level'
--else 'lower'
--end as stages,
--case 
--  when jobtitle = 'cyber security speccialist' then salary+(salary*.29)
--   when jobtitle = 'cloud engr' then salary+(salary*.10)
--    when jobtitle = 'software developer' then salary+(salary*.15)
--	 when jobtitle = 'cleaner' then salary+(salary*.05)
--	 else salary+(salary*.03)
--end as salaryraise
--from [allwell first practice].dbo.employeedemo 
--inner join [allwell first practice].dbo.employeesalary
--on employeedemo.employeeID = employeesalary.employeeID
----where jobtitle <> 'tax accountant'
--ORDER BY age desc


----select jobtitle, avg(salary)
----from [allwell first practice].dbo.employeesalary
----group by jobtitle
----having avg(salary)> 500000
----order by jobtitle

--select* 
--from [allwell first practice].dbo.abcdefg
--update [allwell first practice].dbo.abcdefg
--set Postal_Code = '10225'
--where customer_id = 'CR-12730'


----set Postal_Code= '34465'
----where customer_id = 'RH-9495'
----set Postal_Code = '543534'
----where customer_id = 'JM-15655'
----set Postal_Code = '645934'
----where customer_id = 'TS-21340'
----set Postal_Code = '35855'
----where customer_id = 'MB-18085'

--SELECT firstname+ '  ' +lastname AS FULLNAME,gender,age,
--count(gender) over(partition by gender) 
--with cte_employee
--(select firstname,lastname,gender,age,salary, count (salary) over (partition by gender) as totalgender,
--count (age) over (partition by salary) as total_nopaidsal
--FROM [allwell first practice].DBO.employeedemo demo
--inner join [allwell first practice].dbo.employeesalary sal
--on demo.employeeID = sal.employeeID)
--select* 
--from [allwell first practice].dbo.employeesalary

--drop table if exists #temp_employeesal2
--create table #temp_employeesal2
--(employeeID int,
--jobtitle varchar(100),
--salary int)

--select*,
--case
--  when jobtitle = 'cloud engr' then salary+(salary * .03)
--  else salary+(salary*.02)
--end as raise
--from #temp_employeesal2
--order by employeeid asc

--insert into #temp_employeesal2
--select*
--from [allwell first practice].dbo.employeesalary sal
--inner join [allwell first practice].dbo.employeedemo demo
--on demo.employeeID = sal.employeeID

SELECT EMPLOYEEID, SALARY,(SELECT AVG(SALARY)FROM[allwell first practice].DBO.employeesalary) AS AVGSALARY 
FROM [allwell first practice].DBO.employeesalary

