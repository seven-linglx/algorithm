cmake_minimum_required(VERSION 3.8)
set(PROJECT_NAME LoopBack)
project(${PROJECT_NAME})
set(CMAKE_CXX_STANDARD 11)

find_file(Eigen REQUIRED)

set(SOURCE_FILES_L loopback.cpp)
add_executable(${PROJECT_NAME} ${SOURCE_FILES_L})

set(SOURCE_FILES_S sort.cpp)
add_executable(Sort ${SOURCE_FILES_S})

set(SOURCE_FILES_B bst.cpp)
add_executable(BST ${SOURCE_FILES_B})

set(SOURCE_FILES_G seed_growth.cpp)
add_executable(SeedGrowth ${SOURCE_FILES_G})
