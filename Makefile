fields.so: fields.o
	gcc -shared -o libfields.so fields.o

fields.o: fields.c
	gcc -c  -fpic fields.c