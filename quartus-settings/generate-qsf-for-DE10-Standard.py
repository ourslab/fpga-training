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

def print_de10():
  print(f"#============================================================")
  print(f"# DE10-Standard")
  print(f"#============================================================")
  print(f"set_global_assignment -name FAMILY \"Cyclone V\"")
  print(f"set_global_assignment -name DEVICE 5CSXFC6D6F31C6")
  print(f"set_global_assignment -name TOP_LEVEL_ENTITY {TOP_LEVEL_ENTITY}")
  print(f"set_global_assignment -name PROJECT_OUTPUT_DIRECTORY output_files")
  print(f"set_global_assignment -name EDA_SIMULATION_TOOL \"ModelSim-Altera (VHDL)\"")
print_de10()

def print_clock():
  print(f"#============================================================")
  print(f"# CLOCK")
  print(f"#============================================================")
  print_3p3("CLOCK_50", "PIN_AF14")
  print_3p3("CLOCK2_50", "PIN_AA16")
  print_3p3("CLOCK3_50", "PIN_Y26")
  print_3p3("CLOCK4_50", "PIN_K14")
  print_3p3("HPS_CLOCK1_25", "PIN_D25")
  print_3p3("HPS_CLOCK2_25", "PIN_F25")
print_clock()

def print_sw():
  print(f"#============================================================")
  print(f"# SW")
  print(f"#============================================================")
  sw_pins = ["PIN_AB30", "PIN_Y27",  "PIN_AB28", "PIN_AC30", "PIN_W25",
             "PIN_V25",  "PIN_AC28", "PIN_AD30", "PIN_AC29", "PIN_AA30"]
  for a in range(len(sw_pins)):
    print_2p5(f"SW[{a}]", sw_pins[a]) # Depending on JP3
print_sw()

def print_key():
  print(f"#============================================================")
  print(f"# KEY")
  print(f"#============================================================")
  key_pins = ["PIN_AJ14", "PIN_AK4", "PIN_AA14", "PIN_AA15"]
  for a in range(len(key_pins)):
    print_3p3(f"KEY[{a}]", key_pins[a])
print_key()

def print_ledr():
  print(f"#============================================================")
  print(f"# LEDR")
  print(f"#============================================================")
  ledr_pins = ["PIN_AA24", "PIN_AB23", "PIN_AC23", "PIN_AD24", "PIN_AG25",
               "PIN_AF25", "PIN_AE24", "PIN_AF24", "PIN_AB22", "PIN_AC22"]
  for a in range(len(ledr_pins)):
    print_3p3(f"LEDR[{a}]", ledr_pins[a])
print_ledr()

def print_hex():
  print(f"#============================================================")
  print(f"# HEX")
  print(f"#============================================================")
  hex_pins = [["PIN_W17",  "PIN_V18",  "PIN_AG17", "PIN_AG16", "PIN_AH17", "PIN_AG18", "PIN_AH18"],
              ["PIN_AF16", "PIN_V16",  "PIN_AE16", "PIN_AD17", "PIN_AE18", "PIN_AE17", "PIN_V17" ],
              ["PIN_AA21", "PIN_AB17", "PIN_AA18", "PIN_Y17",  "PIN_Y18",  "PIN_AF18", "PIN_W16" ],
              ["PIN_Y19",  "PIN_W19",  "PIN_AD19", "PIN_AA20", "PIN_AC20", "PIN_AA19", "PIN_AD20"],
              ["PIN_AD21", "PIN_AG22", "PIN_AE22", "PIN_AE23", "PIN_AG23", "PIN_AF23", "PIN_AH22"],
              ["PIN_AF21", "PIN_AG21", "PIN_AF20", "PIN_AG20", "PIN_AE19", "PIN_AF19", "PIN_AB21"]]
  for a in range(6):
    for b in range(7):
      print_3p3(f"HEX{a}[{b}]", hex_pins[a][b])
print_hex()

def print_gpio():
  print(f"#============================================================")
  print(f"# GPIO")
  print(f"#============================================================")
  gpio_pins = ["PIN_W15", "PIN_AK2", "PIN_Y16",  "PIN_AK3",  "PIN_AJ1",  "PIN_AJ2", "PIN_AH2",  "PIN_AH3",  "PIN_AH4", 
               "PIN_AH5", "PIN_AG1", "PIN_AG2",  "PIN_AG3",  "PIN_AG5",  "PIN_AG6", "PIN_AG7",  "PIN_AG8",  "PIN_AF4",
               "PIN_AF5", "PIN_AF6", "PIN_AF8",  "PIN_AF9",  "PIN_AF10", "PIN_AE7", "PIN_AE9",  "PIN_AE11", "PIN_AE12",
               "PIN_AD7", "PIN_AD9", "PIN_AD10", "PIN_AD11", "PIN_AD12", "PIN_AC9", "PIN_AC12", "PIN_AB12", "PIN_AA12"]
  for a in range(36):
    print_3p3(f"GPIO[{a}]", gpio_pins[a])
print_gpio()

def print_hsmc():
  print(f"#============================================================")
  print(f"# HSMC")
  print(f"#============================================================")
  print_3p3(f"HSMC_CLKIN0", "PIN_J14") # Depending on JP3
  print_2p5(f"HSMC_CLKIN_N1", "PIN_AB27") # Depending on JP3
  print_2p5(f"HSMC_CLKIN_N2", "PIN_G15") # Depending on JP3
  print_2p5(f"HSMC_CLKIN_P1", "PIN_AA26") # Depending on JP3
  print_2p5(f"HSMC_CLKIN_P2", "PIN_H15") # Depending on JP3
  print_2p5(f"HSMC_CLKOUT0", "PIN_AD29") # Depending on JP3
  print_2p5(f"HSMC_CLKOUT_N1", "PIN_E6") # Depending on JP3
  print_2p5(f"HSMC_CLKOUT_N2", "PIN_A10") # Depending on JP3
  print_2p5(f"HSMC_CLKOUT_P1", "PIN_E7") # Depending on JP3
  print_2p5(f"HSMC_CLKOUT_P2", "PIN_A11") # Depending on JP3
  hsmc_d_pins = ["PIN_C10", "PIN_H13", "PIN_C9", "PIN_H12"]
  for a in range(4):
    print_2p5(f"HSMC_D[{a}]", hsmc_d_pins[a]) # Depending on JP3
  print_2p5("HSMC_SCL", "PIN_AA28")
  print_2p5("HSMC_SDA", "PIN_AE29")
  hsmc_rx_d_n_pins = ["PIN_G11", "PIN_J12", "PIN_F10", "PIN_J9",  "PIN_K8",
                      "PIN_H7",  "PIN_G8",  "PIN_F8",  "PIN_E11", "PIN_B5",
                      "PIN_D9",  "PIN_D12", "PIN_D10", "PIN_B12", "PIN_E13",
                      "PIN_G13", "PIN_F14"]
  for a in range(17):
    print_2p5(f"HSMC_RX_D_N[{a}]", hsmc_rx_d_n_pins[a]) # Depending on JP7
  hsmc_rx_d_p_pins = ["PIN_G12", "PIN_K12", "PIN_G10", "PIN_J10", "PIN_K7",
                      "PIN_J7",  "PIN_H8",  "PIN_F9",  "PIN_F11", "PIN_B6",
                      "PIN_E9",  "PIN_E12", "PIN_D11", "PIN_C13", "PIN_F13",
                      "PIN_H14", "PIN_F15"]
  for a in range(17):
    print_2p5(f"HSMC_RX_D_P[{a}]", hsmc_rx_d_p_pins[a]) # Depending on JP7
  hsmc_tx_d_n_pins = ["PIN_A8",  "PIN_D7", "PIN_F6", "PIN_C5", "PIN_C4",
                      "PIN_E2",  "PIN_D4", "PIN_B3", "PIN_D1", "PIN_C2",
                      "PIN_B1",  "PIN_A3", "PIN_A5", "PIN_B7", "PIN_B8",
                      "PIN_B11", "PIN_A13"]
  for a in range(17):
    print_2p5(f"HSMC_TX_D_N[{a}]", hsmc_tx_d_n_pins[a]) # Depending on JP7
  hsmc_tx_d_p_pins = ["PIN_A9",  "PIN_E8", "PIN_G7", "PIN_D6", "PIN_D5",
                      "PIN_E3",  "PIN_E4", "PIN_C3", "PIN_E1", "PIN_D2",
                      "PIN_B2",  "PIN_A4", "PIN_A6", "PIN_C7", "PIN_C8",
                      "PIN_C12", "PIN_B13"]
  for a in range(17):
    print_2p5(f"HSMC_TX_D_P[{a}]", hsmc_tx_d_p_pins[a]) # Depending on JP7
print_hsmc()

def print_audio():
  print(f"#============================================================")
  print(f"# AUD")
  print(f"#============================================================")
  print_3p3(f"AUD_ADCLRCK", "PIN_AH29")
  print_3p3(f"AUD_ADCDAT", "PIN_AJ29")
  print_3p3(f"AUD_DACLRCK", "PIN_AG30")
  print_3p3(f"AUD_DACDAT", "PIN_AF29")
  print_3p3(f"AUD_XCK", "PIN_AH30")
  print_3p3(f"AUD_BCLK", "PIN_AF30")
print_audio()

def print_i2c():
  print(f"#============================================================")
  print(f"# I2C")
  print(f"#============================================================")
  print_3p3(f"FPGA_I2C_SCLK", "PIN_Y24")
  print_3p3(f"FPGA_I2C_SDAT", "PIN_Y23")
  print_3p3(f"HPS_I2C1_SCLK", "PIN_E23")
  print_3p3(f"HPS_I2C1_SDAT", "PIN_C24")
  print_3p3(f"HPS_I2C2_SCLK", "PIN_H23")
  print_3p3(f"HPS_I2C2_SDAT", "PIN_A25")
print_i2c()

def print_vga():
  print(f"#============================================================")
  print(f"# VGA")
  print(f"#============================================================")
  vga_r = ["PIN_AK29", "PIN_AK28", "PIN_AK27", "PIN_AJ27", "PIN_AH27", "PIN_AF26", "PIN_AG26", "PIN_AJ26"]
  for a in range(len(vga_r)):
    print_3p3(f"VGA_R[{a}]", vga_r[a])
  vga_g = ["PIN_AK26" , "PIN_AJ25", "PIN_AH25", "PIN_AK24", "PIN_AJ24", "PIN_AH24", "PIN_AK23", "PIN_AH23"]
  for a in range(len(vga_g)):
    print_3p3(f"VGA_G[{a}]", vga_g[a])
  vga_b = ["PIN_AJ21", "PIN_AJ20", "PIN_AH20", "PIN_AJ19", "PIN_AH19", "PIN_AJ17", "PIN_AJ16", "PIN_AK16"]
  for a in range(len(vga_b)):
    print_3p3(f"VGA_B[{a}]", vga_b[a])
  print_3p3(f"VGA_CLK", "PIN_AK21")
  print_3p3(f"VGA_BLANK_N", "PIN_AK22")
  print_3p3(f"VGA_HS", "PIN_AK19")
  print_3p3(f"VGA_VS", "PIN_AK18")
  print_3p3(f"VGA_SYNC_N", "PIN_AJ22")
print_vga()

def print_TVDecoder():
  print(f"#============================================================")
  print(f"# TVDecoder")
  print(f"#============================================================")
  td_data = ["PIN_AG27", "PIN_AF28", "PIN_AE28", "PIN_AE27", "PIN_AE26", "PIN_AD27", "PIN_AD26", "PIN_AD25"]
  for a in range(len(td_data)):
    print_3p3(f"TD_DATA[{a}]", td_data[a])
  print_3p3(f"TD_HS", "PIN_AH28")
  print_3p3(f"TD_VS", "PIN_AG28")
  print_3p3(f"TD_CLK27", "PIN_AC18")
  print_3p3(f"TD_RESET_N", "PIN_AC27")
print_TVDecoder()

def print_ir():
  print(f"#============================================================")
  print(f"# IR")
  print(f"#============================================================")
  print_3p3(f"IRDA_RXD", "PIN_W20")
  print_3p3(f"IRDA_TXD", "PIN_W21")
print_ir()

def print_dram():
  print(f"#============================================================")
  print(f"# DRAM")
  print(f"#============================================================")
  dram_addr = ["PIN_AK14", "PIN_AH14", "PIN_AG15", "PIN_AE14", "PIN_AB15", "PIN_AC14",
               "PIN_AD14", "PIN_AF15", "PIN_AH15", "PIN_AG13", "PIN_AG12", "PIN_AH13", "PIN_AJ14"]
  for a in range(len(dram_addr)):
    print_3p3(f"DRAM_ADDR[{a}]", dram_addr[a])
  dram_dat = ["PIN_AK6" , "PIN_AJ7" , "PIN_AK7" , "PIN_AK8" , "PIN_AK9", "PIN_AG10",
              "PIN_AK11", "PIN_AJ11", "PIN_AH10", "PIN_AJ10", "PIN_AJ9", "PIN_AH9" ,
              "PIN_AH8" , "PIN_AH7" , "PIN_AJ6" , "PIN_AJ5"]
  for a in range(len(dram_dat)):
    print_3p3(f"DRAM_DQ[{a}]", dram_dat[a])
  print_3p3(f"DRAM_BA[0]", "PIN_AF13")
  print_3p3(f"DRAM_BA[1]", "PIN_AJ12")
  print_3p3(f"DRAM_LDQM", "PIN_AB13")
  print_3p3(f"DRAM_UDQM", "PIN_AK12")
  print_3p3(f"DRAM_RAS_N", "PIN_AE13")
  print_3p3(f"DRAM_CAS_N", "PIN_AF11")
  print_3p3(f"DRAM_CKE", "PIN_AK13")
  print_3p3(f"DRAM_CLK", "PIN_AH12")
  print_3p3(f"DRAM_WE_N", "PIN_AA13")
  print_3p3(f"DRAM_CS_N", "PIN_AG11")
print_dram()

def print_ps2():
  print(f"#============================================================")
  print(f"# PS2")
  print(f"#============================================================")
  print_3p3(f"PS2_CLK", "PIN_AB25")
  print_3p3(f"PS2_DAT", "PIN_AA25")
  print_3p3(f"PS2_CLK2", "PIN_AC25")
  print_3p3(f"PS2_DAT2", "PIN_AB26")
print_ps2()

def print_adconv():
  print(f"#============================================================")
  print(f"# ADconverter")
  print(f"#============================================================")
  print_3p3(f"ADC_CONVST", "PIN_Y21")
  print_3p3(f"ADC_DOUT", "PIN_V23")
  print_3p3(f"ADC_DIN", "PIN_W22")
  print_3p3(f"ADC_SCLK", "PIN_W24")
print_adconv()

def print_hps_enet():
  print(f"#============================================================")
  print(f"# HPS_ENET")
  print(f"#============================================================")
  print_3p3(f"HPS_ENET_TX_EN", "PIN_A20")
  print_3p3(f"HPS_ENET_TX_DATA[0]", "PIN_F20")
  print_3p3(f"HPS_ENET_TX_DATA[1]", "PIN_J19")
  print_3p3(f"HPS_ENET_TX_DATA[2]", "PIN_F21")
  print_3p3(f"HPS_ENET_TX_DATA[3]", "PIN_F19")
  print_3p3(f"HPS_ENET_RX_DV", "PIN_K17")
  print_3p3(f"HPS_ENET_RX_DATA[0]", "PIN_A21")
  print_3p3(f"HPS_ENET_RX_DATA[1]", "PIN_B20")
  print_3p3(f"HPS_ENET_RX_DATA[2]", "PIN_B18")
  print_3p3(f"HPS_ENET_RX_DATA[3]", "PIN_D21")
  print_3p3(f"HPS_ENET_RX_CLK", "PIN_G20")
  print_3p3(f"HPS_ENET_RESET_N", "PIN_E18")
  print_3p3(f"HPS_ENET_MDIO", "PIN_E21")
  print_3p3(f"HPS_ENET_MDC", "PIN_B21")
  print_3p3(f"HPS_ENET_INT_N", "PIN_C19")
  print_3p3(f"HPS_ENET_GTX_CLK", "PIN_H19")
print_hps_enet()

def print_hps_uart():
  print(f"#============================================================")
  print(f"# HPS_UART")
  print(f"#============================================================")
  print_3p3(f"HPS_UART_RX", "PIN_B25")
  print_3p3(f"HPS_UART_TX", "PIN_C25")
  print_3p3(f"HPS_CONV_USB_N", "PIN_B15")
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
  print_3p3(f"HPS_SD_CLK", "PIN_A16")
  print_3p3(f"HPS_SD_CMD", "PIN_F18")
  print_3p3(f"HPS_SD_DATA[0]", "PIN_G18")
  print_3p3(f"HPS_SD_DATA[1]", "PIN_C17")
  print_3p3(f"HPS_SD_DATA[2]", "PIN_D17")
  print_3p3(f"HPS_SD_DATA[3]", "PIN_B16")
print_hps_sdcard()

def print_hps_usb():
  print(f"#============================================================")
  print(f"# HPS_USB")
  print(f"#============================================================")
  print_3p3(f"HPS_USB_CLKOUT", "PIN_N16")
  hps_usb_data = ["PIN_E16", "PIN_G16", "PIN_D16", "PIN_D14", "PIN_A15",
                  "PIN_C14", "PIN_D15", "PIN_M17"]
  for a in range(len(hps_usb_data)):
    print_3p3(f"HPS_USB_DATA[{a}]", hps_usb_data[a])
  print_3p3(f"HPS_USB_DIR", "PIN_E14")
  print_3p3(f"HPS_USB_NXT", "PIN_A14")
  print_3p3(f"HPS_USB_RESET", "PIN_G17")
  print_3p3(f"HPS_USB_STP", "PIN_C15")
print_hps_usb()

def print_hps_gsensor():
  print(f"#============================================================")
  print(f"# HPS_GSENSOR")
  print(f"#============================================================")
  print_3p3(f"HPS_GSENSOR_INT", "PIN_B22")
print_hps_gsensor()

def print_hps_ltc():
  print(f"#============================================================")
  print(f"# HPS_LTC")
  print(f"#============================================================")
  print_3p3(f"HPS_LTC_GPIO", "PIN_H17")
print_hps_ltc()

def print_hps_spim():
  print(f"#============================================================")
  print(f"# HPS_SPIM")
  print(f"#============================================================")
  print_3p3(f"HPS_SPIM_CLK", "PIN_C23")
  print_3p3(f"HPS_SPIM_MISO", "PIN_E24")
  print_3p3(f"HPS_SPIM_MOSI", "PIN_D22")
  print_3p3(f"HPS_SPIM_SS", "PIN_D24")
print_hps_spim()

def print_lcd():
  print(f"#============================================================")
  print(f"# LCD")
  print(f"#============================================================")
  print_3p3(f"HPS_LCM_D_C", "PIN_C18")
  print_3p3(f"HPS_LCM_RST_N", "PIN_E17")
  print_3p3(f"HPS_LCM_SPIM_CLK", "PIN_A23")
  print_3p3(f"HPS_LCM_SPIM_MOSI", "PIN_C22")
  print_3p3(f"HPS_LCM_SPIM_SS", "PIN_H20")
print_lcd()

def print_config():
  print(f"#============================================================")
  print(f"# CONFIGURE")
  print(f"#============================================================")
  print(f"set_global_assignment -name MIN_CORE_JUNCTION_TEMP 0")
  print(f"set_global_assignment -name MAX_CORE_JUNCTION_TEMP 85")
print_config()

