#!/usr/bin/env bash

declare -A BAND_COLORS=(
    ["black"]=0
    ["brown"]=1
    ["red"]=2
    ["orange"]=3
    ["yellow"]=4
    ["green"]=5
    ["blue"]=6
    ["violet"]=7
    ["grey"]=8
    ["white"]=9
)
echo "${BAND_COLORS[$1]:?"invalid color"}${BAND_COLORS[$2]:?"invalid color"}"
