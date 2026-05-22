class CampusOSError(Exception):
    """Base exception class for all CampusOS application errors."""
    code = "INTERNAL_SERVER_ERROR"
    status_code = 500
    
    def __init__(self, message: str, details: dict = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}

class ValidationError(CampusOSError):
    """Raised when request payload or form validation fails."""
    code = "VALIDATION_ERROR"
    status_code = 400

class BusinessRuleError(CampusOSError):
    """Raised when a business rule or service validation constraint is violated."""
    code = "BUSINESS_RULE_VIOLATION"
    status_code = 422

class AuthenticationError(CampusOSError):
    """Raised when user credentials or token verification fails."""
    code = "UNAUTHORIZED"
    status_code = 401

class ForbiddenError(CampusOSError):
    """Raised when a user lacks permission to perform a specific action (RBAC)."""
    code = "FORBIDDEN"
    status_code = 403

class ResourceNotFoundError(CampusOSError):
    """Raised when a requested resource is missing in the system."""
    code = "NOT_FOUND"
    status_code = 404
