SELECT MEASDATE, ROUND(UNBAL*100,2) AS UNBAL
FROM READINGS WHERE METER_ID = :METERID
ORDER BY MEASDATE DESC 
LIMIT 50;