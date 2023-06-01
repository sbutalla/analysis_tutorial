# This file was automatically created by FeynRules 2.3.36
# Mathematica version: 11.3.0 for Mac OS X x86 (64-bit) (March 7, 2018)
# Date: Wed 3 Feb 2021 11:54:17


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.d__tilde__, P.d, P.g ],
             color = [ 'T(3,2,1)' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_4})

V_2 = Vertex(name = 'V_2',
             particles = [ P.s__tilde__, P.s, P.g ],
             color = [ 'T(3,2,1)' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_4})

V_3 = Vertex(name = 'V_3',
             particles = [ P.b__tilde__, P.b, P.g ],
             color = [ 'T(3,2,1)' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_4})

V_4 = Vertex(name = 'V_4',
             particles = [ P.u__tilde__, P.u, P.g ],
             color = [ 'T(3,2,1)' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_4})

V_5 = Vertex(name = 'V_5',
             particles = [ P.c__tilde__, P.c, P.g ],
             color = [ 'T(3,2,1)' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_4})

V_6 = Vertex(name = 'V_6',
             particles = [ P.t__tilde__, P.t, P.g ],
             color = [ 'T(3,2,1)' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_4})

V_7 = Vertex(name = 'V_7',
             particles = [ P.Fd11, P.Fd11, P.Zd ],
             color = [ '1' ],
             lorentz = [ L.FFV2 ],
             couplings = {(0,0):C.GC_5})

V_8 = Vertex(name = 'V_8',
             particles = [ P.Fd21, P.Fd11, P.Zd ],
             color = [ '1' ],
             lorentz = [ L.FFV2 ],
             couplings = {(0,0):C.GC_6})

V_9 = Vertex(name = 'V_9',
             particles = [ P.d__tilde__, P.d, P.a ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFV5 ],
             couplings = {(0,0):C.GC_1})

V_10 = Vertex(name = 'V_10',
              particles = [ P.s__tilde__, P.s, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_1})

V_11 = Vertex(name = 'V_11',
              particles = [ P.b__tilde__, P.b, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_1})

V_12 = Vertex(name = 'V_12',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_7})

V_13 = Vertex(name = 'V_13',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_7})

V_14 = Vertex(name = 'V_14',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_7})

V_15 = Vertex(name = 'V_15',
              particles = [ P.d__tilde__, P.d, P.Zd ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_11})

V_16 = Vertex(name = 'V_16',
              particles = [ P.s__tilde__, P.s, P.Zd ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_11})

V_17 = Vertex(name = 'V_17',
              particles = [ P.b__tilde__, P.b, P.Zd ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_11})

V_18 = Vertex(name = 'V_18',
              particles = [ P.e__plus__, P.e__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV6 ],
              couplings = {(0,0):C.GC_2})

V_19 = Vertex(name = 'V_19',
              particles = [ P.mu__plus__, P.mu__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV6 ],
              couplings = {(0,0):C.GC_2})

V_20 = Vertex(name = 'V_20',
              particles = [ P.ta__plus__, P.ta__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV6 ],
              couplings = {(0,0):C.GC_2})

V_21 = Vertex(name = 'V_21',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV6 ],
              couplings = {(0,0):C.GC_8})

V_22 = Vertex(name = 'V_22',
              particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV6 ],
              couplings = {(0,0):C.GC_8})

V_23 = Vertex(name = 'V_23',
              particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_8,(0,1):C.GC_10})

V_24 = Vertex(name = 'V_24',
              particles = [ P.e__plus__, P.e__minus__, P.Zd ],
              color = [ '1' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_12,(0,1):C.GC_14})

V_25 = Vertex(name = 'V_25',
              particles = [ P.mu__plus__, P.mu__minus__, P.Zd ],
              color = [ '1' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_12,(0,1):C.GC_14})

V_26 = Vertex(name = 'V_26',
              particles = [ P.ta__plus__, P.ta__minus__, P.Zd ],
              color = [ '1' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_12,(0,1):C.GC_14})

V_27 = Vertex(name = 'V_27',
              particles = [ P.u__tilde__, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_1,(0,1):C.GC_3})

V_28 = Vertex(name = 'V_28',
              particles = [ P.c__tilde__, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_1,(0,1):C.GC_3})

V_29 = Vertex(name = 'V_29',
              particles = [ P.t__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_1,(0,1):C.GC_3})

V_30 = Vertex(name = 'V_30',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_7,(0,1):C.GC_9})

V_31 = Vertex(name = 'V_31',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_7,(0,1):C.GC_9})

V_32 = Vertex(name = 'V_32',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_7,(0,1):C.GC_9})

V_33 = Vertex(name = 'V_33',
              particles = [ P.u__tilde__, P.u, P.Zd ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_11,(0,1):C.GC_13})

V_34 = Vertex(name = 'V_34',
              particles = [ P.c__tilde__, P.c, P.Zd ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_11,(0,1):C.GC_13})

V_35 = Vertex(name = 'V_35',
              particles = [ P.t__tilde__, P.t, P.Zd ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_11,(0,1):C.GC_13})

V_36 = Vertex(name = 'V_36',
              particles = [ P.ve__tilde__, P.ve, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_2})

V_37 = Vertex(name = 'V_37',
              particles = [ P.vm__tilde__, P.vm, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_2})

V_38 = Vertex(name = 'V_38',
              particles = [ P.vt__tilde__, P.vt, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_2})

V_39 = Vertex(name = 'V_39',
              particles = [ P.ve__tilde__, P.ve, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_8})

V_40 = Vertex(name = 'V_40',
              particles = [ P.vm__tilde__, P.vm, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_8})

V_41 = Vertex(name = 'V_41',
              particles = [ P.vt__tilde__, P.vt, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_8})

V_42 = Vertex(name = 'V_42',
              particles = [ P.ve__tilde__, P.ve, P.Zd ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_12})

V_43 = Vertex(name = 'V_43',
              particles = [ P.vm__tilde__, P.vm, P.Zd ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_12})

V_44 = Vertex(name = 'V_44',
              particles = [ P.vt__tilde__, P.vt, P.Zd ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_12})

