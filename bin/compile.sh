#!/bin/bash

config=$1
if [ "${config}" == "" ]
then
    config=build
fi

npm run -s ${config}