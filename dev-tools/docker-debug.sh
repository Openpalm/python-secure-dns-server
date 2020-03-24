#!/bin/bash - 
#===============================================================================
#
#          FILE: docker-debug.sh
# 
#         USAGE: ./docker-debug.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 02/10/2020 09:52
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error
docker run -ti --rm --user root -p 53:53 dns-tls-proxy:latest sh

