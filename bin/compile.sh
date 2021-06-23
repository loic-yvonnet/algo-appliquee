#!/bin/bash

# The default argument is to build the whole thing but PDFs (which are long to process)
config=$1
if [ "${config}" == "" ]
then
    config=build_local
fi

# Build
npm run -s ${config}