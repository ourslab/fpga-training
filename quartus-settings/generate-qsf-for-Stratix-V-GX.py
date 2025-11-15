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
    print_gpio("HSMA_CLK_IN0"   , hsmc_a_pins[0])
    print_gpio("HSMA_CLK_IN_N1" , hsmc_a_pins[1])
    print_gpio("HSMA_CLK_IN_N2" , hsmc_a_pins[2])
    print_gpio("HSMA_CLK_IN_P1" , hsmc_a_pins[3])
    print_gpio("HSMA_CLK_IN_P2" , hsmc_a_pins[4])
    print_gpio("HSMA_CLK_OUT0"  , hsmc_a_pins[5])
    print_gpio("HSMA_CLK_OUT_N1", hsmc_a_pins[6])
    print_gpio("HSMA_CLK_OUT_N2", hsmc_a_pins[7])
    print_gpio("HSMA_CLK_OUT_P1", hsmc_a_pins[8])
    print_gpio("HSMA_CLK_OUT_P2", hsmc_a_pins[9])
    print_gpio("HSMA_RX_P0"     , hsmc_a_pins[10])
    print_gpio("HSMA_RX_N0"     , hsmc_a_pins[11])
    print_gpio("HSMA_RX_P1"     , hsmc_a_pins[12])
    print_gpio("HSMA_RX_N1"     , hsmc_a_pins[13])
    print_gpio("HSMA_RX_P2"     , hsmc_a_pins[14])
    print_gpio("HSMA_RX_N2"     , hsmc_a_pins[15])
    print_gpio("HSMA_RX_P3"     , hsmc_a_pins[16])
    print_gpio("HSMA_RX_N3"     , hsmc_a_pins[17])
    print_gpio("HSMA_RX_P4"     , hsmc_a_pins[18])
    print_gpio("HSMA_RX_N4"     , hsmc_a_pins[19])
    print_gpio("HSMA_RX_P5"     , hsmc_a_pins[20])
    print_gpio("HSMA_RX_N5"     , hsmc_a_pins[21])
    print_gpio("HSMA_RX_P6"     , hsmc_a_pins[22])
    print_gpio("HSMA_RX_N6"     , hsmc_a_pins[23])
    print_gpio("HSMA_RX_P7"     , hsmc_a_pins[24])
    print_gpio("HSMA_RX_N7"     , hsmc_a_pins[25])

def print_audio():
  print(f"#============================================================")
  print(f"# AUD")
  print(f"#============================================================")
  print_lvttl3p3(f"AUD_ADCLRCK", "PIN_K8")
  print_lvttl3p3(f"AUD_ADCDAT", "PIN_K7")
  print_lvttl3p3(f"AUD_DACLRCK", "PIN_H8")
  print_lvttl3p3(f"AUD_DACDAT", "PIN_J7")
  print_lvttl3p3(f"AUD_XCK", "PIN_G7")
  print_lvttl3p3(f"AUD_BCLK", "PIN_H7")
print_audio()

def print_i2c():
  print(f"#============================================================")
  print(f"# I2C")
  print(f"#============================================================")
  print_lvttl3p3(f"FPGA_I2C_SCLK", "PIN_J12")
  print_lvttl3p3(f"FPGA_I2C_SDAT", "PIN_K12")
  print_lvttl3p3(f"HPS_I2C1_SCLK", "PIN_E23")
  print_lvttl3p3(f"HPS_I2C1_SDAT", "PIN_C24")
  print_lvttl3p3(f"HPS_I2C2_SCLK", "PIN_H23")
  print_lvttl3p3(f"HPS_I2C2_SDAT", "PIN_A25")
print_i2c()

def print_vga():
  print(f"#============================================================")
  print(f"# VGA")
  print(f"#============================================================")
  vga_r = ["PIN_A13", "PIN_C13", "PIN_E13", "PIN_B12", "PIN_C12", "PIN_D12", "PIN_E12", "PIN_F13"]
  for a in range(len(vga_r)):
    print_lvttl3p3(f"VGA_R[{a}]", vga_r[a])
  vga_g = ["PIN_J9" , "PIN_J10", "PIN_H12", "PIN_G10", "PIN_G11", "PIN_G12", "PIN_F11", "PIN_E11"]
  for a in range(len(vga_g)):
    print_lvttl3p3(f"VGA_G[{a}]", vga_g[a])
  vga_b = ["PIN_B13", "PIN_G13", "PIN_H13", "PIN_F14", "PIN_H14", "PIN_F15", "PIN_G15", "PIN_J14"]
  for a in range(len(vga_b)):
    print_lvttl3p3(f"VGA_B[{a}]", vga_b[a])
  print_lvttl3p3(f"VGA_CLK", "PIN_A11")
  print_lvttl3p3(f"VGA_BLANK_N", "PIN_F10")
  print_lvttl3p3(f"VGA_HS", "PIN_B11")
  print_lvttl3p3(f"VGA_VS", "PIN_D11")
  print_lvttl3p3(f"VGA_SYNC_N", "PIN_C10")
print_vga()

def print_TVDecoder():
  print(f"#============================================================")
  print(f"# TVDecoder")
  print(f"#============================================================")
  td_data = ["PIN_D2", "PIN_B1", "PIN_E2", "PIN_B2", "PIN_D1", "PIN_E1", "PIN_C2", "PIN_B3"]
  for a in range(len(td_data)):
    print_lvttl3p3(f"TD_DATA[{a}]", td_data[a])
  print_lvttl3p3(f"TD_HS", "PIN_A5")
  print_lvttl3p3(f"TD_VS", "PIN_A3")
  print_lvttl3p3(f"TD_CLK27", "PIN_H15")
  print_lvttl3p3(f"TD_RESET_N", "PIN_F6")
print_TVDecoder()

def print_ir():
  print(f"#============================================================")
  print(f"# IR")
  print(f"#============================================================")
  print_lvttl3p3(f"IRDA_RXD", "PIN_AA30")
  print_lvttl3p3(f"IRDA_TXD", "PIN_AB30")
print_ir()

def print_dram():
  print(f"#============================================================")
  print(f"# DRAM")
  print(f"#============================================================")
  dram_addr = ["PIN_AK14", "PIN_AH14", "PIN_AG15", "PIN_AE14", "PIN_AB15", "PIN_AC14", 
                "PIN_AD14", "PIN_AF15", "PIN_AH15", "PIN_AG13", "PIN_AG12", "PIN_AH13", "PIN_AJ14"]
  for a in range(len(dram_addr)):
    print_lvttl3p3(f"DRAM_ADDR[{a}]", dram_addr[a])
  dram_dat = ["PIN_AK6" , "PIN_AJ7" , "PIN_AK7" , "PIN_AK8" , "PIN_AK9", "PIN_AG10", 
               "PIN_AK11", "PIN_AJ11", "PIN_AH10", "PIN_AJ10", "PIN_AJ9", "PIN_AH9" , 
               "PIN_AH8" , "PIN_AH7" , "PIN_AJ6" , "PIN_AJ5"]
  for a in range(len(dram_dat)):
    print_lvttl3p3(f"DRAM_DQ[{a}]", dram_dat[a])
  print_lvttl3p3(f"DRAM_BA[0]", "PIN_AF13")
  print_lvttl3p3(f"DRAM_BA[1]", "PIN_AJ12")
  print_lvttl3p3(f"DRAM_LDQM", "PIN_AB13")
  print_lvttl3p3(f"DRAM_UDQM", "PIN_AK12")
  print_lvttl3p3(f"DRAM_RAS_N", "PIN_AE13")
  print_lvttl3p3(f"DRAM_CAS_N", "PIN_AF11")
  print_lvttl3p3(f"DRAM_CKE", "PIN_AK13")
  print_lvttl3p3(f"DRAM_CLK", "PIN_AH12")
  print_lvttl3p3(f"DRAM_WE_N", "PIN_AA13")
  print_lvttl3p3(f"DRAM_CS_N", "PIN_AG11")
print_dram()

def print_ps2():
  print(f"#============================================================")
  print(f"# PS2")
  print(f"#============================================================")
  print_lvttl3p3(f"PS2_CLK", "PIN_AD7")
  print_lvttl3p3(f"PS2_DAT", "PIN_AE7")
  print_lvttl3p3(f"PS2_CLK2", "PIN_AD9")
  print_lvttl3p3(f"PS2_DAT2", "PIN_AE9")
print_ps2()

def print_adconv():
  print(f"#============================================================")
  print(f"# ADconverter")
  print(f"#============================================================")
  print_lvttl3p3(f"ADC_CS_N", "PIN_AJ4")
  print_lvttl3p3(f"ADC_DOUT", "PIN_AK3")
  print_lvttl3p3(f"ADC_DIN", "PIN_AK4")
  print_lvttl3p3(f"ADC_SCLK", "PIN_AK2")
print_adconv()

def print_hps_enet():
  print(f"#============================================================")
  print(f"# HPS_ENET")
  print(f"#============================================================")
  print_lvttl3p3(f"HPS_ENET_TX_EN", "PIN_A20")
  print_lvttl3p3(f"HPS_ENET_TX_DATA[0]", "PIN_F20")
  print_lvttl3p3(f"HPS_ENET_TX_DATA[1]", "PIN_J19")
  print_lvttl3p3(f"HPS_ENET_TX_DATA[2]", "PIN_F21")
  print_lvttl3p3(f"HPS_ENET_TX_DATA[3]", "PIN_F19")
  print_lvttl3p3(f"HPS_ENET_RX_DV", "PIN_K17")
  print_lvttl3p3(f"HPS_ENET_RX_DATA[0]", "PIN_A21")
  print_lvttl3p3(f"HPS_ENET_RX_DATA[1]", "PIN_B20")
  print_lvttl3p3(f"HPS_ENET_RX_DATA[2]", "PIN_B18")
  print_lvttl3p3(f"HPS_ENET_RX_DATA[3]", "PIN_D21")
  print_lvttl3p3(f"HPS_ENET_RX_CLK", "PIN_G20")
  print_lvttl3p3(f"HPS_ENET_RESET_N", "PIN_E18")
  print_lvttl3p3(f"HPS_ENET_MDIO", "PIN_E21")
  print_lvttl3p3(f"HPS_ENET_MDC", "PIN_B21")
  print_lvttl3p3(f"HPS_ENET_INT_N", "PIN_C19")
  print_lvttl3p3(f"HPS_ENET_GTX_CLK", "PIN_H19")
print_hps_enet()

def print_hps_uart():  
  print(f"#============================================================")
  print(f"# HPS_UART")
  print(f"#============================================================")
  print_lvttl3p3(f"HPS_UART_RX", f"PIN_B25")
  print_lvttl3p3(f"HPS_UART_TX", f"PIN_C25") 
  print_lvttl3p3(f"HPS_CONV_USB_N", f"PIN_B15")
print_hps_uart()

def print_hps_ddr3():
  print(f"#============================================================")
  print(f"# HPS_DDR3")
  print(f"#============================================================")
  hps_ddr3_a_pins = ["PIN_F26", "PIN_G30", "PIN_F28", "PIN_F30", "PIN_J25", "PIN_J27", "PIN_F29", "PIN_E28",
                     "PIN_H27", "PIN_G26", "PIN_D29", "PIN_C30", "PIN_B30", "PIN_C29", "PIN_H25"]
  for a in range(len(hps_ddr3_a_pins)):
    print_sstl1p5(f"HPS_DDR3_A[{a}]", hps_ddr3_a_pins[a]) 
  hps_ddr3_ba_pins = ["PIN_E29", "PIN_J24", "PIN_J23"]
  for a in range(len(hps_ddr3_ba_pins)):
    print_sstl1p5(f"HPS_DDR3_BA[{a}]", hps_ddr3_ba_pins[a]) 
  print_sstl1p5(f"HPS_DDR3_CAS_n", "PIN_E27")  
  print_sstl1p5(f"HPS_DDR3_CKE", "PIN_L29")  
  print_diff1p5(f"HPS_DDR3_CK_n", "PIN_L23")  
  print_diff1p5(f"HPS_DDR3_CK_p", "PIN_M23")  
  print_sstl1p5(f"HPS_DDR3_CS_n", "PIN_H24")  
  hps_ddr3_dm_pins = ["PIN_K28", "PIN_M28", "PIN_R28", "PIN_W30"]
  for a in range(len(hps_ddr3_dm_pins)):
    print_sstl1p5(f"HPS_DDR3_DM[{a}]", hps_ddr3_dm_pins[a])
  hps_ddr3_dq_pins = ["PIN_K23", "PIN_K22", "PIN_H30", "PIN_G28", "PIN_L25", "PIN_L24", 
                      "PIN_J30", "PIN_J29", "PIN_K26", "PIN_L26", "PIN_K29", "PIN_K27", 
                      "PIN_M26", "PIN_M27", "PIN_L28", "PIN_M30", "PIN_U26", "PIN_T26", 
                      "PIN_N29", "PIN_N28", "PIN_P26", "PIN_P27", "PIN_N27", "PIN_R29", 
                      "PIN_P24", "PIN_P25", "PIN_T29", "PIN_T28", "PIN_R27", "PIN_R26", 
                      "PIN_V30", "PIN_W29"]
  for a in range(len(hps_ddr3_dq_pins)):
    print_sstl1p5(f"HPS_DDR3_DQ[{a}]", hps_ddr3_dq_pins[a])
  hps_ddr3_dqs_n_pins = ["PIN_M19", "PIN_N24", "PIN_R18", "PIN_R21"]
  for a in range(len(hps_ddr3_dqs_n_pins)):
    print_sstl1p5(f"HPS_DDR3_DQS_N[{a}]", hps_ddr3_dqs_n_pins[a])
  hps_ddr3_dqs_p_pins = ["PIN_N18", "PIN_N25", "PIN_R19", "PIN_R22"]
  for a in range(len(hps_ddr3_dqs_p_pins)):
    print_sstl1p5(f"HPS_DDR3_DQS_P[{a}]", hps_ddr3_dqs_p_pins[a])
  print_sstl1p5(f"HPS_DDR3_ODT", "PIN_H28")  
  print_sstl1p5(f"HPS_DDR3_RAS_n", "PIN_D30")  
  print_sstl1p5(f"HPS_DDR3_RESET_n", "PIN_P30")  
  print_sstl1p5(f"HPS_DDR3_WE_n", "PIN_C28")  
  print_sstl1p5(f"HPS_DDR3_RZQ", "PIN_D27")  
print_hps_ddr3()

def print_hps_sdcard():
  print(f"#============================================================")
  print(f"# HPS_SD")
  print(f"#============================================================")
  print_lvttl3p3(f"HPS_SD_CLK", "PIN_A16")
  print_lvttl3p3(f"HPS_SD_CMD", "PIN_F18")
  print_lvttl3p3(f"HPS_SD_DATA[0]", "PIN_G18")
  print_lvttl3p3(f"HPS_SD_DATA[1]", "PIN_C17")
  print_lvttl3p3(f"HPS_SD_DATA[2]", "PIN_D17")
  print_lvttl3p3(f"HPS_SD_DATA[3]", "PIN_B16")
print_hps_sdcard()

def print_hps_usb():
  print(f"#============================================================")
  print(f"# HPS_USB")
  print(f"#============================================================")
  print_lvttl3p3(f"HPS_USB_CLKOUT", "PIN_N16")
  hps_usb_data = ["PIN_E16", "PIN_G16", "PIN_D16", "PIN_D14", "PIN_A15", 
                  "PIN_C14", "PIN_D15", "PIN_M17"]
  for a in range(len(hps_usb_data)):
    print_lvttl3p3(f"HPS_USB_DATA[{a}]", hps_usb_data[a])
  print_lvttl3p3(f"HPS_USB_DIR", "PIN_E14")
  print_lvttl3p3(f"HPS_USB_NXT", "PIN_A14")
  print_lvttl3p3(f"HPS_USB_RESET", "PIN_G17")
  print_lvttl3p3(f"HPS_USB_STP", "PIN_C15")
print_hps_usb()

def print_hps_gsensor():
  print(f"#============================================================")
  print(f"# HPS_GSENSOR")
  print(f"#============================================================")
  print_lvttl3p3(f"HPS_GSENSOR_INT", "PIN_B22")
print_hps_gsensor()

def print_hps_ltc():
  print(f"#============================================================")
  print(f"# HPS_LTC")
  print(f"#============================================================")
  print_lvttl3p3(f"HPS_LTC_GPIO", "PIN_H17")
print_hps_ltc()

def print_hps_spim():
  print(f"#============================================================")
  print(f"# HPS_SPIM")
  print(f"#============================================================")
  print_lvttl3p3(f"HPS_SPIM_CLK", "PIN_C23")
  print_lvttl3p3(f"HPS_SPIM_MISO", "PIN_E24")
  print_lvttl3p3(f"HPS_SPIM_MOSI", "PIN_D22")
  print_lvttl3p3(f"HPS_SPIM_SS", "PIN_D24")
print_hps_spim()

def print_config():
  print(f"#============================================================")
  print(f"# CONFIGURE")
  print(f"#============================================================")
  print(f"set_global_assignment -name MIN_CORE_JUNCTION_TEMP 0")
  print(f"set_global_assignment -name MAX_CORE_JUNCTION_TEMP 85")
print_config()
