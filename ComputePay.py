def computepay(h,r):
if h &gt; 40:
p = 1.5 * r * (h - 40) + (40 *r)
else:
p = h * r
return p

hrs = input(&quot;Enter Hours:&quot;)
hr = float(hrs)
rphrs = input(&quot;Enter rate per hour:&quot;)
rphr = float(rphrs)

p = computepay(hr,rphr)
print(&quot;Pay&quot;,+p)

