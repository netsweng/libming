#!/usr/bin/python
from ming import *

m =  SWFMovie();


# SWF_SETBACKGROUNDCOLOR 
m.setBackground(0xff, 0xff, 0xff);

# SWF_PROTECT 
m.protect("foobar");

# SWF_SHOWFRAME 
m.nextFrame(); # end of frame 1 

# SWF_END 

m.save("test02.swf");
