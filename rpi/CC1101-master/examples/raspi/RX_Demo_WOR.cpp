#include "cc1100_raspi.h"
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#include <sys/select.h>

#include <getopt.h>
#include <wiringPi.h>
#include <wiringPiSPI.h>

#define PACKAGE    "CC1100 SW"
#define VERSION_SW "0.9.0"

//--------------------------[Global CC1100 variables]--------------------------
uint8_t Tx_fifo[FIFOBUFFER], Rx_fifo[FIFOBUFFER], Patable[8];
uint8_t My_addr, Tx_addr, Rx_addr, Pktlen, pktlen, Lqi, Rssi;
uint8_t rx_addr,sender,lqi;
 int8_t rssi_dbm;


int cc1100_freq_select, cc1100_mode_select, cc1100_channel_select;
uint8_t cc1100_debug = 0;								//set CC1100 lib in no-debug output mode
uint8_t cc1100_wor_enable_flag = 0;

CC1100 cc1100;

//-------------------------- [End] --------------------------

void print_help(int exval) {
	printf("%s,%s by CW\r\n", PACKAGE, VERSION_SW);
	printf("%s [-h] [-V] [-v] [-a My_Addr] [-c channel] [-f frequency] \r\n", PACKAGE);
	printf("          [-m modulation]\n\r\n\r");
	printf("  -h              			print this help and exit\r\n");
	printf("  -V              			print version and exit\r\n\r\n");
	printf("  -v              			set verbose flag\r\n");
	printf("  -a my address [1-255] 		set my address\r\n\r\n");
	printf("  -c channel 	[1-255] 		set transmit channel\r\n");
	printf("  -f frequency  [315,434,868,915]  	set ISM band\r\n\r\n");
	printf("  -m modulation [100,250,500] 		set modulation\r\n\r\n");

	exit(exval);
}


//|============================ Main ============================|
int main(int argc, char *argv[]) {
	//------------- command line option parser -------------------
	int opt;
	// no arguments given
	if(argc == 1) {
		fprintf(stderr, "This program needs arguments....\n\r\n\r");
		print_help(1);
	}

	while((opt = getopt(argc, argv, "hVva:c:f:m:")) != -1) {
		switch(opt) {
		case 'h':
			print_help(0);
			break;
		case 'V':
			printf("%s %s\n\n", PACKAGE, VERSION_SW);
			exit(0);
			break;
		case 'v':
			printf("%s: Verbose option is set `%c'\n", PACKAGE, optopt);
			cc1100_debug = 1;
			break;
		case 'a':
			My_addr = atoi (optarg);
			break;
		case 'c':
			cc1100_channel_select = atoi (optarg);
			break;
		case 'f':
			cc1100_freq_select = atoi (optarg);
			switch(cc1100_freq_select){
				case 315:
					cc1100_freq_select = 1;
					break;
				case 434:
					cc1100_freq_select = 2;
					break;
				case 868:
					cc1100_freq_select = 3;
					break;
				case 915:
					cc1100_freq_select = 4;
					break;
				}
			break;
		case 'm':
			cc1100_mode_select = atoi (optarg);
			switch(cc1100_mode_select){
				case 1:
					cc1100_mode_select = 1;
					break;
				case 38:
					cc1100_mode_select = 2;
					break;

				case 100:
					cc1100_mode_select = 3;
					break;
				case 250:
					cc1100_mode_select = 4;
					break;
				case 500:
					cc1100_mode_select = 5;
					break;
				}
				break;
		case ':':
				fprintf(stderr, "%s: Error - Option `%c' needs a value\n\n", PACKAGE, optopt);
				print_help(1);
				break;
		case '?':
				fprintf(stderr, "%s: Error - No such option: `%c'\n\n", PACKAGE, optopt);
				print_help(1);
		}
	}

	// print all remaining options
	for(; optind < argc; optind++)
		printf("argument: %s\n", argv[optind]);

	//------------- welcome message ------------------------
	printf("Raspberry CC1101 SPI Library test\n");

	//------------- hardware setup ------------------------

	wiringPiSetup();			               //setup wiringPi library

	cc1100.begin(My_addr);			           //setup cc1000 RF IC
	cc1100.sidle();
	cc1100.set_output_power_level(0);          //set PA level

	cc1100.spi_read_burst(PATABLE_BURST, Patable, 8); //backup selected PA Table settings
	
	cc1100.show_main_settings();               //shows setting debug messages to UART
    cc1100.show_register_settings();

	cc1100.wor_enable();                       //enable WOR mode
    cc1100_wor_enable_flag = 1;                //set WOR enable flag
	//------------------------- Main Loop ------------------------
	for (;;) {
		delay(1);                              //delay to reduce system load
		
		if (cc1100.packet_available() == TRUE) //checks if a packed is available
		{
		  if(cc1100_wor_enable_flag == 1){                                     //only disable and update PA Table if CC1101 is in WOR mode
            //Serial.println(F("update PA_Table: "));
            cc1100_wor_enable_flag = 0;
            cc1100.spi_write_burst(PATABLE_BURST, Patable, 8);                 //bugfix, CC1101 PA Table is lost after SLEEP mode
          }

		  cc1100.get_payload(Rx_fifo, pktlen, rx_addr, sender, rssi_dbm, lqi); //stores the payload data to Rx_fifo
		  cc1100.wor_reset();
		  cc1100_wor_enable_flag = 1;
		}
	}
	return 0;
}
//-------------------- END OF MAIN --------------------------------
