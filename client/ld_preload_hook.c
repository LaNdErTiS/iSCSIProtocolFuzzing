#define _GNU_SOURCE
#include <dlfcn.h>
#include <sys/socket.h>
#include <unistd.h>
#include <time.h>

ssize_t (*orig_read)(int fildes, void *buf, size_t nbyte);

ssize_t read(int fildes, void *buf, size_t nbyte) {

read()
    if(!orig_read) orig_read = dlsym(RTLD_NEXT, "read");

    printf("WAS\n");
    ssize_t len = orig_read(fildes,buf,nbyte);

    for(int i = 0; i < nbyte; i++){
      printf("%x", ((char *)buf)[i]);
    }
    printf("\nBECOME\n");
    srand(time(NULL));
    int r = rand() % len;
    int t = rand() % 250;
    ((char *)buf)[r]=t;

    for(int i = 0; i < nbyte; i++){
      printf("%x", ((char *)buf)[i]);
    }
    printf("\n");

    return len;
}
