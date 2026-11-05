import numpy as np
from PIL import Image, ImageDraw, ImageFilter
W=3000; rng=np.random.default_rng(76)
# dark stone wall with block texture
a=np.zeros((W,W,3)); a[...]=(16,14,20)
img=Image.fromarray(a.astype('uint8')); d=ImageDraw.Draw(img)
for row,y in enumerate(range(0,W,190)):
    off=0 if row%2 else 160
    for x in range(-off,W,320):
        c=int(rng.integers(18,30)); d.rectangle([x+6,y+6,x+314,y+184],fill=(c,c-2,c+4))
# window shape: pointed (lancet) arch
cx, top, bot, hw = 1500, 520, 2550, 560
yy0,xx0=np.mgrid[0:W,0:W]
spring=1450
rect=(xx0>=cx-hw)&(xx0<=cx+hw)&(yy0>=spring)&(yy0<=bot)
arch=(yy0<spring)&(np.hypot(xx0-(cx+hw),yy0-spring)<=2*hw)&(np.hypot(xx0-(cx-hw),yy0-spring)<=2*hw)
win=Image.fromarray(((rect|arch)*255).astype('uint8'))
# glow behind window
glow=win.filter(ImageFilter.GaussianBlur(140))
img=Image.composite(Image.new('RGB',(W,W),(40,150,120)),img,glow.point(lambda v:int(v*0.45)))
# stained glass fill: radial colours
yy,xx=np.mgrid[0:W,0:W]; r=np.hypot(xx-cx,yy-2150)
col=np.zeros((W,W,3))
col[...,0]=30+40*np.sin(r/90)**2; col[...,1]=140+80*np.cos(r/140)**2; col[...,2]=120+90*np.sin(r/70+1)**2
glass=Image.fromarray(col.clip(0,255).astype('uint8'))
img.paste(glass,(0,0),win); d=ImageDraw.Draw(img)
# leading: Wi-Fi arcs + dot as the tracery, plus a few panes
L=(12,10,14)
for k,rad in enumerate([260,480,700]):
    d.arc([cx-rad,2150-rad,cx+rad,2150+rad],225,315,fill=L,width=70)
d.ellipse([cx-80,2070,cx+80,2230],fill=(255,236,160))
d.ellipse([cx-80,2070,cx+80,2230],outline=L,width=26)
for x in (cx-hw//2, cx+hw//2): d.line([(x,2350),(x,bot)],fill=L,width=26)
d.line([(cx-hw,2350),(cx+hw,2350)],fill=L,width=26)
# window outline
edge=win.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.MaxFilter(41))
img.paste(Image.new('RGB',(W,W),(40,36,44)),(0,0),edge)
a=np.asarray(img).astype(float)+rng.normal(0,6,(W,W,1))
r2=np.hypot(xx-W/2,yy-W/2)/(W/1.4); a*=(1-0.5*r2**2)[...,None]
img=Image.fromarray(a.clip(0,255).astype('uint8'))
img.save('/home/user/Clauno/in-nomine-wifi/art/cover.png',optimize=True)
img.resize((300,300),Image.LANCZOS).save('/tmp/claude-0/-home-user-Clauno/64fd93a0-a618-59bd-a459-bcae33d9f4e2/scratchpad/thumb4.png')
