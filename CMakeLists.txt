cmake_minimum_required(VERSION 3.8)
set(PROJECT_NAME LoopBack)
project(${PROJECT_NAME})
set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES loopback.cpp)
add_executable(${PROJECT_NAME} ${SOURCE_FILES})
