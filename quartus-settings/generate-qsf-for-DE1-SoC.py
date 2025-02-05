#! /usr/bin/python3

TOP_LEVEL_ENTITY = "TOP"

def print_sstl1p5(name, location):
  print(f"set_location_assignment {location} -to {name}")
  print(f"set_instance_assignment -name IO_STANDARD \"SSTL-15 CLASS I\" -to {name}")
def print_diff1p5(name, location):
  print(f"set_location_assignment {location} -to {name}")
  print(f"set_instance_assignment -name IO_STANDARD \"DIFFERENTIAL 1.5-V SSTL CLASS I\" -to {name}")
def print_2p5(name, location):
  print(f"set_location_assignment {location} -to {name}")
  print(f"set_instance_assignment -name IO_STANDARD \"2.5 V\" -to {name}")
def print_diff2p5(name, location):
  print(f"set_location_assignment {location} -to {name}")
  print(f"set_instance_assignment -name IO_STANDARD \"DIFFERENTIAL 2.5-V SSTL CLASS II\" -to {name}")
def print_3p3(name, location):
  print(f"set_location_assignment {location} -to {name}")
  print(f"set_instance_assignment -name IO_STANDARD \"3.3 V\" -to {name}")
def print_lvttl3p3(name, location):
  print(f"set_location_assignment {location} -to {name}")
  print(f"set_instance_assignment -name IO_STANDARD \"3.3-V LVTTL\" -to {name}")

def print_de1soc():
  print(f"#============================================================")
  print(f"# DE1-SoC")
  print(f"#============================================================")
  print(f"set_global_assignment -name FAMILY \"Cyclone V\"")
  print(f"set_global_assignment -name DEVICE 5CSEMA5F31C6")
  print(f"set_global_assignment -name TOP_LEVEL_ENTITY {TOP_LEVEL_ENTITY}")
  print(f"set_global_assignment -name PROJECT_OUTPUT_DIRECTORY output_files")
  print(f"set_global_assignment -name EDA_SIMULATION_TOOL \"ModelSim-Altera (VHDL)\"")
print_de1soc()

def print_clock():
  print(f"#============================================================")
  print(f"# CLOCK")
  print(f"#============================================================")
  print_lvttl3p3("CLOCK_50", "PIN_AF14")
  print_lvttl3p3("CLOCK1_50", "PIN_AF14")
  print_lvttl3p3("CLOCK2_50", "PIN_AA16")
  print_lvttl3p3("CLOCK3_50", "PIN_Y26")
  print_lvttl3p3("CLOCK4_50", "PIN_K14")
  print_lvttl3p3("HPS_CLOCK1_25", "PIN_D25")
  print_lvttl3p3("HPS_CLOCK2_25", "PIN_F25")
print_clock()

def print_sw():
  print(f"#============================================================")
  print(f"# SW")
  print(f"#============================================================")
  sw_pins = ["PIN_AB12", "PIN_AC12", "PIN_AF9", "PIN_AF10", "PIN_AD11",
             "PIN_AD12", "PIN_AE11", "PIN_AC9", "PIN_AD10", "PIN_AE12"]
  for a in range(10):
    print_lvttl3p3(f"SW[{a}]", sw_pins[a])
print_sw()

def print_key():
  print(f"#============================================================")
  print(f"# KEY")
  print(f"#============================================================")
  key_pins = ["PIN_AA14", "PIN_AA15", "PIN_W15", "PIN_Y16"]
  for a in range(4):
    print_lvttl3p3(f"KEY[{a}]", key_pins[a])
print_key()

def print_ledr():
  print(f"#============================================================")
  print(f"# LEDR")
  print(f"#============================================================")
  ledr_pins = ["PIN_V16", "PIN_W16", "PIN_V17", "PIN_V18", "PIN_W17",
               "PIN_W19", "PIN_Y19", "PIN_W20", "PIN_W21", "PIN_Y21"]
  for a in range(10):
    print_lvttl3p3(f"LEDR[{a}]", ledr_pins[a])
print_ledr()

def print_hex():
  print(f"#============================================================")
  print(f"# HEX")
  print(f"#============================================================")
  hex_pins = [["PIN_AE26", "PIN_AE27", "PIN_AE28", "PIN_AG27", "PIN_AF28", "PIN_AG28", "PIN_AH28"],
              ["PIN_AJ29", "PIN_AH29", "PIN_AH30", "PIN_AG30", "PIN_AF29", "PIN_AF30", "PIN_AD27"],
              ["PIN_AB23", "PIN_AE29", "PIN_AD29", "PIN_AC28", "PIN_AD30", "PIN_AC29", "PIN_AC30"],
              ["PIN_AD26", "PIN_AC27", "PIN_AD25", "PIN_AC25", "PIN_AB28", "PIN_AB25", "PIN_AB22"],
              ["PIN_AA24", "PIN_Y23",  "PIN_Y24",  "PIN_W22",  "PIN_W24",  "PIN_V23",  "PIN_W25"],
              ["PIN_V25", "PIN_AA28",  "PIN_Y27",  "PIN_AB27", "PIN_AB26", "PIN_AA26", "PIN_AA25"]]
  for a in range(6):
    for b in range(7):
      print_lvttl3p3(f"HEX{a}[{b}]", hex_pins[a][b])
print_hex()

def print_gpio():
  print(f"#============================================================")
  print(f"# GPIO")
  print(f"#============================================================")
  gpio0_pins = ["PIN_AC18", "PIN_Y17", "PIN_AD17", "PIN_Y18", "PIN_AK16", "PIN_AK18", "PIN_AK19", "PIN_AJ19", "PIN_AJ17", 
                "PIN_AJ16", "PIN_AH18", "PIN_AH17", "PIN_AG16", "PIN_AE16", "PIN_AF16", "PIN_AG17", "PIN_AA18", "PIN_AA19", 
                "PIN_AE17", "PIN_AC20", "PIN_AH19", "PIN_AJ20", "PIN_AH20", "PIN_AK21", "PIN_AD19", "PIN_AD20", "PIN_AE18", 
                "PIN_AE19", "PIN_AF20", "PIN_AF21", "PIN_AF19", "PIN_AG21", "PIN_AF18", "PIN_AG20", "PIN_AG18", "PIN_AJ21"]
  gpio1_pins = ["PIN_AB17", "PIN_AA21", "PIN_AB21", "PIN_AC23", "PIN_AD24", "PIN_AE23", "PIN_AE24", "PIN_AF25", "PIN_AF26",
                "PIN_AG25", "PIN_AG26", "PIN_AH24", "PIN_AH27", "PIN_AJ27", "PIN_AK29", "PIN_AK28", "PIN_AK27", "PIN_AJ26",
                "PIN_AK26", "PIN_AH25", "PIN_AJ25", "PIN_AJ24", "PIN_AK24", "PIN_AG23", "PIN_AK23", "PIN_AH23", "PIN_AK22",
                "PIN_AJ22", "PIN_AH22", "PIN_AG22", "PIN_AF24", "PIN_AF23", "PIN_AE22", "PIN_AD21", "PIN_AA20", "PIN_AC22"]
  for a in range(36):
    print_lvttl3p3(f"GPIO_0[{a}]", gpio0_pins[a])
  for a in range(36):
    print_lvttl3p3(f"GPIO_1[{a}]", gpio1_pins[a])
print_gpio()

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

