#!/bin/bash
awk '/Teste /{n++}{print >"res" n ".json" }' outputB.json
sed -i 1,2d res*
sed -i '$d' res*  
sed -i -e '$a\ }' res*
sed -i -e '$a\ }' res*
