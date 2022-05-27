import logging as lg
import os
import sys

path = os.path.dirname(os.path.realpath(sys.argv[0]))
arquivo = os.path.join(path, 'main.log')
lg.basicConfig(handlers=[lg.FileHandler(arquivo, 'a', 'utf-8')],
                    level=lg.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')
logger = lg.getLogger('root')

def send_log_error(msg):
    print(f"Erro: {msg}")
    logger.error(msg)

def send_log_info(msg):
    print(f"Info: {msg}")
    logger.info(msg)

def send_log_warning(msg):
    print(f"Warning: {msg}")
    logger.warning(msg)

def send_log_critical(msg):
    print(f"Critical: {msg}")
    logger.critical(msg)

def send_log_debug(msg):
    print(f"Debug: {msg}")
    logger.debug(msg)