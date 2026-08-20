from fastapi import HTTPException, status

def bad_request(message: str):
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=message
    )

def forbidden(message: str):
    return HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=message
    )

def not_found(message: str):
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=message
    )