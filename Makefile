CC = gcc
CFLAGS = -g -fPIC -lm -std=gnu99 -O3 -march=native -DCONJUGRAD_FLOAT=64

#all: libfields.so

#m.PHONY : clean

fields.so: fields.o
	gcc -shared -o libfields.so fields.o
	#gcc -shared -Wl,-soname,$@ -o $@ $^

clean:
	rm -vf libfields.so *.o

fields.o: fields.c
	gcc -c  -fpic fields.c