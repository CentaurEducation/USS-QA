from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, Aer, execute
import math as m
def r_1 ( r_0, n_0, n_1, circ ):
    q = QuantumRegister (1)
    c = ClassicalRegister (1)
    qc = QuantumCircuit(q, c)
    
    qc.u3 (2*m.acos ( r_0 ), n_1*m.pi/8,0,q )
    qc.x ( q )
    qc.u1 ( n_0*m.pi/8, q )
    qc.x( q )
    for i in range ( len ( circ )):
        if circ [ i ] is 'x':
            qc.x( q )
        elif circ [ i ] is 's':
            qc.s( q )
        elif circ [ i ] is 't':
            qc.t ( q )
        elif circ [ i ] is 'h':
            qc.h( q )
    qc.measure( q , c )
    
    backend = Aer.get_backend ('qasm_simulator')
    job_sim = execute (qc , backend )
    sim_result = job_sim.result ()

    return sim_result.get_counts (qc )
def p_1 ( N_0, N_1, circ ):
    n_0 =  N_0
    n_1 =  N_1
    s =  0
    H =  0
    for i in range( len ( circ )):
        if circ [ i ] is 'x':
            temp =  n_0
            n_0 =  n_1
            n_1 =  temp
            s =  ( s + 1) %% 2
        elif circ [ i ] is 's':
            n_1 =  (n_1 + 8) %% 16
        elif circ [ i ] is 't':
            n_1 =  (n_1 + 2) %% 16
        elif circ [ i ] is 'h':
            if H is 0 and s is 0:
                n_1 =  n_0
                H =  1
            if H is 0 and s is 1:
                n_0 =  n_1
                n_1 =  (n_1 + 8) %% 16
                H =  1
            if H is 1:
                n_0 =  ((n_0 + n_1))/2
                n_1 =  ((n_0 + n_1 + 8))/2
    return 16*n_1 + n_0
def eval ( r_0, n_0, n_1, q ):
    R_0 =  r1(r_0,n_0,n_1,q)['0']/1024
    N_0 =  p1(n_0,n_1,q)%16
    N_1 =  ( p1(n_0,n_1,q) - N_0)/16
    
    res =  [R_0,N_0,N_1]
    return res
def exec ( C , R , N_0 , N_1 ):
    i = 0
    
    res = []
    for line in C:
        res.append( eval ( R [ i ], N_0 [ i ], N_1 [ i ], line ))
    return res
