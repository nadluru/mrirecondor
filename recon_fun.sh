#!/bin/sh

outputFolderName=$1

echo ${outputFolderName}

cp I001.dcm fun.dcm

mkdir ${outputFolderName}
mv fun.dcm ./${outputFolderName}

