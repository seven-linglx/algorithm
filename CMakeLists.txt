cmake_minimum_required(VERSION 3.5)
set(PROJECT_NAME Algorithm)
project(${PROJECT_NAME})
set(CMAKE_CXX_STANDARD 11)

find_file(Eigen REQUIRED)
INCLUDE_DIRECTORIES(/usr/include/eigen3)

set(SOURCE_FILES_L loopback.cpp)
add_executable(LoopBack ${SOURCE_FILES_L})

set(SOURCE_FILES_B bst.cpp)
add_executable(BST ${SOURCE_FILES_B})

set(SOURCE_FILES_G seed_growth.cpp)
add_executable(SeedGrowth ${SOURCE_FILES_G})

set(SOURCE_FILES_Q queens.cpp)
add_executable(Queens ${SOURCE_FILES_Q})

set(SOURCE_FILES_stair stair.cpp)
add_executable(Stair ${SOURCE_FILES_stair})

set(SOURCE_FILES_sort quick_sort.cpp)
add_executable(QuickSort ${SOURCE_FILES_sort})

set(SOURCE_FILES_sunday sunday.cpp)
add_executable(Sunday ${SOURCE_FILES_sunday})

set(SOURCE_FILES_dijkstar dijkstar.cpp)
add_executable(Dijkstar ${SOURCE_FILES_dijkstar})
