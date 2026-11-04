import numpy as np
from PIL import Image, ImageDraw, ImageFilter
W=3000; rng=np.random.default_rng(9)
y=np.linspace(0,1,W)[:,None]
a=np.zeros((W,W,3)); a[...,0]=14+20*y; a[...,1]=18+22*y; a[...,2]=44+30*y
img=Image.fromarray(a.clip(0,255).astype('uint8')); d=ImageDraw.Draw(img)
# attic beams (slanted roof lines)
d.polygon([(0,0),(1500,0),(0,1100)],fill=(10,12,28)); d.polygon([(3000,0),(1500,0),(3000,1100)],fill=(10,12,28))
# soft halo behind moon
halo=Image.new('L',(W,W),0); ImageDraw.Draw(halo).ellipse([1050,650,1950,1550],fill=255)
halo=halo.filter(ImageFilter.GaussianBlur(220))
img=Image.composite(Image.new('RGB',(W,W),(255,226,160)),img,halo.point(lambda v:int(v*0.35))); d=ImageDraw.Draw(img)
# fishing line
d.line([(1500,0),(1500,760)],fill=(200,200,210),width=5)
# paper crescent moon: big disk minus offset disk
moon=Image.new('L',(W,W),0); md=ImageDraw.Draw(moon)
md.ellipse([1150,760,1850,1460],fill=255); md.ellipse([1330,700,2030,1400],fill=0)
paper=np.zeros((W,W,3)); paper[...]=(244,232,205)
# fold creases on paper
pimg=Image.fromarray(paper.astype('uint8')); pd=ImageDraw.Draw(pimg)
for (x1,y1,x2,y2) in [(1150,1110,1600,1000),(1300,800,1420,1460),(1180,940,1650,1350)]:
    pd.line([(x1,y1),(x2,y2)],fill=(214,200,170),width=7)
img.paste(pimg,(0,0),moon); d=ImageDraw.Draw(img)
d.ellipse([1490,752,1510,772],fill=(160,160,170))  # pin hole
# horseshoe magnet, lower right, tilted up toward the moon
mag=Image.new('RGBA',(1400,1400),(0,0,0,0)); g=ImageDraw.Draw(mag)
g.arc([200,200,1200,1200],0,180,fill=(196,38,38,255),width=280)
g.rectangle([200,300,480,700],fill=(196,38,38,255)); g.rectangle([920,300,1200,700],fill=(196,38,38,255))
g.rectangle([200,140,480,320],fill=(220,220,226,255)); g.rectangle([920,140,1200,320],fill=(220,220,226,255))
mag=mag.rotate(38,resample=Image.BICUBIC,expand=False)
img.paste(mag,(1450,1500),mag); d=ImageDraw.Draw(img)
# magnetic field lines from tips toward moon
for k in range(5):
    r=250+k*120
    d.arc([1900-r,1950-r,1900+r,1950+r],205,245,fill=(120,140,210),width=6)
# grain + vignette
a=np.asarray(img).astype(float); a+=rng.normal(0,7,(W,W,1))
yy,xx=np.mgrid[0:W,0:W]; r=np.hypot(xx-W/2,yy-W/2)/(W/1.4); a*=(1-0.5*r**2)[...,None]
img=Image.fromarray(a.clip(0,255).astype('uint8'))
img.save('/home/user/Clauno/doctor-perigee/art/cover.png',optimize=True)
img.resize((300,300),Image.LANCZOS).save('/tmp/claude-0/-home-user-Clauno/64fd93a0-a618-59bd-a459-bcae33d9f4e2/scratchpad/thumb2.png')
