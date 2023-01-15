#!/bin/sh
gen-project -d dapi dapi.yaml
gen-yuml -d . dapi.yaml -f svg 