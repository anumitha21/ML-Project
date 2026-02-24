import sys #used to get traceback details)

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() #here the info func return thresst hings...tyoe, value and traceback..here we need only treaceback,we ignore 1st two
    file_name = exc_tb.tb_frame.f_code.co_filename #getting the file a=name where error happ
    exc_tb.tb_lineno,str(error)#getting the line number where error happ
    error_message = "Error occurred in script:  [{file_name}] at line number: [{exc_tb.tb_lineno}] with error message: {str(error)}" # custom error message
    return error_message


# it lets you raise your own error with custom message and details
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys): #runs when an erro is created
        super().__init__(error_message) #calling the parent class constructor,if error occurs
        self.error_message = error_message_detail(error_message,error_detail) #calls the prev func for detiled error message

    def __str__(self): #It returns the custom detailed message instead of default Python error text.
        return self.error_message
    #cusotm errors like..model notfound ...usernotfunf in backend api//instead of showing default error message we can show custom error message with details like where the error happend and what is the error message