# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_bitchin_n_moanin_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED bitchin_n_moanin_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(bitchin_n_moanin_FOUND FALSE)
  elseif(NOT bitchin_n_moanin_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(bitchin_n_moanin_FOUND FALSE)
  endif()
  return()
endif()
set(_bitchin_n_moanin_CONFIG_INCLUDED TRUE)

# output package information
if(NOT bitchin_n_moanin_FIND_QUIETLY)
  message(STATUS "Found bitchin_n_moanin: 0.0.0 (${bitchin_n_moanin_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'bitchin_n_moanin' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${bitchin_n_moanin_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(bitchin_n_moanin_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${bitchin_n_moanin_DIR}/${_extra}")
endforeach()
