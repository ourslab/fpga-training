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

def print_de2():
  print(f"#============================================================")
  print(f"# DE2-115")
  print(f"#============================================================")
  print(f"set_global_assignment -name FAMILY \"Cyclone IV\"")
  print(f"set_global_assignment -name DEVICE EP4CE115F29C7N")
  print(f"set_global_assignment -name TOP_LEVEL_ENTITY {TOP_LEVEL_ENTITY}")
  print(f"set_global_assignment -name PROJECT_OUTPUT_DIRECTORY output_files")
  print(f"set_global_assignment -name EDA_SIMULATION_TOOL \"ModelSim-Altera (VHDL)\"")
print_de2()

def print_clock():
  print(f"#============================================================")
  print(f"# CLOCK")
  print(f"#============================================================")
  print_3p3(f"CLOCK_50", "PIN_Y2")
  print_3p3(f"CLOCK2_50M", "PIN_AG14")
  print_3p3(f"CLOCK3_50M", "PIN_AG15") # Depending on JP6
  print_3p3(f"SMA_CLKOUT", "PIN_AE23") # Depending on JP6
  print_3p3(f"SMA_CLKIN", "PIN_AH14")
print_clock()

def print_sw():
  print(f"#============================================================")
  print(f"# SW")
  print(f"#============================================================")
  sw_pins = ["PIN_AB28", "PIN_AC28", "PIN_AC27", "PIN_AD27", "PIN_AB27",
             "PIN_AC26", "PIN_AD26", "PIN_AB26", "PIN_AC25", "PIN_AB25",
             "PIN_AC24", "PIN_AB24", "PIN_AB23", "PIN_AA24", "PIN_AA23",
             "PIN_AA22", "PIN_Y24", "PIN_Y23"]
  print_2p5(f"SW[0]", sw_pins[0]) # Depending on JP7
  print_2p5(f"SW[1]", sw_pins[1]) # Depending on JP7
  print_2p5(f"SW[2]", sw_pins[2]) # Depending on JP7
  print_2p5(f"SW[3]", sw_pins[3]) # Depending on JP7
  print_2p5(f"SW[4]", sw_pins[4]) # Depending on JP7
  print_2p5(f"SW[5]", sw_pins[5]) # Depending on JP7
  print_2p5(f"SW[6]", sw_pins[6]) # Depending on JP7
  print_2p5(f"SW[7]", sw_pins[7]) # Depending on JP7
  print_2p5(f"SW[8]", sw_pins[8]) # Depending on JP7
  print_2p5(f"SW[9]", sw_pins[9]) # Depending on JP7
  print_2p5(f"SW[10]", sw_pins[10]) # Depending on JP7
  print_2p5(f"SW[11]", sw_pins[11]) # Depending on JP7
  print_2p5(f"SW[12]", sw_pins[12]) # Depending on JP7
  print_2p5(f"SW[13]", sw_pins[13]) # Depending on JP7
  print_2p5(f"SW[14]", sw_pins[14]) # Depending on JP7
  print_2p5(f"SW[15]", sw_pins[15]) # Depending on JP7
  print_2p5(f"SW[16]", sw_pins[16]) # Depending on JP7
  print_2p5(f"SW[17]", sw_pins[17]) # Depending on JP7
print_sw()

def print_key():
  print(f"#============================================================")
  print(f"# KEY")
  print(f"#============================================================")
  key_pins = ["PIN_M23", "PIN_M21", "PIN_N21", "PIN_R24"]
  print_2p5(f"KEY[0]", key_pins[0]) # Depending on JP7
  print_2p5(f"KEY[1]", key_pins[1]) # Depending on JP7
  print_2p5(f"KEY[2]", key_pins[2]) # Depending on JP7
  print_2p5(f"KEY[3]", key_pins[3]) # Depending on JP7
print_key()

def print_led():
  print(f"#============================================================")
  print(f"# LEDR")
  print(f"#============================================================")
  ledr_pins = ["PIN_G19", "PIN_F19", "PIN_E19", "PIN_F21", "PIN_F18",
               "PIN_E18", "PIN_J19", "PIN_H19", "PIN_J17", "PIN_G17",
               "PIN_J15", "PIN_H16", "PIN_J16", "PIN_H17", "PIN_F15",
               "PIN_G15", "PIN_G16", "PIN_H15"]
  print_2p5(f"LEDR[0]", ledr_pins[0])
  print_2p5(f"LEDR[1]", ledr_pins[1])
  print_2p5(f"LEDR[2]", ledr_pins[2])
  print_2p5(f"LEDR[3]", ledr_pins[3])
  print_2p5(f"LEDR[4]", ledr_pins[4])
  print_2p5(f"LEDR[5]", ledr_pins[5])
  print_2p5(f"LEDR[6]", ledr_pins[6])
  print_2p5(f"LEDR[7]", ledr_pins[7])
  print_2p5(f"LEDR[8]", ledr_pins[8])
  print_2p5(f"LEDR[9]", ledr_pins[9])
  print_2p5(f"LEDR[10]", ledr_pins[10])
  print_2p5(f"LEDR[11]", ledr_pins[11])
  print_2p5(f"LEDR[12]", ledr_pins[12])
  print_2p5(f"LEDR[13]", ledr_pins[13])
  print_2p5(f"LEDR[14]", ledr_pins[14])
  print_2p5(f"LEDR[15]", ledr_pins[15])
  print_2p5(f"LEDR[16]", ledr_pins[16])
  print_2p5(f"LEDR[17]", ledr_pins[17])
  print(f"#============================================================")
  print(f"# LEDG")
  print(f"#============================================================")
  ledg_pins = ["PIN_E21", "PIN_E22", "PIN_E25", "PIN_E24", "PIN_H21",
                    "PIN_G20", "PIN_G22", "PIN_G21", "PIN_F17"]
  print_2p5(f"LEDG[0]", ledg_pins[0])
  print_2p5(f"LEDG[1]", ledg_pins[1])
  print_2p5(f"LEDG[2]", ledg_pins[2])
  print_2p5(f"LEDG[3]", ledg_pins[3])
  print_2p5(f"LEDG[4]", ledg_pins[4])
  print_2p5(f"LEDG[5]", ledg_pins[5])
  print_2p5(f"LEDG[6]", ledg_pins[6])
  print_2p5(f"LEDG[7]", ledg_pins[7])
  print_2p5(f"LEDG[8]", ledg_pins[8])
print_led()

def print_hex():
  print(f"#============================================================")
  print(f"# HEX")
  print(f"#============================================================")
  hex_pins = [["PIN_G18", "PIN_F22", "PIN_E17", "PIN_L26", "PIN_L25", "PIN_J22", "PIN_H22"],
              ["PIN_M24", "PIN_Y22", "PIN_W21", "PIN_W22", "PIN_W25", "PIN_U23", "PIN_U24"],
              ["PIN_AA25", "PIN_AA26", "PIN_Y25", "PIN_W26", "PIN_Y26", "PIN_W27", "PIN_W28"],
              ["PIN_V21", "PIN_U21", "PIN_AB20", "PIN_AA21", "PIN_AD24", "PIN_AF23", "PIN_Y19"],
              ["PIN_AB19", "PIN_AA19", "PIN_AG21", "PIN_AH21", "PIN_AE19", "PIN_AF19", "PIN_AE18"],
              ["PIN_AD18", "PIN_AC18", "PIN_AB18", "PIN_AH19", "PIN_AG19", "PIN_AF18", "PIN_AH18"],
              ["PIN_AA17", "PIN_AB16", "PIN_AA16", "PIN_AB17", "PIN_AB15", "PIN_AA15", "PIN_AC17"],
              ["PIN_AD17", "PIN_AE17", "PIN_AG17", "PIN_AH17", "PIN_AF17", "PIN_AG18", "PIN_AA14"]]
  for a in range(8):
    for b in range(7):
      print_2p5(f"HEX{a}[{b}]", hex_pins[a][b])
print_hex()

def print_lcd():
  print(f"#============================================================")
  print(f"# LCD")
  print(f"#============================================================")
  lcd_data_pins = ["PIN_L3", "PIN_L1", "PIN_L2", "PIN_K7", "PIN_K1", 
                   "PIN_K2", "PIN_M3", "PIN_M5"]
  print_3p3(f"LCD_DATA[0]", lcd_data_pins[0])
  print_3p3(f"LCD_DATA[1]", lcd_data_pins[1])
  print_3p3(f"LCD_DATA[2]", lcd_data_pins[2])
  print_3p3(f"LCD_DATA[3]", lcd_data_pins[3])
  print_3p3(f"LCD_DATA[4]", lcd_data_pins[4])
  print_3p3(f"LCD_DATA[5]", lcd_data_pins[5])
  print_3p3(f"LCD_DATA[6]", lcd_data_pins[6])
  print_3p3(f"LCD_DATA[7]", lcd_data_pins[7])
  print_3p3(f"LCD_EN", "PIN_L4")
  print_3p3(f"LCD_RW", "PIN_M1")
  print_3p3(f"LCD_RS", "PIN_M2")
  print_3p3(f"LCD_ON", "PIN_L5")
  print_3p3(f"LCD_BLON", "PIN_L6")
print_lcd()

def print_hsmc():
  print(f"#============================================================")
  print(f"# HSMC")
  print(f"#============================================================")
  print_3p3(f"HSMC_CLKIN0", "PIN_AH15") # Depending on JP6
  print_2p5(f"HSMC_CLKIN_N1", "PIN_J28") # Depending on JP7
  print_2p5(f"HSMC_CLKIN_N2", "PIN_Y28") # Depending on JP7
  print_2p5(f"HSMC_CLKIN_P1", "PIN_J27") # Depending on JP7
  print_2p5(f"HSMC_CLKIN_P2", "PIN_Y27") # Depending on JP7
  print_2p5(f"HSMC_CLKOUT0", "PIN_AD28") # Depending on JP7
  print_2p5(f"HSMC_CLKOUT_N1", "PIN_G24") # Depending on JP7
  print_2p5(f"HSMC_CLKOUT_N2", "PIN_V24") # Depending on JP7
  print_2p5(f"HSMC_CLKOUT_P1", "PIN_G23") # Depending on JP7
  print_2p5(f"HSMC_CLKOUT_P2", "PIN_V23") # Depending on JP7
  hsmc_d_pins = ["PIN_AE26", "PIN_AE28", "PIN_AE27", "PIN_AF27"]
  for a in range(4):
    print_2p5(f"HSMC_D[{a}]", hsmc_d_pins[a]) # Depending on JP7
  hsmc_rx_d_n_pins = ["PIN_F25", "PIN_C27", "PIN_E26", "PIN_G26", "PIN_H26",
                      "PIN_K26", "PIN_L24", "PIN_M26", "PIN_R26", "PIN_T26",
                      "PIN_U26", "PIN_L22", "PIN_N26", "PIN_P26", "PIN_R21",
                      "PIN_R23", "PIN_T22"]
  for a in range(17):
    print_2p5(f"HSMC_RX_D_N[{a}]", hsmc_rx_d_n_pins[a]) # Depending on JP7
  hsmc_rx_d_p_pins = ["PIN_F24", "PIN_D26", "PIN_F26", "PIN_G25", "PIN_H25",
                      "PIN_K25", "PIN_L23", "PIN_M25", "PIN_R25", "PIN_T25",
                      "PIN_U25", "PIN_L21", "PIN_N25", "PIN_P25", "PIN_P21",
                      "PIN_R22", "PIN_T21"]
  for a in range(17):
    print_2p5(f"HSMC_RX_D_P[{a}]", hsmc_rx_d_p_pins[a]) # Depending on JP7
  hsmc_tx_d_n_pins = ["PIN_D28", "PIN_E28", "PIN_F28", "PIN_G28", "PIN_K28",
                      "PIN_M28", "PIN_K22", "PIN_H24", "PIN_J24", "PIN_P28",
                      "PIN_J26", "PIN_L28", "PIN_V26", "PIN_R28", "PIN_U28",
                      "PIN_V28", "PIN_V22"]
  for a in range(17):
    print_2p5(f"HSMC_TX_D_N[{a}]", hsmc_tx_d_n_pins[a]) # Depending on JP7
  hsmc_tx_d_p_pins = ["PIN_D27", "PIN_E27", "PIN_F27", "PIN_G27", "PIN_K27",
                      "PIN_M27", "PIN_K21", "PIN_H23", "PIN_J23", "PIN_P27",
                      "PIN_J25", "PIN_L27", "PIN_V25", "PIN_R27", "PIN_U27",
                      "PIN_V27", "PIN_U22"]
  for a in range(17):
    print_2p5(f"HSMC_TX_D_P[{a}]", hsmc_tx_d_p_pins[a]) # Depending on JP7
print_hsmc()

def print_gpio():
  print(f"#============================================================")
  print(f"# GPIO")
  print(f"#============================================================")
  gpio_pins = ["PIN_AB22", "PIN_AC15", "PIN_AB21", "PIN_Y17", "PIN_AC21",
               "PIN_Y16", "PIN_AD21", "PIN_AE16", "PIN_AD15", "PIN_AE15", 
               "PIN_AC19", "PIN_AF16", "PIN_AD19", "PIN_AF15", "PIN_AF24",
               "PIN_AE21", "PIN_AF25", "PIN_AC22", "PIN_AE22", "PIN_AF21", 
               "PIN_AF22", "PIN_AD22", "PIN_AG25", "PIN_AD25", "PIN_AH25",
               "PIN_AE25", "PIN_AG22", "PIN_AE24", "PIN_AH22", "PIN_AF26",
               "PIN_AE20", "PIN_AG23", "PIN_AF20", "PIN_AH26", "PIN_AH23", "PIN_AG26"]
  for a in range(36):
    print_3p3(f"GPIO[{a}]", gpio_pins[a]) # Depending on JP6
  ex_io_pins = ["PIN_J10", "PIN_J14", "PIN_H13", "PIN_H14", "PIN_F14",
                "PIN_E10", "PIN_D9"]
  for a in range(7):
    print_3p3(f"EX_IO[{a}]", ex_io_pins[a])
print_gpio()

def print_audio():
  print(f"#============================================================")
  print(f"# AUD")
  print(f"#============================================================")
  print_3p3(f"AUD_ADCLRCK", "PIN_C2")
  print_3p3(f"AUD_ADCDAT", "PIN_D2")
  print_3p3(f"AUD_DACLRCK", "PIN_E3")
  print_3p3(f"AUD_DACDAT", "PIN_D1")
  print_3p3(f"AUD_XCK", "PIN_E1")
  print_3p3(f"AUD_BCLK", "PIN_F2")
print_audio()

def print_i2c():
  print(f"#============================================================")
  print(f"# I2C")
  print(f"#============================================================")
  print_3p3(f"I2C_SCLK", "PIN_B7")
  print_3p3(f"I2C_SDAT", "PIN_A8")
print_i2c()

def print_vga():
  print(f"#============================================================")
  print(f"# VGA")
  print(f"#============================================================")
  vga_r = ["PIN_E12", "PIN_E11", "PIN_D10", "PIN_F12", "PIN_G10", "PIN_J12", "PIN_H8", "PIN_H10"]
  for a in range(len(vga_r)):
    print_3p3(f"VGA_R[{a}]", vga_r[a])
  vga_g = ["PIN_G8" , "PIN_G11", "PIN_F8", "PIN_H12", "PIN_C8", "PIN_B8", "PIN_F10", "PIN_C9"]
  for a in range(len(vga_g)):
    print_3p3(f"VGA_G[{a}]", vga_g[a])
  vga_b = ["PIN_B10", "PIN_A10", "PIN_C11", "PIN_B11", "PIN_A11", "PIN_C12", "PIN_D11", "PIN_D12"]
  for a in range(len(vga_b)):
    print_3p3(f"VGA_B[{a}]", vga_b[a])
  print_3p3(f"VGA_CLK", "PIN_A12")
  print_3p3(f"VGA_BLANK_N", "PIN_F11")
  print_3p3(f"VGA_HS", "PIN_G13")
  print_3p3(f"VGA_VS", "PIN_C13")
  print_3p3(f"VGA_SYNC_N", "PIN_C10")
print_vga()

def print_uart():
  print(f"#============================================================")
  print(f"# UART")
  print(f"#============================================================")
  print_3p3(f"UART_RXD", "PIN_G12") 
  print_3p3(f"UART_TXD", "PIN_G9")
  print_3p3(f"UART_CTS", "PIN_G14")
  print_3p3(f"UART_RTS", "PIN_J13") 
print_uart()

def print_TVDecoder():
  print(f"#============================================================")
  print(f"# TVDecoder")
  print(f"#============================================================")
  print_3p3(f"TD_DATA[0]", "PIN_E8")
  print_3p3(f"TD_DATA[1]", "PIN_A7")
  print_3p3(f"TD_DATA[2]", "PIN_D8")
  print_3p3(f"TD_DATA[3]", "PIN_C7")
  print_3p3(f"TD_DATA[4]", "PIN_D7")
  print_3p3(f"TD_DATA[5]", "PIN_D6")
  print_3p3(f"TD_DATA[6]", "PIN_E7")
  print_3p3(f"TD_DATA[7]", "PIN_F7")
  print_3p3(f"TD_HS", "PIN_E5")
  print_3p3(f"TD_VS", "PIN_E4")
  print_3p3(f"TD_CLK27", "PIN_B14")
  print_3p3(f"TD_RESET_N", "PIN_G7")
print_TVDecoder()

def print_ir():
  print(f"#============================================================")
  print(f"# IR")
  print(f"#============================================================")
  print_3p3(f"IR_RX", "PIN_Y15")
print_ir()


def print_sram():
  print(f"#============================================================")
  print(f"# SRAM")
  print(f"#============================================================")
  sram_addr_pins = ["PIN_AB7", "PIN_AD7", "PIN_AE7", "PIN_AC7", "PIN_AB6", 
                    "PIN_AE6", "PIN_AB5", "PIN_AC5", "PIN_AF5", "PIN_T7",
                    "PIN_AF2", "PIN_AD3", "PIN_AB4", "PIN_AC3", "PIN_AA4",
                    "PIN_AB11", "PIN_AC11", "PIN_AB9", "PIN_AB8", "PIN_T8"]
  for a in range(20):
    print_3p3(f"SRAM_ADDR[{a}]", sram_addr_pins[a])
  sram_dq_pins = ["PIN_AH3", "PIN_AF4", "PIN_AG4", "PIN_AH4", "PIN_AF6",
                  "PIN_AG6", "PIN_AH6", "PIN_AF7", "PIN_AD1", "PIN_AD2",
                  "PIN_AE2", "PIN_AE1", "PIN_AE3", "PIN_AE4", "PIN_AF3", "PIN_AG3"]
  for a in range(16):
    print_3p3(f"SRAM_DQ[{a}]", sram_dq_pins[a])
  print_3p3(f"SRAM_OE_N", "PIN_AD5")
  print_3p3(f"SRAM_WE_N", "PIN_AE8")
  print_3p3(f"SRAM_CE_N", "PIN_AF8")
  print_3p3(f"SRAM_LB_N", "PIN_AD4")
  print_3p3(f"SRAM_UB_N", "PIN_AC4")
print_sram()

def print_dram():
  print(f"#============================================================")
  print(f"# DRAM")
  print(f"#============================================================")
  dram_addr_pins = ["PIN_R6", "PIN_V8", "PIN_U8", "PIN_P1", "PIN_V5",
                    "PIN_W8", "PIN_W7", "PIN_AA7", "PIN_Y5", "PIN_Y6",
                    "PIN_R5", "PIN_AA5", "PIN_Y7"]
  for a in range(13):
    print_3p3(f"DRAM_ADDR[{a}]", dram_addr_pins[a])
  dram_dq_pins = ["PIN_W3", "PIN_W2", "PIN_V4", "PIN_W1", "PIN_V3",
                  "PIN_V2", "PIN_V1", "PIN_U3", "PIN_Y3", "PIN_Y4",
                  "PIN_AB1", "PIN_AA3", "PIN_AB2", "PIN_AC1", "PIN_AB3",
                  "PIN_AC2", "PIN_M8", "PIN_L8", "PIN_P2", "PIN_N3",
                  "PIN_N4", "PIN_M4", "PIN_M7", "PIN_L7", "PIN_U5",
                  "PIN_R7", "PIN_R1", "PIN_R2", "PIN_R3", "PIN_T3",
                  "PIN_U4", "PIN_U1"]
  for a in range(32):
    print_3p3(f"DRAM_DQ[{a}]", dram_dq_pins[a])
  print_3p3(f"DRAM_BA[0]", "PIN_U7")
  print_3p3(f"DRAM_BA[1]", "PIN_R4")
  print_3p3(f"DRAM_DQM[0]", "PIN_U2")
  print_3p3(f"DRAM_DQM[1]", "PIN_W4")
  print_3p3(f"DRAM_DQM[2]", "PIN_K8")
  print_3p3(f"DRAM_DQM[3]", "PIN_N8")
  print_3p3(f"DRAM_RAS_N", "PIN_U6")
  print_3p3(f"DRAM_CAS_N", "PIN_V7")
  print_3p3(f"DRAM_CKE", "PIN_AA6")
  print_3p3(f"DRAM_CLK", "PIN_AE5")
  print_3p3(f"DRAM_WE_N", "PIN_V6")
  print_3p3(f"DRAM_CS_N", "PIN_T4")
print_dram() 

def print_flash():
  print(f"#============================================================")
  print(f"# FLASH (TODO)")
  print(f"#============================================================")
print_flash()

def print_eep():
  print(f"#============================================================")
  print(f"# EEP (TODO)")
  print(f"#============================================================")
print_eep()

def print_sd():
  print(f"#============================================================")
  print(f"# SD (TODO)")
  print(f"#============================================================")
print_sd()

def print_ps2():
  print(f"#============================================================")
  print(f"# PS2")
  print(f"#============================================================")
  print_3p3(f"PS2_CLK", "PIN_G6")
  print_3p3(f"PS2_DAT", "PIN_H5")
  print_3p3(f"PS2_CLK2", "PIN_G5")
  print_3p3(f"PS2_DAT2", "PIN_F5")
print_ps2()

def print_otg():
  print(f"#============================================================")
  print(f"# OTG")
  print(f"#============================================================")
  print_3p3(f"OTG_ADDR[0]", "PIN_H7")
  print_3p3(f"OTG_ADDR[1]", "PIN_C3")
  print_3p3(f"OTG_DATA[0]", "PIN_J6")
  print_3p3(f"OTG_DATA[1]", "PIN_K4")
  print_3p3(f"OTG_DATA[2]", "PIN_J5")
  print_3p3(f"OTG_DATA[3]", "PIN_K3")
  print_3p3(f"OTG_DATA[4]", "PIN_J4")
  print_3p3(f"OTG_DATA[5]", "PIN_J3")
  print_3p3(f"OTG_DATA[6]", "PIN_J7")
  print_3p3(f"OTG_DATA[7]", "PIN_H6")
  print_3p3(f"OTG_DATA[8]", "PIN_H3")
  print_3p3(f"OTG_DATA[9]", "PIN_H4")
  print_3p3(f"OTG_DATA[10]", "PIN_G1")
  print_3p3(f"OTG_DATA[11]", "PIN_G2")
  print_3p3(f"OTG_DATA[12]", "PIN_G3")
  print_3p3(f"OTG_DATA[13]", "PIN_F1")
  print_3p3(f"OTG_DATA[14]", "PIN_F3")
  print_3p3(f"OTG_DATA[15]", "PIN_G4")
  print_3p3(f"OTG_CS_N", "PIN_A3")
  print_3p3(f"OTG_RD_N", "PIN_B3")
  print_3p3(f"OTG_WR_N", "PIN_A4")
  print_3p3(f"OTG_RST_N", "PIN_C5")
  print_3p3(f"OTG_INT", "PIN_D5")
print_otg()

def print_enet():
  print(f"#============================================================")
  print(f"# ENET")
  print(f"#============================================================")
  print_2p5(f"ENET0_GTX_CLK", "PIN_A17")
  print_2p5(f"ENET0_INT_N", "PIN_A21")
  print_3p3(f"ENET0_LINK100", "PIN_C14")
  print_2p5(f"ENET0_MDC", "PIN_C20")
  print_2p5(f"ENET0_MDIO", "PIN_B21")
  print_2p5(f"ENET0_RST_N", "PIN_C19")
  print_2p5(f"ENET0_RX_CLK", "PIN_A15")
  print_2p5(f"ENET0_RX_COL", "PIN_E15")
  print_2p5(f"ENET0_RX_CRS", "PIN_D15")
  print_2p5(f"ENET0_RX_DATA[0]", "PIN_C16")
  print_2p5(f"ENET0_RX_DATA[1]", "PIN_D16")
  print_2p5(f"ENET0_RX_DATA[2]", "PIN_D17")
  print_2p5(f"ENET0_RX_DATA[3]", "PIN_C15")
  print_2p5(f"ENET0_RX_DV", "PIN_C17")
  print_2p5(f"ENET0_RX_ER", "PIN_D18")
  print_2p5(f"ENET0_TX_CLK", "PIN_B17")
  print_2p5(f"ENET0_TX_DATA[0]", "PIN_C18")
  print_2p5(f"ENET0_TX_DATA[1]", "PIN_D19")
  print_2p5(f"ENET0_TX_DATA[2]", "PIN_A19")
  print_2p5(f"ENET0_TX_DATA[3]", "PIN_B19")
  print_2p5(f"ENET0_TX_EN", "PIN_A18")
  print_2p5(f"ENET0_TX_ER", "PIN_B18")
  print_2p5(f"ENET1_GTX_CLK", "PIN_C23")
  print_2p5(f"ENET1_INT_N", "PIN_D24")
  print_3p3(f"ENET1_LINK100", "PIN_D13")
  print_2p5(f"ENET1_MDC", "PIN_D23")
  print_2p5(f"ENET1_MDIO", "PIN_D25")
  print_2p5(f"ENET1_RST_N", "PIN_D22")
  print_2p5(f"ENET1_RX_CLK", "PIN_B15")
  print_2p5(f"ENET1_RX_COL", "PIN_B22")
  print_2p5(f"ENET1_RX_CRS", "PIN_D20")
  print_2p5(f"ENET1_RX_DATA[0]", "PIN_B23")
  print_2p5(f"ENET1_RX_DATA[1]", "PIN_C21")
  print_2p5(f"ENET1_RX_DATA[2]", "PIN_A23")
  print_2p5(f"ENET1_RX_DATA[3]", "PIN_D21")
  print_2p5(f"ENET1_RX_DV", "PIN_A22")
  print_2p5(f"ENET1_RX_ER", "PIN_C24")
  print_2p5(f"ENET1_TX_CLK", "PIN_C22")
  print_2p5(f"ENET1_TX_DATA[0]", "PIN_C25")
  print_2p5(f"ENET1_TX_DATA[1]", "PIN_A26")
  print_2p5(f"ENET1_TX_DATA[2]", "PIN_B26")
  print_2p5(f"ENET1_TX_DATA[3]", "PIN_C26")
  print_2p5(f"ENET1_TX_EN", "PIN_B25")
  print_2p5(f"ENET1_TX_ER", "PIN_A25")
  print_3p3(f"ENETCLK_25", "PIN_A14")
print_enet()

def print_config():
  print(f"#============================================================")
  print(f"# CONFIGURE")
  print(f"#============================================================")
  print(f"set_global_assignment -name MIN_CORE_JUNCTION_TEMP 0")
  print(f"set_global_assignment -name MAX_CORE_JUNCTION_TEMP 85")
print_config()


