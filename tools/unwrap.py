import json,glob,os,sys
r=sys.argv[1]
def u(x):
 if isinstance(x,dict) and set(x)=={"value","Count"}: return u(x["value"])
 return [u(i) for i in x] if isinstance(x,list) else x
ok=lambda q:isinstance(q,list) and len(q)>=5 and isinstance(q[2],list) and isinstance(q[3],int) and 0<=q[3]<len(q[2])
t=0
for f in sorted(glob.glob(r+"/batches/*/*.json")):
 with open(f,encoding="utf-8-sig") as h: d=u(json.load(h))
 with open(f,"w",encoding="utf-8") as h: json.dump(d,h,ensure_ascii=False,separators=(",",":"))
 t+=len(d); print(f[len(r)+9:].ljust(28),len(d),"bad",sum(not ok(q) for q in d))
print("TOTAL",t)