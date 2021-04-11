import math as m

def G ( phi, N ):
    def  f (  x ):
        s = 0
        for i in range( N):
            i = i + 2
            nu = m.floor ( m.log( phi( ( i + 1)**2 )**2 ) / m.log ( i ) ) + 1
            s = s + ( x/i)**nu
        
        return s
    return  f
def a ( x ):
    return x **2
def expand ( st, M_s, M_a, T, ip_size, N  ):
    v = []
    v.append (0)
    print ( st [0])
    
    for i in range ( m.floor ( G ( T, N )( ip_size )) ):
        res = []
        res2 = []
        for s in v:
            res.append ( M_s [ s ][0] )
            res.append ( M_s [ s ][1] )
            res2.append ( st [ M_s [ s ][0] ] )
            res2.append ( st [ M_s [ s ][1] ] )
        print (res2 )
        v = res

