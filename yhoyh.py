from sprite import sprite
from manipulate import complete
import re

face = '''\

 _-"-_
|.....|
|.....|
|.....|
 \.../
  \./
   V

'''
face = face.translate(''.maketrans('.','\u00A0'))
face = complete(face)
hair = '''\
 %%%%%%
%%%%%%%%
%% %  %%
'''
hair = complete(hair)
eyes = sprite({'basic':'\' \'\n','smile':'^ ^\n'},[['basic',0,0]])
mouth = sprite({'basic':'-\n','gasp':'O\n'},[['basic',0,0]])
body = '''\
   l...| 
   l...| 
/"".....""\\
|\\......./|
| |.....| |
t |.....l t
  |..A..|
  \\./ \\./
   V   V  
   |   |  
   L   L  
'''
body = complete(body)
body = body.translate(''.maketrans('.','\u00A0'))

 
yhoyh = sprite({'body':body,'eyes':eyes,'mouth':mouth,'face':face,'hair':hair},
	[['body',0,5],['face',2,0],['eyes',4,3],['mouth',5,5],['hair',2,0]])
