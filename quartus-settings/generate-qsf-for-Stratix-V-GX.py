#! /usr/bin/python3

TOP_LEVEL_ENTITY = "TOP"
CHIP_SELECT="Stratix V GX"
#CHIP_SELECT="MAX V CPLD"

def print_sstl1p5(name, location):
  print(f"set_location_assignment PIN_{location} -to {name}")
  print(f"set_instance_assignment -name IO_STANDARD \"SSTL-15 CLASS I\" -to {name}")
def print_diff1p5(name, location):
  print(f"set_location_assignment PIN_{location} -to {name}")
  print(f"set_instance_assignment -name IO_STANDARD \"DIFFERENTIAL 1.5-V SSTL CLASS I\" -to {name}")
def print_1p8(name, location):
  print(f"set_location_assignment PIN_{location} -to {name}")
  print(f"set_instance_assignment -name IO_STANDARD \"1.8 V\" -to {name}")
def print_2p5(name, location):
  print(f"set_location_assignment PIN_{location} -to {name}")
  print(f"set_instance_assignment -name IO_STANDARD \"2.5 V\" -to {name}")
def print_diff2p5(name, location):
  print(f"set_location_assignment PIN_{location} -to {name}")
  print(f"set_instance_assignment -name IO_STANDARD \"DIFFERENTIAL 2.5-V SSTL CLASS II\" -to {name}")
def print_3p3(name, location):
  print(f"set_location_assignment PIN_{location} -to {name}")
  print(f"set_instance_assignment -name IO_STANDARD \"3.3 V\" -to {name}")
def print_lvttl3p3(name, location):
  print(f"set_location_assignment PIN_{location} -to {name}")
  print(f"set_instance_assignment -name IO_STANDARD \"3.3-V LVTTL\" -to {name}")
def print_lvds(name, location):
  print(f"set_location_assignment PIN_{location} -to {name}")
  print(f"set_instance_assignment -name IO_STANDARD \"LVDS\" -to {name}")

def print_device():
  print(f"#============================================================")
  print(f"# Device")
  print(f"#============================================================")
  if CHIP_SELECT == "Stratix V GX":
    print(f"set_global_assignment -name FAMILY \"Stratix V\"")
    print(f"set_global_assignment -name DEVICE 5SGXEA7K2F40C")
    print(f"set_global_assignment -name TOP_LEVEL_ENTITY {TOP_LEVEL_ENTITY}")
    print(f"set_global_assignment -name PROJECT_OUTPUT_DIRECTORY output_files")
    print(f"set_global_assignment -name EDA_SIMULATION_TOOL \"ModelSim-Altera (VHDL)\"")
print_device()

def print_clock():
  print(f"#============================================================")
  print(f"# CLOCK")
  print(f"#============================================================")
  if CHIP_SELECT == "Stratix V GX":
    print_1p8 ("CLKIN_50"     , "AN6")
    print_lvds("REFCLK1_QL0_P", "AD33")
    print_lvds("REFCLK1_QL0_N", "AD34")
    print_lvds("CLKINBOT_P0"  , "AH22")
    print_lvds("CLKINBOT_N0"  , "AJ22")
    print_lvds("CLKINTOP_P0"  , "J23")
    print_lvds("CLKINTOP_N0"  , "J24")
    print_lvds("REFCLK4_QR2_P", "V6")
    print_lvds("REFCLK4_QR2_N", "V5")
    print_lvds("CLK_125_P"    , "AV29")
    print_lvds("CLK_125_N"    , "AW29")
print_clock()

def print_reset():
  print(f"#============================================================")
  print(f"# RESET")
  print(f"#============================================================")
  if CHIP_SELECT == "Stratix V GX":
    print_2p5("CPU_RESETn", "AM34")
print_reset()

def print_flash():
  print(f"#============================================================")
  print(f"# FLASH MEMORY")
  print(f"#============================================================")
  if CHIP_SELECT == "Stratix V GX":
    print_1p8("FLASH_ADVn"    , "AP7")
    print_1p8("FLASH_CEn0"    , "AV14")
    print_1p8("FLASH_CEn1"    , "AW13")
    print_1p8("FLASH_CLK"     , "AM8")
    print_1p8("FLASH_OEn"     , "AJ7")
    print_1p8("FLASH_RDYBSYN0", "AL6")
    print_1p8("FLASH_RDYBSYN1", "AN7")
    print_1p8("FLASH_RESETn"  , "AJ6")
    print_1p8("FLASH_WEn"     , "AN8")
print_flash()

def print_push_button():
  print(f"#============================================================")
  print(f"# PUSH BUTTON")
  print(f"#============================================================")  
  if CHIP_SELECT == "Stratix V GX":
    print_2p5("USER_PB0", "A7")
    print_2p5("USER_PB1", "B7")
    print_2p5("USER_PB2", "C7")
print_push_button()

def print_dipsw():
  print(f"#============================================================")
  print(f"# DIPSW")
  print(f"#============================================================")
  if CHIP_SELECT == "Stratix V GX":
    dipsw_pins = ["E7", "H7", "J7", "K7", "M6", "N6", "P7", "N7"]
    for a in range(len(dipsw_pins)):
      print_2p5(f"USER_DIPSW[{a}]", dipsw_pins[a])
print_dipsw()

def print_led():
  print(f"#============================================================")
  print(f"# LED")
  print(f"#============================================================")
  if CHIP_SELECT == "Stratix V GX":
    ledr_pins = ["AH28", "AG30", "AL7", "AR24", "AM7", "AW7", "AL23", "AV7"]
    ledg_pins = ["J11", "U10", "U9", "AU24", "AF28", "AE29", "AR7", "AV10"]
    print_2p5(f"USER_LED_R[0]", ledr_pins[0])
    print_2p5(f"USER_LED_R[1]", ledr_pins[1])
    print_1p8(f"USER_LED_R[2]", ledr_pins[2])
    print_1p8(f"USER_LED_R[3]", ledr_pins[3])
    print_1p8(f"USER_LED_R[4]", ledr_pins[4])
    print_1p8(f"USER_LED_R[5]", ledr_pins[5])
    print_1p8(f"USER_LED_R[6]", ledr_pins[6])
    print_1p8(f"USER_LED_R[7]", ledr_pins[7])
    print_2p5(f"USER_LED_G[0]", ledg_pins[0])
    print_2p5(f"USER_LED_G[1]", ledg_pins[1])
    print_2p5(f"USER_LED_G[2]", ledg_pins[2])
    print_1p8(f"USER_LED_G[3]", ledg_pins[3])
    print_2p5(f"USER_LED_G[4]", ledg_pins[4])
    print_2p5(f"USER_LED_G[5]", ledg_pins[5])
    print_1p8(f"USER_LED_G[6]", ledg_pins[6])
    print_2p5(f"USER_LED_G[7]", ledg_pins[7])
print_ledr()

def print_lcd():
  print(f"#============================================================")
  print(f"# LCD")
  print(f"#============================================================")
  if CHIP_SELECT == "Stratix V GX":
    print_2p5("LCD_D_Cn"    , "AH10")
    print_2p5("LCD_WEn"     , "AW10")
    print_2p5("LCD_CSn"     , "AU9")
    lcd_data_pins = ["AP10", "AN10", "AM10", "AL10", "AP9", "AN9", "AT9", "AR9"]
    for a in range(len(lcd_data_pins)):
      print_2p5("LCD_DATA[{a}]" , lcd_data_pins[a])
print_hex()

def print_hsmc():
  print(f"#============================================================")
  print(f"# HSMC")
  print(f"#============================================================")
  if CHIP_SELECT == "Stratix V GX":
    hsmc_a_pins = ["AG28", "AT8" , "G6"  , "AR8" , "G7"  , "AJ10", "AH9" , "G8"  , "AG9" , "G9"  ,
                   "AV2" , "AV1" , "AP2" , "AP2" , "AM2" , "AM1" , "AK2" , "AK1" , "AH2" , "AH1" ,
                   "AF2" , "AF1" , "AD2" , "AD1" , "AB2" , "AB1" , "AU4" , "AU3" , "AN4" , "AN3" ,
                   "AL4" , "AL3" , "AJ4" , "AJ3" , "AG4" , "AG3" , "AE4" , "AE3" , "AC4" , "AC3" , 
                   "AA4" , "AA3" , "AJ29", "AK29", "AR28", "AP28", "AW8" , "AM29", "AL29", "AW11",
                   "AU12", "AR12", "AK12", "AJ12", "AG10", "AE12", "AG10", "R9"  , "L9"  , "L8"  ,
                   "G11" , "F9"  , "E8"  , "E11" , "C9"  , "A10" , "AV11", "AT12", "AR11", "AL12",
                   "AH12", "AF10", "AD12", "AB10", "T9"  , "M9"  , "M8"  , "H11" , "G10" , "F8"  ,
                   "F11" , "C8"  , "B10" , "AU11", "AN11", "AL11", "AF11", "AE11", "AE9" , "AC9" ,
                   "AC12", "P8"  , "N10" , "N9"  , "J9"  , "H10" , "D9"  , "C10" , "A11" , "B8"  ,
                   "AT11", "AM11", "AK11", "AG12", "AE10", "AD9" , "AB9" , "AB12", "R8"  , "P10" ,
                   "N8"  , "K9"  , "J10" , "E9"  , "D10" , "B11" , "A8"]
    print_2p5("HSMA_CLK_IN0"   , hsmc_a_pins[0])
    print_2p5("HSMA_CLK_IN_N1" , hsmc_a_pins[1])
    print_2p5("HSMA_CLK_IN_N2" , hsmc_a_pins[2])
    print_2p5("HSMA_CLK_IN_P1" , hsmc_a_pins[3])
    print_2p5("HSMA_CLK_IN_P2" , hsmc_a_pins[4])
    print_2p5("HSMA_CLK_OUT0"  , hsmc_a_pins[5])
    print_2p5("HSMA_CLK_OUT_N1", hsmc_a_pins[6])
    print_2p5("HSMA_CLK_OUT_N2", hsmc_a_pins[7])
    print_2p5("HSMA_CLK_OUT_P1", hsmc_a_pins[8])
    print_2p5("HSMA_CLK_OUT_P2", hsmc_a_pins[9])
    print_2p5("HSMA_RX_P[0]"   , hsmc_a_pins[10])
    print_2p5("HSMA_RX_N[0]"   , hsmc_a_pins[11])
    print_2p5("HSMA_RX_P[1]"   , hsmc_a_pins[12])
    print_2p5("HSMA_RX_N[1]"   , hsmc_a_pins[13])
    print_2p5("HSMA_RX_P[2]"   , hsmc_a_pins[14])
    print_2p5("HSMA_RX_N[2]"   , hsmc_a_pins[15])
    print_2p5("HSMA_RX_P[3]"   , hsmc_a_pins[16])
    print_2p5("HSMA_RX_N[3]"   , hsmc_a_pins[17])
    print_2p5("HSMA_RX_P[4]"   , hsmc_a_pins[18])
    print_2p5("HSMA_RX_N[4]"   , hsmc_a_pins[19])
    print_2p5("HSMA_RX_P[5]"   , hsmc_a_pins[20])
    print_2p5("HSMA_RX_N[5]"   , hsmc_a_pins[21])
    print_2p5("HSMA_RX_P[6]"   , hsmc_a_pins[22])
    print_2p5("HSMA_RX_N[6]"   , hsmc_a_pins[23])
    print_2p5("HSMA_RX_P[7]"   , hsmc_a_pins[24])
    print_2p5("HSMA_RX_N[7]"   , hsmc_a_pins[25])
    print_2p5("HSMA_TX_P[0]"   , hsmc_a_pins[26])
    print_2p5("HSMA_TX_N[0]"   , hsmc_a_pins[27])
    print_2p5("HSMA_TX_P[1]"   , hsmc_a_pins[28])
    print_2p5("HSMA_TX_N[1]"   , hsmc_a_pins[29])
    print_2p5("HSMA_TX_P[2]"   , hsmc_a_pins[30])
    print_2p5("HSMA_TX_N[2]"   , hsmc_a_pins[31])
    print_2p5("HSMA_TX_P[3]"   , hsmc_a_pins[32])
    print_2p5("HSMA_TX_N[3]"   , hsmc_a_pins[33])
    print_2p5("HSMA_TX_P[4]"   , hsmc_a_pins[34])
    print_2p5("HSMA_TX_N[4]"   , hsmc_a_pins[35])
    print_2p5("HSMA_TX_P[5]"   , hsmc_a_pins[36])
    print_2p5("HSMA_TX_N[5]"   , hsmc_a_pins[37])
    print_2p5("HSMA_TX_P[6]"   , hsmc_a_pins[38])
    print_2p5("HSMA_TX_N[6]"   , hsmc_a_pins[39])
    print_2p5("HSMA_TX_P[7]"   , hsmc_a_pins[40])
    print_2p5("HSMA_TX_N[7]"   , hsmc_a_pins[41])
    print_2p5("HSMA_D[0]"      , hsmc_a_pins[42])
    print_2p5("HSMA_D[1]"      , hsmc_a_pins[43])
    print_2p5("HSMA_D[2]"      , hsmc_a_pins[44])
    print_2p5("HSMA_D[3]"      , hsmc_a_pins[45])
    

def print_config():
  print(f"#============================================================")
  print(f"# CONFIGURE")
  print(f"#============================================================")
  print(f"set_global_assignment -name MIN_CORE_JUNCTION_TEMP 0")
  print(f"set_global_assignment -name MAX_CORE_JUNCTION_TEMP 85")
print_config()
