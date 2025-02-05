LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.STD_LOGIC_ARITH.ALL;
USE IEEE.STD_LOGIC_UNSIGNED.ALL;

ENTITY USING_LED IS
  PORT (
    SW : IN  STD_LOGIC_VECTOR(9 DOWNTO 0);
    LED: OUT STD_LOGIC_VECTOR(9 DOWNTO 0)
  );
END USING_LED;

ARCHITECTURE MAIN OF USING_LED IS
BEGIN
  LED <= SW;
END MAIN;

