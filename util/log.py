#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import logging, logging.config, os

class Log:
    logger = None
     
    def __init__(self):
        projectName = "CJZK.CMS.Data"
        thePath = os.getcwd()
        thePath = thePath[:thePath.find(projectName) + len(projectName)]
        logging.config.fileConfig(thePath+"/config/logger.conf")
        self.logger = logging.getLogger("logger01")  
     
    def debug(self, msg):
        self.logger.debug(msg)
     
    def info(self, msg):
        self.logger.info(msg)
        
    def warning(self, msg):
        self.logger.warning(msg)
         
    def warn(self, msg):
        self.logger.warn(msg)
        
    def error(self, msg):
        self.logger.error(msg)
    
    def critical(self, msg):
        self.logger.critical(msg)
 
 
Log().logger.info("abc")