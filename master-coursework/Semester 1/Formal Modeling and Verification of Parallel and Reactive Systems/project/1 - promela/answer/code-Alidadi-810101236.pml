#define PACKET_SIZE 4;

chan blueTooth [3] = [0] of {int};
chan BUS [3] = [0] of {int};
chan info [3] = [100] of {int}; //asynch channels between the 3 radios and the master

proctype Sensor(byte i) {
	int data = 1;
	do
	:: true -> blueTooth[i]!data;
	od
}

proctype CPU (byte i) {
	int sensorData;
	int receivedData = 0;
	do
	:: receivedData < PACKET_SIZE -> blueTooth[i]?sensorData; printf("%d\n", sensorData); receivedData++;
	:: else -> BUS[i]!4; receivedData = 0;
	od
}

proctype Radio(byte i) {
	int comData;
	do
	:: true -> BUS[i]?comData; info[i]!comData;
	od
}

proctype Master() {
	int turn = 0;
	int result;
	do
	:: turn == 0 -> info[0]?result; turn++; turn = turn%3;
	:: turn == 1 -> info[1]?result; turn++; turn = turn%3;
	:: turn == 2 -> info[2]?result; turn++; turn = turn%3;
	od
}

init {
	run Sensor(0);
	run Sensor(1);
	run Sensor(2);
	run CPU(0);
	run CPU(1);
	run CPU(2);
	run Radio(0);
	run Radio(1);
	run Radio(2);
	run Master();
}