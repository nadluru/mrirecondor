#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Om Shanti. Om Sai Ram. November 14, 2014. 2:05 p.m. Madison, WI.
#Om Shanti. Om Sai Ram. October 6, 2014. 10:27 a.m. Madison, WI.
#Om Shanti. Om Sai Ram.
#July 18, 2014. 7:33 p.m. Madison.
#Om Shanti. Om Sai Ram.
#July 15, 2014. 9:06 p.m. Madison.
#Om Shanti. Om Sai Ram.
#July 10, 2014. 8:50 p.m. Madison.
#Om Shanti. Om Sai Ram.
#July 8, 2014. 2:45 p.m. Madison.
#Om Shanti. #Om Sai Ram.
#May 20, 2014. 10:40 a.m. Madison.
#Om Shanti.
#February 15, 2014.
#Om Shanti.
#January 7, 2014.
#Om Shanti.
#January 2, 2014.
#November 13, 2013.
#June 18, 2013.
#Nagesh Adluru.

import sys
import os
import subprocess as sp
import glob
from os.path import isfile,isdir,join

PFileName = "P14848.7"
outputFolderName = "DatFileFolder"
cmdName="recon24_102914"
vdsName = "VIPR_IR_256_100_1000.grad"
dcmName = "I001.dcm"
suffix="_20141119"
init_dir = "/scratch/kecskemeti/MPnRAGE_CONDOR/"

submitFile=open("condor_fun.submit","w")
submitFile.write("Universe=vanilla\n")
submitFile.write("getenv=True\n")
submitFile.write("Executable=recon_fun.sh\n")

submitFile.write("PeriodicRemove =  (((CurrentTime - EnteredCurrentStatus) > (2*24*3600)) && JobStatus == 5)\n")
submitFile.write("Requirements = ( OpSys == \"LINUX\" && Arch == \"X86_64\" )\n")
submitFile.write("request_cpus = 1\n")
submitFile.write("request_memory = 8000\n")
submitFile.write("request_disk = 1000000\n")
submitFile.write("periodic_release = (JobStatus == 5) && ((CurrentTime - EnteredCurrentStatus) > 30) && (NumSystemHolds < 10)\n")
submitFile.write("match_list_length = 5\n")
submitFile.write("requirements = (TARGET.Name =!= LastMatchName1)\n")

submitFile.write("should_transfer_files = yes\n")
submitFile.write("when_to_transfer_output = ON_EXIT\n\n")

PFile = "/study/iggrant/MPnRAGE_MOTION_CORRECTION/323637/%s" % (PFileName)
cmdFile = "/home/kecskemeti/MRIRecondor/mrirecondor/%s" % (cmdName)
dcmFile = "/home/kecskemeti/MRIRecondor/mrirecondor/%s" % (dcmName)
vdsFile = "/home/kecskemeti/MRIRecondor/mrirecondor/%s" % (vdsName)

# Per chunk.
submitFile.write("initialdir=/scratch/kecskemeti/VIPRIRReconTest\n")
if not os.path.exists("/scratch/kecskemeti/VIPRIRReconTest"):
	os.makedirs("/scratch/kecskemeti/VIPRIRReconTest");
submitFile.write("Log=test.log\n")
submitFile.write("Output=test.out\n")
submitFile.write("Error=test.err\n")

submitFile.write("transfer_input_files = %s, %s, %s\n" % (cmdFile, dcmFile, vdsFile))
submitFile.write("transfer_output_files = %s\n" % (outputFolderName))
submitFile.write("Arguments=%s\n" % (outputFolderName))
#submitFile.write("+WantGlidein=true\n")
submitFile.write("Queue\n\n")

submitFile.close()
