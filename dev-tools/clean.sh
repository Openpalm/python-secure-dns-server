#!/bin/bash - 
#===============================================================================
#
#          FILE: clean.sh
# 
#         USAGE: ./clean.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 02/10/2020 08:08
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error
docker rm -f $(docker ps -aq)
docker system prune -af
docker ps -a
docker images
