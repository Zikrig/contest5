# import time

class MxMin:
    def __init__(self, mass, w):
        self.mass = mass
        self.max_from_beginning = {}
        self.min_from_beginning = {}
        self.w = w
        mx = -1
        mn = 1000000000
        for i in self.mass:
            if(self.mass[i] > mx):
                mx = self.mass[i]
                self.max_from_beginning[i] = mx
            if(self.mass[i] < mn):
                mn = self.mass[i]
                self.min_from_beginning[i] = mn
        self.max_from_ending = {}
        self.min_from_ending = {}
        mx = -1
        mn = 1000000000
        for i in reversed(self.mass):
            j = self.w-i -1
            if(self.mass[i] > mx):
                mx = self.mass[i]
                self.max_from_ending[j] = mx
            if(self.mass[i] < mn):
                mn = self.mass[i]
                self.min_from_ending[j] = mn

        self.keys = {
            'beg_min' : list(self.min_from_beginning.keys()),
            'beg_max' : list(self.max_from_beginning.keys()),
            'end_min' : list(self.min_from_ending.keys()),
            'end_max' : list((self.max_from_ending.keys()))
        }

    def get_min_on_k_from_begin(self, k):
        minind = 0
        mxind = len(self.keys['beg_min'])
        while(mxind-minind > 1):
            srind = (mxind+minind) // 2
            if(self.keys['beg_min'][srind] > k):
                mxind = srind
            else:
                minind = srind

        lastmin_ab = self.keys['beg_min'][minind]
        if(lastmin_ab>k):
            return -1
        return self.min_from_beginning[lastmin_ab]
    
    def get_max_on_k_from_begin(self, k):
        minind = 0
        mxind = len(self.keys['beg_max'])
        while(mxind-minind > 1):
            srind = (mxind+minind) // 2
            if(self.keys['beg_max'][srind] > k):
                mxind = srind
            else:
                minind = srind

        lastmin_ab = self.keys['beg_max'][minind]
        if(lastmin_ab>k):
            return -1
        return self.max_from_beginning[lastmin_ab]
    
    def minmax_beg(self, k):
        return self.get_max_on_k_from_begin(k)-self.get_min_on_k_from_begin(k)+1

    def get_min_on_k_from_end(self, k):
        minind = 0
        mxind = len(self.keys['end_min'])
        while(mxind-minind > 1):
            srind = (mxind+minind) // 2
            if(self.keys['end_min'][srind] >= k):
                mxind = srind
            else:
                minind = srind

        lastmin_ab = self.keys['end_min'][minind]
        if(lastmin_ab>k):
            return -1
        return self.min_from_ending[lastmin_ab]
    
    def get_max_on_k_from_end(self, k):
        minind = 0
        mxind = len(self.keys['end_max'])
        while(mxind-minind > 1):
            srind = (mxind+minind) // 2
            if(self.keys['end_max'][srind] >= k):
                mxind = srind
            else:
                minind = srind

        lastmin_ab = self.keys['end_max'][minind]
        if(lastmin_ab>k):
            return -1
        return self.max_from_ending[lastmin_ab]
    
    def minmax_end(self, k):
        r = self.get_max_on_k_from_end(k)-self.get_min_on_k_from_end(k)+1
        return r
    
class Square:
    def __init__(self, w, h, cnt_of_dyrs):
        self.w = w
        self.h = h
        self.cnt = cnt_of_dyrs
        self.dots = []
        self.shir = -1
        self.shrminmax = {}
        self.shrmin = {}
        self.shrmax = {}
        for i in range(cnt_of_dyrs):
            ak, bk = [int(nn) for nn in input().split()]
            self.dots.append([ak-1, bk-1])
        self.dots.sort()
        for a, b in self.dots:
            if a in self.shrmin:
                if(b < self.shrmin[a]):
                    self.shrmin[a] = b
            else:
                self.shrmin[a] = b

            if a in self.shrmax:
                if(b > self.shrmax[a]):
                    self.shrmax[a] = b
            else:
                self.shrmax[a] = b

        self.maxesMM = MxMin(self.shrmax, self.w)
        self.minesMM = MxMin(self.shrmin, self.w)

    def print_all(self):
        r = [["&" for i in range(self.h)] for j in range(self.w)]
        for dot in self.dots:
            r[dot[0]][dot[1]] = '*'
        for j in range(self.w):
            print(*r[j])

    def try_shir(self, n):
        self.shir = n
        i_prev = -1
        i = 0
            
        for k in self.maxesMM.keys['beg_max']:
            i = k
            rs = self.try_from(i)
            if(rs):
                return True
            
        for k in self.maxesMM.keys['end_max']:
            i = k
            rs = self.try_from(i)
            if(rs):
                return True

        for k in self.minesMM.keys['beg_min']:
            i = k
            rs = self.try_from(i)
            if(rs):
                return True
        for k in self.minesMM.keys['end_min']:
            i = k
            rs = self.try_from(i)
            if(rs):
                return True
        return False
            
    def try_from(self, fr):
        mindot1 = self.minesMM.get_min_on_k_from_begin(fr-1)
        mxdot1 = self.maxesMM.get_max_on_k_from_begin(fr-1)

        mindot2 = self.minesMM.get_min_on_k_from_end(self.w - self.shir-fr)
        mxdot2 = self.maxesMM.get_max_on_k_from_end(self.w - self.shir-fr)
        mintotal = -1
        maxtotal = -1
        if(fr-1<0 or mindot1 == -1):
            mintotal = mindot2
            maxtotal = mxdot2
        elif(self.w - self.shir-fr <=0 or mindot2 == -1):
            mintotal = mindot1
            maxtotal = mxdot1
        else:
            mintotal = min(mindot2, mindot1)
            maxtotal = max(mxdot2,mxdot1)
        if(maxtotal - mintotal < self.shir):
            return True
        else:
            return False

    def get_need_shir(self):
        smin = 1
        smax = min(self.h, self.w)
        while(smax-smin>1):
            s = (smax+smin)//2
            r = self.try_shir(s)
            if(r):
                smax = s
            else:
                smin = s
        if(self.try_shir(smin)):
            return smin
        return smax
w, h, k = [int(nn) for nn in input().split()]

sq = Square(w, h, k)
res = sq.get_need_shir()

print(res)