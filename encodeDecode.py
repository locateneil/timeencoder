import math, mpmath
from mpmath import mp
import decimal
mp.dps = 12
#print(mp.quad(lambda x: mp.exp(-x**2), [-mp.inf, mp.inf]) ** 2)
st = 10
t = st
ti = 1
lv = 44
pre = 0.00000000000
fp = 0.0

fluxList = [7, 3, 9, 6, 8, 2, 3, 7, 3, 9, 5, 2, 8, 9, 4, 3, 6, 7, 5, 9, 5, 6, 4, 4, 8, 7, 7, 8, 3, 6, 2, 3, 7, 6,]


lpre = []
lxpre = []
#print(mpmath.polylog(3,3))

#print(fluxList)

#encode
xpre = 0.0
cnt = 0
ccn = 0.0
preflux = 0
prepre = 0.0
xerr = 0.0
totalerr = 0.0
lllvt = 0.0

for flux in fluxList:

    llvt = mpmath.log(t,lv)
    #print(lv ** llvt, ' - ',llvt)


    #print(pre, xerr)
    fp = flux + pre
    pre = mpmath.power(llvt, fp)

    # ======= reverse calculation for error correction
    if(pre!=0):
        lllvt = mpmath.log(pre, llvt)
        xpre = lllvt - flux

    xerr = prepre - xpre
    #pre = pre + xerr

    #print(pre, pre + xerr, xerr)

    #xpre = xpre+xerr
    #totalerr = totalerr + xerr
    #print(lllvt, fp)



    #pre = pre + xerr

    lpre.append(pre + xerr)

    #pre = pre + tpre
    #print('Time:',t,'LogTime:',llvt,'Fp:', fp,'Pre:', pre)

    t = t + ti
    #pre = mpmath.sqrt(llvt)
    cnt = cnt +1
    prepre = pre
    #print(t, '|', llvt,'|', flux,'|', fp,'|', pre)

#print('---', lpre)
#print('---', lxpre)



#print(totalerr)

lastNum = pre # last number


#--correct errors
# xcn = 0
# t=st
# for epre in lpre:
#     #print(epre,lxpre[xcn] )
#     llvt = mpmath.log(t, lv)
#     lllvt = mpmath.log(epre, llvt)
#     xflux = int(lllvt)
#     xpre = lllvt - xflux
#     #lxpre.append(xpre)
#     if(xcn>0):
#         lpre[xcn-1] = lpre[xcn-1]
#         print(lpre[xcn-1], xpre)
#
#     t = t+ti
#     xcn = xcn+1

#------------------------------------------------------
#print(lpre)
####decode



#dd = mpmath.log(pre,100)


print('-----------------------------------------------')
print('number generated',lastNum)
print('-----------------------------------------------')
#x = mp.nsum(lambda k: 4*(-1)**(k+1)/(2*k-1), [1,mp.inf])
#print(x)

#(exp(1+euler/2)/nprod(lambda n: (1+1/n)**n * exp(1/(2*n)-1), [1, inf]))**2/2


t = len(fluxList)+st-1 ##skip last

flux = 0
count = 0
resultFlux = []

#lerr.append(aaa)
while (t >= st):
    llvt = mpmath.log(t, lv)





    #lpre is from encoding
    lpr = lpre[t - st]
    err = lpr - lastNum

    #reencoding and decoding to calkulate error rate
    fp = flux + lastNum
    qpre = mpmath.power(llvt, fp)
    qlllvt = mpmath.log(qpre, llvt)
    qflux = int(qlllvt)
    qlast = qlllvt - qflux
    #print(lpr, qlast, lastNum)
    #lastNum = lastNum + (qlast-lastNum)
    print(lpr, lastNum, err)
    #errL.append(err)

    #print(lpr,lastNum)

    #print(flux, lastNum, err)

    #with error correction

    lastNum = lastNum + err
    lllvt = mpmath.log(lastNum,llvt)

    flux = int(lllvt)



    lastNum = lllvt-flux

    #print(t, flux)
    resultFlux.append(flux)
    t=t-1





#print(errL)
resultFlux.reverse()
#print(len(fluxList))
print('Results :',resultFlux)
print('Original:',fluxList)

