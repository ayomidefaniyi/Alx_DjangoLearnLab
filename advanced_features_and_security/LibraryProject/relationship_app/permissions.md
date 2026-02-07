# Permissions and Groups Setup

## Custom Permissions Added to Book Model
- can_view
- can_create
- can_edit
- can_delete

## Groups Created
- Editors: can_view, can_create, can_edit
- Viewers: can_view
- Admins: all permissions

## Enforcement in Views
Views use @permission_required decorator to restrict access.
Example:
@permission_required('relationship_app.can_edit', raise_exception=True)
