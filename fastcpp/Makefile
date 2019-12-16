CC = g++
CFLAGS = -g -Wall
SRCS = fast.cpp
PROG = fast

OPENCV = `pkg-config opencv --cflags --libs`
LIBS = $(OPENCV)

$(PROG):$(SRCS)
	$(CC) $(CFLAGS) -o $(PROG) $(SRCS) $(LIBS)
