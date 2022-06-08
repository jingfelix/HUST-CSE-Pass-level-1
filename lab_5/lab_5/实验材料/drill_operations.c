/*
 * Student ID: XXX
 * Author: XXX
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int act(int fd, char code)
{
	ssize_t bytes = 0;

	bytes = write(fd, &code, 1);
	if (bytes <= 0) {
		perror("[-] write");
		return EXIT_FAILURE;
	}

	return EXIT_SUCCESS;
}

int main(void)
{
	int ret = EXIT_FAILURE;

	//printf("begin as: uid=%d, euid=%d\n", getuid(), geteuid());

	// MDL: Use act function to implement the following commands
	// MDL: echo '1' > /sys/kernel/debug/drill/drill_act
	// MDL: echo '2' > /sys/kernel/debug/drill/drill_act
	// MDL: echo '3' > /sys/kernel/debug/drill/drill_act
	// MDL: echo '4' > /sys/kernel/debug/drill/drill_act

	return ret;
}
