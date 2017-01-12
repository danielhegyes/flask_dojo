DROP TABLE IF EXISTS "huf_currency"


CREATE TABLE huf_currency (

	id INT PRIMARY KEY,
	company_name VARCHAR(11)
	budget_in_huf VARCHAR(11)
	
);

UPDATE project SET budget_value = (budget_in_huf * 292.25) WHERE budget_currency = ('USD');
UPDATE project SET budget_value = (budget_in_huf * 354.99) WHERE budget_currency = ('GBP');
UPDATE project SET budget_value = (budget_in_huf * 308.5) WHERE budget_currency = ('EUR');


SELECT company_name, budget_value, main_color FROM project ORDER BY budget_value
#COUNTPROBABLYWONTWORKBUTWHATCANYOUDO_and_onlycountsasinglecompany(ifworks):
  SELECT COUNT(company_name) AS KazioProjects FROM project WHERE company_name = "Kazio";


	budget_in_huf INT REFERENCES(50) #CANWEDOTHISLOL?



