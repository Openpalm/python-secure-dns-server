#!/bin/bash - 
#===============================================================================
#
#          FILE: clean-workspace.sh
# 
#         USAGE: ./clean-workspace.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 02/10/2020 09:22
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error
rm -rf __pycache__
rm -rf *pyc
rm -rf tags

