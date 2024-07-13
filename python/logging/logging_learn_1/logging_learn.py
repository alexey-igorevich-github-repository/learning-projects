import logging
import logging.config
from logging_config import logger_conf        # importiruem iz faila nastroek

logging.config.dictConfig(logger_conf) # peredaem nashi nastroyki v funkciu

############################################################################################################

# teper posle slovarya, nasktoyki, sozdadim logger
logger = logging.getLogger('my_python_logger')   # peredaem tuda nash logger iz slovarya
#print(logger)
#print(logger.handlers) #posmotrim kakie est obrabotchiki

def log_nonset(logger, message, *args, **kwargs):
    if logger.isEnabledFor(logging.NOTSET):
        logger._log(logging.NOTSET, message, args, **kwargs)


def add_notset_method_to_logger(logger):
    def notset_method(message, *args, **kwargs):
        log_nonset(logger, message, *args, **kwargs)
    logger.notset = notset_method

add_notset_method_to_logger(logger)



############################################################################################################

def main():
    logger.notset('message_notset_00')
    logger.debug('message_debug_10')
    logger.info('message_info_20')
    logger.warning('message_warning_30')
    logger.error('message_error_40')
    logger.critical('message_critical_50')  

    # status = 404
    # logger.error('404_not_found', extra={'status_code': status})     # soobshenie s dop parametrom v record

    # try:
    #     print(10/0)
    # except Exception as e:
    #     logger.exception(e)


############################################################################################################

if __name__ == '__main__':
    main()

