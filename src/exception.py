import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()                   #_,_, implies the first 2 details i am not interseted about & exc_tb is variable which will store the inf. about the error like line no, details etc.
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error Occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))

    return error_message
    




class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)


    def __str__(self):
        return self.error_message
    





