'''
Created on 12/08/2017

@author: ernesto
'''
import logging
from collections import Counter
from functools import reduce
import sys
nivel_log = logging.ERROR
# nivel_log = logging.DEBUG
logger_cagada = None

def shit_core(numeros):
    numeros_tam = len(numeros)
    ocurrencias = Counter(numeros)
    llaves_ord = sorted(ocurrencias.keys())
    valores_llaves = {}
    toma = []
    no_toma = []
    
    valores_llaves = reduce(lambda valores, llave:valores.update({llave: llave * ocurrencias[llave]}) or valores, llaves_ord, {})
    logger_cagada.debug("los valores de cada llave {}".format(valores_llaves))
    
    no_toma.append(0)
    toma.append(valores_llaves[llaves_ord[0]])
    
    for idx, llave in enumerate(llaves_ord[1:], 1):
        llave_ant = llaves_ord[idx - 1]
        puede_tomar_ant = 0
        valor_no_toma = max(no_toma[idx - 1], toma[idx - 1])
        no_toma.append(valor_no_toma)
        
        valor_toma = valores_llaves[llave]
        puede_tomar_ant = llave - llave_ant > 1
        if(puede_tomar_ant):
            valor_toma += max(no_toma[idx - 1], toma[idx - 1])
        else:
            valor_toma += no_toma[idx - 1]
        
        toma.append(valor_toma)
    
    logger_cagada.debug("valores no toma {}".format(no_toma))
    logger_cagada.debug("valores toma {}".format(toma))
    maxima_caca = max(no_toma[-1], toma[-1])
    return maxima_caca

def shit_main():
    lineas = list(sys.stdin)
    
    numeros = [int(x) for x in lineas[1].strip().split(" ")]
    
    caca = shit_core(numeros)
    print(caca)
    

if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)
        shit_main()
