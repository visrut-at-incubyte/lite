UNITY_DIR = ./Unity/src
SRC_DIR = ./src
TEST_DIR = ./test

# reason: https://github.com/mcinglis/c-style
CFLAGS = -I$(UNITY_DIR) -I$(SRC_DIR) -Wall -Wextra -Wpedantic \
          -Wformat=2 -Wno-unused-parameter -Wshadow \
          -Wwrite-strings -Wstrict-prototypes -Wold-style-definition \
          -Wredundant-decls -Wnested-externs -Wmissing-include-dirs

ifeq ($(CC),gcc)
    CFLAGS += -Wjump-misses-init -Wlogical-op
endif

CFLAGS += -O2

DEBUG_CFLAGS = $(CFLAGS) -g -O0

TARGET = test_runner
DEBUG_TARGET = test_runner_debug
TEST_SRC = $(TEST_DIR)/test_main.c
SRC = $(SRC_DIR)/main.c
UNITY_SRC = $(UNITY_DIR)/unity.c

all: $(TARGET)

$(TARGET): $(TEST_SRC) $(SRC) $(UNITY_SRC)
	$(CC) $(CFLAGS) $^ -o $@

debug: $(DEBUG_TARGET)

$(DEBUG_TARGET): $(TEST_SRC) $(SRC) $(UNITY_SRC)
	$(CC) $(DEBUG_CFLAGS) $^ -o $@

run_tests: $(TARGET)
	./$(TARGET)

clean:
	rm -f $(TARGET) $(DEBUG_TARGET)

.PHONY: all run_tests clean debug
