LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.STD_LOGIC_ARITH.ALL;
USE IEEE.STD_LOGIC_UNSIGNED.ALL;
 
ENTITY HEX_ENCODE IS
  PORT( 
    I: IN  STD_LOGIC_VECTOR(3 DOWNTO 0);
    O: OUT STD_LOGIC_VECTOR(6 DOWNTO 0)
  );
END HEX_ENCODE;
 
 
ARCHITECTURE MAIN OF HEX_ENCODE IS
BEGIN
  O <= "1000000" WHEN I = "0000" ELSE
       "1111001" WHEN I = "0001" ELSE
       "0100100" WHEN I = "0010" ELSE
       "0110000" WHEN I = "0011" ELSE
       "0011001" WHEN I = "0100" ELSE
       "0010010" WHEN I = "0101" ELSE
       "0000010" WHEN I = "0110" ELSE
       "1111000" WHEN I = "0111" ELSE
       "0000000" WHEN I = "1000" ELSE
       "0010000" WHEN I = "1001" ELSE
       "0001000" WHEN I = "1010" ELSE
       "0000011" WHEN I = "1011" ELSE
       "1000110" WHEN I = "1100" ELSE
       "0100001" WHEN I = "1101" ELSE
       "0000110" WHEN I = "1110" ELSE
       "0001110" WHEN I = "1111" ELSE (OTHERS => '0');
END MAIN;
