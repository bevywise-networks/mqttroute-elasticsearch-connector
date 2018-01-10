#!/usr/bin/python
###############################################################################
#
# @2018 Bevywise Networks - www.bevywise.com 
#
# This plugin is an extension to the MQTTRoute, the enterprise mqtt broker. 
# This plugin helps you store all the data received by the broker from different edge devices into the ELASTIC. 
#
# Elastic.py
#
# Author Name: Vardharajulu K N (VKN)
#
# The Package contains Elastic instance creation, data insertion.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# 
# you may not use this file except in compliance with the License.
# 
# You may obtain a copy of the License at  http://www.apache.org/licenses/LICENSE-2.0
# 
###############################################################################

from elasticsearch import Elasticsearch
import logger, os, sys
from config import Config

class Elastic(Config):
    # Initialiser Class
    def __init__(self, filepath):
        super(Elastic, self).__init__(filepath)
        if self._open() == True:
            self.log = logger.Logger(self.get_value('LOG','LOG_FILE_PATH'))
            self.log.info("Config File Loaded Sucessfully.")
        else:
            self.log = logger.Logger()
            self.log.err("Config file open error.")
        self.custom_data = {
                        'elastic_host' : self.get_value('ELASTIC','HOSTNAME'), 
                        'elastic_port' : int(self.get_value('ELASTIC','PORT')), 
                        'elastic_index' : self.get_value('ELASTIC','INDEX_NAME')
                        }
        self.init_db()

    def init_db(self):
        try:
            self.Elastic_instance = Elasticsearch(self.custom_data['elastic_host'], port = self.custom_data['elastic_port'], max_retries = 0)
            if not self.Elastic_instance.ping():
                self.log.err("Unable to Connect with Elastic Port {0}. Change the port in plugin.conf".format(self.custom_data['elastic_port']))
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.log.err("Error in DB connection ")           
            self.log.err('{}:{}:{}'.format(exc_type, fname, exc_tb.tb_lineno))
        else:
            self.log.info("Sucessfully Connected To Elastic at port - {0} ".format(self.custom_data['elastic_port']))    

            
    def data_consumer(self,data,result = ''):
        try:
            self.Elastic_instance.index(index=self.custom_data['elastic_index'],doc_type='payload',body=data)
        except Exception:
            self.log.err("Data Insert Error")           
        
# Write code for testing. 
if __name__ == '__main__':
    Elastic(Config)    
