import numpy as np
from PIL import Image, ImageDraw, ImageFilter
W=3000; rng=np.random.default_rng(7)
y=np.linspace(0,1,W)[:,None,None]
top=np.array([40,18,60]); mid=np.array([235,96,40]); low=np.array([255,196,90])
sky=np.where(y<0.55, top+(mid-top)*(y/0.55), mid+(low-mid)*((y-0.55)/0.45))*np.ones((W,W,3))
img=Image.fromarray(sky.clip(0,255).astype('uint8')); d=ImageDraw.Draw(img)
# sun
sun=Image.new('L',(W,W),0); ImageDraw.Draw(sun).ellipse([700,900,2300,2500],fill=255)
img=Image.composite(Image.new('RGB',(W,W),(255,226,140)),img,sun.filter(ImageFilter.GaussianBlur(6))); d=ImageDraw.Draw(img)
for k,yy in enumerate(range(1750,2150,70)):  # retro sun stripes
    d.rectangle([600,yy,2400,yy+14+k*5],fill=(236,110,52))
# desert ground + mesas
d.polygon([(0,2150),(3000,2150),(3000,3000),(0,3000)],fill=(48,20,30))
d.polygon([(0,2150),(0,1880),(180,1880),(260,1960),(520,1960),(600,2150)],fill=(48,20,30))
d.polygon([(2350,2150),(2450,1830),(2800,1830),(2880,1990),(3000,1990),(3000,2150)],fill=(48,20,30))
# cactus
d.rectangle([2580,1850,2640,2160],fill=(48,20,30)); d.rectangle([2500,1930,2540,2040],fill=(48,20,30)); d.rectangle([2500,2010,2600,2050],fill=(48,20,30))
S=(25,10,20)
# bicycle (wire donkey)
for cx in (1180,1820):
    d.ellipse([cx-260,1890-260,cx+260,1890+260],outline=S,width=26)
    d.ellipse([cx-24,1866,cx+24,1914],fill=S)
pts=[(1180,1890),(1450,1890),(1380,1620),(1180,1890)]; d.line(pts,fill=S,width=30,joint='curve')
d.line([(1450,1890),(1720,1600),(1380,1620)],fill=S,width=30); d.line([(1720,1600),(1820,1890)],fill=S,width=28)
d.line([(1720,1600),(1700,1500),(1800,1480)],fill=S,width=26)  # handlebar
d.rectangle([1330,1585,1450,1615],fill=S)  # saddle
# rider: torso, head, hat, leg, arm
d.line([(1390,1590),(1500,1260)],fill=S,width=110)
d.ellipse([1440,1080,1600,1240],fill=S)
d.ellipse([1320,1150,1740,1205],fill=S); d.polygon([(1320,1178),(1290,1110),(1350,1160)],fill=S); d.polygon([(1740,1178),(1770,1110),(1710,1160)],fill=S); d.polygon([(1450,1170),(1470,1060),(1520,1085),(1575,1060),(1595,1170)],fill=S)  # cowboy hat
d.line([(1520,1330),(1790,1490)],fill=S,width=60)  # arm
d.line([(1400,1600),(1560,1780),(1470,1880)],fill=S,width=70)  # leg
# grain
a=np.asarray(img).astype(float)+rng.normal(0,6,(W,W,1))
img=Image.fromarray(a.clip(0,255).astype('uint8'))
img.save('/home/user/Clauno/english-for-runaways/art/cover.png',optimize=True)
img.resize((300,300),Image.LANCZOS).save('/tmp/claude-0/-home-user-Clauno/64fd93a0-a618-59bd-a459-bcae33d9f4e2/scratchpad/thumb3.png')
