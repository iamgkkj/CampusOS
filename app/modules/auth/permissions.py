from app.core.security import has_role

# Define specific roles using core security decorators
student_only = has_role('student')
teacher_only = has_role('teacher')
admin_only = has_role('admin')
staff_only = has_role('teacher', 'admin')
