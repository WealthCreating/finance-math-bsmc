# -*- coding: utf-8 -*-
"""
En este apartado se establecen las funciones con los metodos de Monte Carlo y 
Black Scholes para evaluar opciones europeas vainillas de compra y de venta con
dividendos.

Funcion metodo de Monte Carlo:
Permite estimar el valor de una opcion vainilla europea tanto de compra como de 
venta con dividendos.
Inputs de la funcion def montecarlo_d(S0,K,r,sigma,T,I,D0):
    
    S0=17.      Es el valor inicial del activo
    K=15.       Es el precio de ejercicio o strike
    r=0.03      Es el tipo de interes constante
    sigma=0.25  Es la volatilidad del activo
    T=0.25      Es el periodo a vencimiento dado en numero de anos
    I=1000000   Es el numero de trayectorias del metodo (Opcional)
    D0=0.015    Es la tasa de dividendos continuos (Opcional)
    
Funcion metodo de Black Scholes:
Permite estimar el valor de una opcion vainilla europea tanto de compra como de 
venta con dividendos.
Inputs de la funcion def bs_d(S0,K,T,r,sigma,D0):
    
    S0=17.      Es el valor inicial del activo
    K=15.       Es el precio de ejercicio o strike
    T=0.25      Es el periodo a vencimiento dado en numero de anos
    r=0.03      Es el tipo de interes constante
    sigma=0.25  Es la volatilidad del activo
    D0=0.015    Es la tasa de dividendos continuos (Opcional)
    
David Camino Perdones
"""
def montecarlo_d(S0,K,r,sigma,T,I=1000000,D0=0):
    import numpy as np
    menu={1:'Evaluar opcion de compra',2:'Evaluar opcion de venta'}
    choice=eval(input('Elija la operacion deseada:\n1: Evaluar opcion de compra\n2: Evaluar opcion de venta\n'))
    if choice==1:
        print('Ha seleccionado:',menu[choice])
        ST=S0*np.exp((r-D0-sigma**2/2)*T+sigma*np.sqrt(T)*np.random.standard_normal(I))
        hT=np.maximum(ST-K,0)
        V0=np.exp(-r*T)*np.sum(hT)/I
        std=np.sqrt(sum((np.exp(-r*T)*hT-V0)**2)/I) #desviacion tipica
        s=r'%' #Calculo del intervalo de confianza al 95%
        print("Intervalo de confianza al 95"+s+"(%f,%f)"%(V0-1.96*std/np.sqrt(I),V0+1.96*std/np.sqrt(I)))
        print('El precio de la opcion es %f' %V0)
    elif choice==2:
        print('Ha seleccionado:',menu[choice])
        ST=S0*np.exp((r-D0-sigma**2/2)*T+sigma*np.sqrt(T)*np.random.standard_normal(I))
        hT=np.maximum(K-ST,0)
        V0=np.exp(-r*T)*np.sum(hT)/I
        std=np.sqrt(sum((np.exp(-r*T)*hT-V0)**2)/I) #desviacion tipica
        s=r'%' #Calculo del intervalo de confianza al 95%
        print("Intervalo de confianza al 95"+s+"(%f,%f)"%(V0-1.96*std/np.sqrt(I),V0+1.96*std/np.sqrt(I)))
        print('El precio de la opcion es %f' %V0)
    else:
        print('Ha seleccionado una opcion no valida. Intentelo de nuevo.')
    return None

def bs_d(S0,K,T,r,sigma,D0=0):
    import math
    from scipy import stats
    menu={1:'Evaluar opcion de compra',2:'Evaluar opcion de venta'}
    choice=eval(input('Elija la operacion deseada:\n1: Evaluar opcion de compra\n2: Evaluar opcion de venta\n'))
    if choice==1:
        print('Ha seleccionado:',menu[choice])
        d1=(math.log(S0/K)+(r-D0+0.5*sigma**2)*T)/(sigma*math.sqrt(T))
        d2=(math.log(S0/K)+(r-D0-0.5*sigma**2)*T)/(sigma*math.sqrt(T))
        valor=(S0*math.exp(-D0*T)*stats.norm.cdf(d1,0.0,1.0)-K*math.exp(-r*T)*stats.norm.cdf(d2,0.0,1.0))
        print('El precio de la opcion es %f' %valor)
    elif choice==2:
        print('Ha seleccionado:',menu[choice])
        d1=(math.log(S0/K)+(r-D0+0.5*sigma**2)*T)/(sigma*math.sqrt(T))
        d2=(math.log(S0/K)+(r-D0-0.5*sigma**2)*T)/(sigma*math.sqrt(T))
        valor=(K*math.exp(-r*T)*stats.norm.cdf(-d2,0.0,1.0)-S0*math.exp(-D0*T)*stats.norm.cdf(-d1,0.0,1.0))
        print('El precio de la opcion es %f' %valor)
    else:
        print('Ha seleccionado una opcion no valida. Intentelo de nuevo.')
    return None
