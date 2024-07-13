import logging
from logging import LogRecord
logging.StreamHandler         # specialniy obrbotchik dlya konsoli 


class ConsoleFilter(logging.Filter):   #filtr zadaetsa cherez class
    def filter(self, record):
        #print(record.__dict__)
        # {'name': 'my_python_logger', 'msg': 'message 777', 'args': (), 'levelname': 'INFO', 'levelno': 20, 'pathname': 'c:\\Users\\User\\Desktop\\PROJECTS\\mass-pdf-converter\\logging-learn.py', 'filename': 'logging-learn.py', 'module': 'logging-learn', 'exc_info': None, 'exc_text': None, 'stack_info': None, 'lineno': 13, 'funcName': 'main', 'created': 1720401547.300147, 'msecs': 300.0, 'relativeCreated': 30.13014793395996, 'thread': 8180, 'threadName': 'MainThread', 'processName': 'MainProcess', 'process': 5972, 'taskName': None}
        if hasattr(record, 'status_code') and record.status_code != 200:
            print('warning http status is not OK')        
        return True

   
class NotsetFilter(logging.Filter):
    def filter(self, record: LogRecord) -> bool:
        #if record.levelno == 0:
        return True # accepts all records for NOTSET


class DebugFilter(logging.Filter):
    def filter(self, record: LogRecord) -> bool:
        return record.levelno == logging.DEBUG #10 #if... return true
            #return True


class InfoFilter(logging.Filter):
    def filter(self, record: LogRecord) -> bool:
        return record.levelno == logging.INFO #20
            #return True


class WarningFilter(logging.Filter):
    def filter(self, record: LogRecord) -> bool:
        return record.levelno == logging.WARNING #30
            #return True


class ErrorFilter(logging.Filter):
    def filter(self, record: LogRecord) -> bool:
        return record.levelno == logging.ERROR #40
            #return True


class CriticalFilter(logging.Filter):
    def filter(self, record: LogRecord) -> bool:
        return record.levelno == logging.CRITICAL #50
            #return True



logger_conf = {
    'version': 1,
    'formatters': {
        'my_console_msg_formatter': {
            'format': '{levelname} {msg} {filename} {funcName} {lineno} {exc_info}',
            'style': "{"
        },
    },
    'handlers': {                         # spisok vseh nashih obrabotchikov
        'console': {                        # obrabotchik - konsol
            'class': 'logging.StreamHandler',
            'level': 'NOTSET',
            'formatter': 'my_console_msg_formatter'
        },
        'file_notset': {                        # obrabotchik - file
            'class': 'logging.FileHandler',
            'level': 'NOTSET',
            'formatter': 'my_console_msg_formatter',
            'filename': 'logs/notset.log',
            'filters': ['my_notset_filter']            
        },        
        'file_debug': {                        
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'my_console_msg_formatter',
            'filename': 'logs/debug.log',
            'filters': ['my_debug_filter']             
        },
        'file_info': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'formatter': 'my_console_msg_formatter',
            'filename': 'logs/info.log',
            'filters': ['my_info_filter'] 
        },
        'file_warning': {
            'class': 'logging.FileHandler',
            'level': 'WARNING',
            'formatter': 'my_console_msg_formatter',
            'filename': 'logs/warning.log',
            'filters': ['my_warning_filter'] 
        },
        'file_error': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'formatter': 'my_console_msg_formatter',
            'filename': 'logs/error.log',
            'filters': ['my_error_filter'] 
        },
        'file_critical': {
            'class': 'logging.FileHandler',
            'level': 'CRITICAL',
            'formatter': 'my_console_msg_formatter',
            'filename': 'logs/critical.log',
            'filters': ['my_critical_filter'] 
        }
    },
    'filters': {
        'my_console_filter': {
            '()': ConsoleFilter     # vizov nashego filtra iz klassa vot tak pishetsa (cherez vot takoy slovar. Teper v obrabotchike nado ukazat nije)
        },
        'my_notset_filter': {
            '()': NotsetFilter     
        },
        'my_debug_filter': {
            '()': DebugFilter    
        },
        'my_info_filter': {
            '()': InfoFilter     
        },
        'my_warning_filter': {
            '()': WarningFilter     
        },
        'my_error_filter': {
            '()': ErrorFilter   
        },
        'my_critical_filter': {
            '()': CriticalFilter   
        }                                                            
    },
    'loggers': {
        'my_python_logger': {
            'level': 'INFO',
            'handlers': ['console', 'file_notset', 'file_debug', 'file_info', 'file_warning', 'file_error', 'file_critical'],          # ukazivaem spisok obrbotchikov kotorie mi budem ispolzovat
            'filters': ['my_console_filter']
        }
    }
}