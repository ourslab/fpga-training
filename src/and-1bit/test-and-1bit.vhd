LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.STD_LOGIC_ARITH.ALL;
USE IEEE.STD_LOGIC_UNSIGNED.ALL;

ENTITY TEST_AND_1BIT IS
END TEST_AND_1BIT;

ARCHITECTURE MAIN OF TEST_AND_1BIT IS
  SIGNAL A: STD_LOGIC_VECTOR(0 DOWNTO 0) := (OTHERS => '0');
  SIGNAL B: STD_LOGIC_VECTOR(0 DOWNTO 0) := (OTHERS => '0');
  SIGNAL S: STD_LOGIC_VECTOR(0 DOWNTO 0);
  COMPONENT AND_1BIT IS PORT (
      A: IN  STD_LOGIC_VECTOR(0 DOWNTO 0);
      B: IN  STD_LOGIC_VECTOR(0 DOWNTO 0);
      S: OUT STD_LOGIC_VECTOR(0 DOWNTO 0)
    );
  END COMPONENT;
BEGIN
  MAP_AND_1BIT: AND_1BIT PORT MAP (
    A => A,
    B => B,
    S => S
  );
  PROCESS
  BEGIN
    WAIT FOR 10 NS;
    A <= NOT A;
  END PROCESS;
  PROCESS
  BEGIN
    WAIT FOR 5 NS;
    B <= NOT B;
  END PROCESS;
END MAIN;

