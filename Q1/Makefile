CXX = g++
CXXFLAGS = -std=c++17 -Wall -c
LXXFLAGS = -std=c++17
OBJECTS = q1.o
TARGET = q1


$(TARGET): $(OBJECTS)
	$(CXX) $(LXXFLAGS) $(OBJECTS) -o $(TARGET)
q1.o: q1.cpp
	$(CXX) $(CXXFLAGS) q1.cpp
clean:
	rm -f $(TARGET) $(OBJECTS)
