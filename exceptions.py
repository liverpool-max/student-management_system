from fastapi import HTTPException,status

class DetailHTTPException(HTTPException):
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL = "Server error"
    def __init__(self):
        super().__init__(status_code=self.STATUS_CODE,detail=self.DETAIL)
    
class UserNottFoundException(DetailHTTPException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "User is not found"


class CourseNotFoundException(DetailHTTPException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "Course is not found"

class UserIsExists(DetailHTTPException):
    STATUS_CODE=status.HTTP_400_BAD_REQUEST
    DETAIL = "User is exists"


class Unauthorized(DetailHTTPException):
    STATUS_CODE=401
    DETAIL = "Permission denied"