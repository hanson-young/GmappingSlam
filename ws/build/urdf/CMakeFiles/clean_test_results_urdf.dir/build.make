# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/flysnow/ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/flysnow/ws/build

# Utility rule file for clean_test_results_urdf.

# Include the progress variables for this target.
include urdf/CMakeFiles/clean_test_results_urdf.dir/progress.make

urdf/CMakeFiles/clean_test_results_urdf:
	cd /home/flysnow/ws/build/urdf && /usr/bin/python /opt/ros/indigo/share/catkin/cmake/test/remove_test_results.py /home/flysnow/ws/build/test_results/urdf

clean_test_results_urdf: urdf/CMakeFiles/clean_test_results_urdf
clean_test_results_urdf: urdf/CMakeFiles/clean_test_results_urdf.dir/build.make
.PHONY : clean_test_results_urdf

# Rule to build all files generated by this target.
urdf/CMakeFiles/clean_test_results_urdf.dir/build: clean_test_results_urdf
.PHONY : urdf/CMakeFiles/clean_test_results_urdf.dir/build

urdf/CMakeFiles/clean_test_results_urdf.dir/clean:
	cd /home/flysnow/ws/build/urdf && $(CMAKE_COMMAND) -P CMakeFiles/clean_test_results_urdf.dir/cmake_clean.cmake
.PHONY : urdf/CMakeFiles/clean_test_results_urdf.dir/clean

urdf/CMakeFiles/clean_test_results_urdf.dir/depend:
	cd /home/flysnow/ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/flysnow/ws/src /home/flysnow/ws/src/urdf /home/flysnow/ws/build /home/flysnow/ws/build/urdf /home/flysnow/ws/build/urdf/CMakeFiles/clean_test_results_urdf.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : urdf/CMakeFiles/clean_test_results_urdf.dir/depend

