import os, sys

class CustomException(Exception):
    def __init__(self,error_message : Exception, error_detail : sys):
        self.error_message = CustomException.get_detailed_error_message(error_message,error_detail)

    @staticmethod
    def get_detailed_error_message(error_message : Exception, error_detail : sys)->str:
        _,_,exce_tb = error_detail.exc_info()

        exception_block_line_number = exce_tb.tb_frame.f_lineno
        try_block_line_number = exce_tb.tb_lineno
        file_name = exce_tb.tb_frame.f_code.co_filename

        error_message_return = f"""
            error occured in execution of : 
            [{file_name}] at
            try block line number : [{try_block_line_number}]
            and exception block line number : [{exception_block_line_number}]
            error message : [{error_message}]
        """

        return error_message_return
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return CustomException.__name__.str()