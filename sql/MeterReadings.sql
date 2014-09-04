SELECT MEASDATE, ROUND(V1,1) AS VOLT_A, ROUND(V2,1) AS VOLT_B, ROUND(V3,1) AS VOLT_C, THD1, THD2, THD3, UNBAL
FROM READINGS 
WHERE METER_ID = :METERID
AND MEASDATE BETWEEN :SDATE AND :EDATE
ORDER BY MEASDATE ASC
;