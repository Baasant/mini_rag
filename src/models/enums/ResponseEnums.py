#TO SAVE CONSTANTS
from enum import Enum

class ResponseSignal(Enum):
    FILE_VALIDATED_SUCCESS="file_validate_successfully"
    FILE_TYPE_NOT_SUPPORTED="file_types_not_supported"
    FILE_SIZE_EXCEEDED="file_size_is_excedded"
    FILE_UPLOAD_SUCESS="file_uploaded_success"
    FILE_UPLOADED_FILED="file_iploaded_filed"
    PROCESSING_FAILED="processing_failed"
    PROCESSING_SUCCESS="processing_sucess"
    


