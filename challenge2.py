#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""
check the integrity with `md5sum -c md5sum.txt`
"""

import os

m=8
with open(os.path.abspath(__file__)) as f:
	d = f.readlines()

l = d.pop()
l = d.pop()
r = ""
while l != "\n":
	r = chr(sum([2**i for i in range(m) if l[:m][i] == "\t"])) + r
	l = d.pop()
eval(str(r))

    			 
 	  			 
	  	 		 
 			 		 
  	 			 
   	 	  
 	   	  
   	  	 
	 	  		 
  		 		 
  		 		 
				 		 
     	  
			 			 
				 		 
 	  			 
  		 		 
  	  		 
     	  
	    	  
 	   	  
	  	 	  
 	 	    
